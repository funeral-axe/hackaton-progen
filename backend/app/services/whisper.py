from functools import lru_cache

from faster_whisper import WhisperModel

from app.core.config import settings


class WhisperService:

    def __init__(self):
        self.model = WhisperModel(
            settings.whisper_model_path,
            device=settings.whisper_device,
            compute_type=settings.whisper_compute_type,
        )

    def transcribe(self, file_path: str):
        segments, info = self.model.transcribe(
            file_path,
            beam_size=5,
            vad_filter=True,
        )

        result = []

        for segment in segments:
            result.append(
                {
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text.strip(),
                }
            )

        return {
            "language": info.language,
            "duration": info.duration,
            "segments": result,
            "text": " ".join(
                x["text"] for x in result
            ),
        }


@lru_cache
def get_whisper_service():
    return WhisperService()