import logging
import requests

_LOGGER = logging.getLogger(__name__)

class OpenAITTSClient:
    """Handles direct calls to OpenAI's /v1/audio/speech for TTS."""

    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry

        self._api_key = entry.data["api_key"]
        self._voice = entry.data.get("voice")
        # Use instruction fields to flavor the TTS output
        self._affect = entry.data.get("affect_personality", "")
        self._tone = entry.data.get("tone", "")
        self._pronunciation = entry.data.get("pronunciation", "")
        self._pause = entry.data.get("pause", "")
        self._emotion = entry.data.get("emotion", "")
        self._model = "tts-1"  # Standard OpenAI TTS model

    async def get_tts_audio(self, text: str, options: dict | None = None):
        """Generate TTS audio from OpenAI using direct HTTP calls."""
        if options is None:
            options = {}

        voice = options.get("voice", self._voice)
        audio_format = options.get("audio_output", "mp3")

        # Combine instruction fields into a fun/happy prefix
        instructions_parts = []
        if self._affect:
            instructions_parts.append(self._affect)
        if self._tone:
            instructions_parts.append(self._tone)
        if self._pronunciation:
            instructions_parts.append(self._pronunciation)
        if self._pause:
            instructions_parts.append(self._pause)
        if self._emotion:
            instructions_parts.append(self._emotion)
        prefix = " ".join(instructions_parts) + " " if instructions_parts else ""
        full_text = f"{prefix}{text}"  # Prepend instructions to make it funny/happy

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self._model,
            "voice": voice,
            "input": full_text,
            "response_format": audio_format
        }

        def do_request():
            resp = requests.post(
                "https://api.openai.com/v1/audio/speech",
                headers=headers,
                json=payload,
                stream=True
            )
            resp.raise_for_status()

            audio_data = b""
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    audio_data += chunk
            return audio_format, audio_data

        try:
            return await self.hass.async_add_executor_job(do_request)
        except Exception as e:
            _LOGGER.error("Error generating OpenAI TTS audio: %s", e)
            return None, None
