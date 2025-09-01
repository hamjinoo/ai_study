from pydantic import BaseModel
from pathlib import Path

class Settings(BaseModel):
    data_dir: Path = Path(__file__).resolve().parents[1] / "data"
    index_dir: Path = Path(__file__).resolve().parents[1] / "index"
    max_context_docs: int = 4
    top_k: int = 8
    chunk_size: int = 512

settings = Settings()
