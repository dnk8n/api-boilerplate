from pydantic import BaseModel


class Root(BaseModel):
    msg: str
