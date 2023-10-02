from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional


# data model for adding todo
class Todo(BaseModel):
    id : Optional[int]
    item : str

    # sample schema for doc
    class Config:
        json_schema_extra = {
            "example": {
                "id" : 1,
                "item": "Complete FastAPI Book",
            }
        }

    @classmethod
    def as_form(cls, item:str=Form(...), id: Optional[int] = None):
        return cls(id=id, item=item)

# task model for todo
class TodoItem(BaseModel):
    item:str

    class Config:
        json_schema_extra = {
            "example" : {
                "item" : "Complete FastAPI book",
            }
        }



# response model for todo
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example" : {
                "todos":[
                    {
                        "item" : "Complete FastAPI Book",
                    },
                    {
                        "name": "Complete Chapter first",
                    }
                ]
            }
        }