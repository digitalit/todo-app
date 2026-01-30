from fastapi import APIRouter, HTTPException

from api.admin.models import Todo, TodoCreate, TodoUpdate

router = APIRouter()

# In-memory storage (replace with a database in production)
todos: dict[int, Todo] = {}
next_id = 1


@router.get("/health", operation_id="wwwHealth")
def health():
    return {"status": "ok"}


@router.get("/todos", response_model=list[Todo], operation_id="adminListTodos")
def list_todos():
    return list(todos.values())


@router.post("/todos", response_model=Todo, operation_id="adminCreateTodo")
def create_todo(todo_data: TodoCreate):
    global next_id

    todo = Todo(
        id=next_id,
        title=todo_data.title,
        completed=todo_data.completed,
        priority=todo_data.priority,
    )
    todos[next_id] = todo
    next_id += 1
    return todo


@router.get("/todos/{todo_id}", response_model=Todo, operation_id="adminGetTodo")
def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@router.put("/todos/{todo_id}", response_model=Todo, operation_id="adminUpdateTodo")
def update_todo(todo_id: int, todo_data: TodoUpdate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo = todos[todo_id]

    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.completed is not None:
        todo.completed = todo_data.completed
    if todo_data.priority is not None:
        todo.priority = todo_data.priority

    return todo


@router.delete("/todos/{todo_id}", status_code=204, operation_id="adminDeleteTodo")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
