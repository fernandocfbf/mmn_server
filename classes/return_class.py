from pydantic import BaseModel, Field

class ReceiveImage(BaseModel):
    data: str = Field(..., example="base64-string")

class ReturnModel(BaseModel):
    datetime: str = Field(..., example="2021-12-09 10:42")
    data: list = Field([], example=[123])
    status: int = Field(..., example=200)
    description: str = Field(..., example="some random description")
