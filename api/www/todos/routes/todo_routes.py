from fastapi import APIRouter, HTTPException

from api.www.todos.models.todo_models import Todo, TodoCreate, TodoUpdate

router = APIRouter()

# In-memory storage (replace with a database in production)
todos: dict[int, Todo] = {}
next_todo_id = 1


@router.get("/todos", response_model=list[Todo], operation_id="wwwListTodos")
def list_todos():
    return list(todos.values())


@router.post("/todos", response_model=Todo, operation_id="wwwCreateTodo")
def create_todo(todo_data: TodoCreate):
    global next_todo_id

    todo = Todo(
        id=next_todo_id,
        title=todo_data.title,
        completed=todo_data.completed,
        priority=todo_data.priority,
    )
    todos[next_todo_id] = todo
    next_todo_id += 1
    return todo


@router.get("/todos/{todo_id}", response_model=Todo, operation_id="wwwGetTodo")
def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@router.put("/todos/{todo_id}", response_model=Todo, operation_id="wwwUpdateTodo")
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


@router.delete("/todos/{todo_id}", status_code=204, operation_id="wwwDeleteTodo")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
