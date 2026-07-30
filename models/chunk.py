from pydantic import BaseModel

class Chunk(BaseModel):
    id: int
    document_name: str
    chunk_index: int
    text: str
    embedding: list[float]