from pydantic import BaseModel

class ImageDate(BaseModel):
    image: str
    dict_of_vars: dict
