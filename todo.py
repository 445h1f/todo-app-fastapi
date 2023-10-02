from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()


todo_list = [] # list to store todos


# path for adding todo
@todo_router.post('/todo', status_code=201)
async def add_todo(todo:Todo):
    todo_list.append(todo)
    return {"message" : "todo added successfully"}



# path for getting todos
@todo_router.get('/todo', response_model=TodoItems)
async def get_todo():
    return {"todos" : todo_list}



#path for getting single todo by id
@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id:int=
                            Path(..., title='The ID of the TODO to retrieve')) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    print('gere')
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="no todo found with given id"
    )



# path for updating todo
@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data:TodoItem,
                    todo_id:int=Path(..., title="The ID of todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item

            return {"message": "successfully updated."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="no todo found with given id"
    )



# delete method to delete single todo
@todo_router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id:int
                            =Path(..., title="The ID of todo to be deleted.")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]

            return {"message": "deleted successfully."}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="no todo found with given id",
    )


# delete all todos
@todo_router.delete('/todo')
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message":"deleted all todos"}