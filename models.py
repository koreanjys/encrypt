from pydantic import BaseModel
from typing import Optional

class Data(BaseModel):
    algorithm: str
    salt: Optional[str] = None
    text: str