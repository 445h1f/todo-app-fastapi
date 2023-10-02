from pydantic import BaseModel
from typing import List


# data model for adding todo
class Todo(BaseModel):
    id : int
    item : str

    # sample schema for doc
    class Config:
        json_schema_extra = {
            "example": {
                "id" : 1,
                "item": "Complete FastAPI Book",
            }
        }


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