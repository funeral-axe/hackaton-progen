import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, UploadFile

from app.services.whisper import (
    WhisperService,
    get_whisper_service,
)

router = APIRouter(
    prefix="/transcriptions",
    tags=["transcriptions"],
)


UPLOAD_DIR = Path("../uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
def transcribe(
    file: UploadFile = File(...),
    whisper: WhisperService = Depends(get_whisper_service),
):
    suffix = Path(file.filename or "").suffix

    filename = f"{uuid.uuid4()}{suffix}"
    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = whisper.transcribe(str(file_path))

    return result