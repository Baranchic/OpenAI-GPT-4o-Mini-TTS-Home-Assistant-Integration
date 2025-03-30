import logging

from homeassistant.components.tts import (
    ATTR_AUDIO_OUTPUT,
    ATTR_VOICE,
    TextToSpeechEntity,
    TtsAudioType,
    Voice,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, OPENAI_TTS_VOICES
from .tts_client import OpenAITTSClient  # Updated import

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback
) -> None:
    """Set up OpenAI TTS from a config entry."""
    client = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([OpenAITTSProvider(config_entry, client)])

class OpenAITTSProvider(TextToSpeechEntity):
    """OpenAI TTS => 'tts.openai_tts_say' in Developer Tools."""

    def __init__(self, config_entry: ConfigEntry, client: OpenAITTSClient) -> None:
        self._config_entry = config_entry
        self._client = client
        self._name = "OpenAI TTS"
        self._attr_unique_id = f"{config_entry.entry_id}-tts"

    @property
    def name(self) -> str:
        """Friendly name for the entity listing."""
        return self._name

    @property
    def default_language(self) -> str:
        """Return the default language code."""
        return "sk"

    @property
    def supported_languages(self) -> list[str]:
        """Return a list of supported languages."""
        return ["sk"]

    @property
    def default_options(self) -> dict:
        """Default TTS options, e.g. mp3."""
        return {ATTR_AUDIO_OUTPUT: "mp3"}

    @property
    def supported_options(self) -> list[str]:
        """Which TTS options can be overridden in the UI or service call."""
        return [ATTR_VOICE, ATTR_AUDIO_OUTPUT]

    async def async_get_tts_audio(
        self, message: str, language: str, options: dict | None = None
    ) -> TtsAudioType:
        """Called by Home Assistant to produce audio from text."""
        audio_format, audio_data = await self._client.get_tts_audio(message, options)
        if not audio_data:
            return None, None
        return audio_format, audio_data

    def async_get_supported_voices(self, language: str) -> list[Voice] | None:
        """Return known OpenAI TTS voices for the voice dropdown."""
        return [Voice(vid, vid.capitalize()) for vid in OPENAI_TTS_VOICES]

    @property
    def extra_state_attributes(self) -> dict:
        """Optional: expose provider name or debug info."""
        return {"provider": self._name}
