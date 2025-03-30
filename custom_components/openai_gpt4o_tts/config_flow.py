import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY
from homeassistant.core import callback

from .const import (
    DOMAIN,
    CONF_VOICE,
    DEFAULT_VOICE,
    OPENAI_TTS_VOICES
)

_LOGGER = logging.getLogger(__name__)

class OpenAITTSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle OpenAI TTS setup flow."""
    
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Initial configuration step."""
        errors = {}

        if user_input is not None:
            # Create the config entry with only TTS-relevant data
            _LOGGER.debug("Creating config entry with API key and voice: %s", user_input)
            return self.async_create_entry(title="OpenAI TTS", data=user_input)

        # Show the setup form with only TTS fields
        data_schema = vol.Schema({
            vol.Required(CONF_API_KEY): str,
            vol.Optional(CONF_VOICE, default=DEFAULT_VOICE): vol.In(OPENAI_TTS_VOICES),
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return OpenAITTSOptionsFlowHandler(config_entry)


class OpenAITTSOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle editing OpenAI TTS settings."""

    def __init__(self, config_entry):
        """Initialize the options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Show the options form with pre-filled values."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Retrieve existing settings from config entry
        existing_settings = self.config_entry.options or self.config_entry.data

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(CONF_VOICE, default=existing_settings.get(CONF_VOICE, DEFAULT_VOICE)): vol.In(OPENAI_TTS_VOICES),
            })
        )
