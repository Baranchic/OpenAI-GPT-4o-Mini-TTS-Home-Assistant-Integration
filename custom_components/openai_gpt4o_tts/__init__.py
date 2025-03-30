import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS
from .tts_client import OpenAITTSClient  # Renamed for clarity

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up OpenAI TTS from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Store the config entry
    hass.data[DOMAIN][entry.entry_id] = entry

    # Initialize the OpenAI TTS client
    hass.data[DOMAIN][entry.entry_id] = OpenAITTSClient(hass, entry)

    # Forward to TTS platform only
    await hass.config_entries.async_forward_entry_setups(entry, ["tts"])

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload OpenAI TTS config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["tts"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
