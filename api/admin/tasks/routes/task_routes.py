from fastapi import APIRouter, HTTPException

from api.admin.tasks.models.task_models import Task, TaskCreate, TaskUpdate

router = APIRouter()

# In-memory storage (replace with a database in production)
tasks: dict[int, Task] = {}
next_task_id = 1


@router.get("/tasks", response_model=list[Task], operation_id="adminListTasks")
def list_tasks():
    return list(tasks.values())


@router.post("/tasks", response_model=Task, operation_id="adminCreateTask")
def create_task(task_data: TaskCreate):
    global next_task_id

    task = Task(
        id=next_task_id,
        title=task_data.title,
        completed=task_data.completed,
        priority=task_data.priority,
    )
    tasks[next_task_id] = task  # correct storage
    next_task_id += 1
    return task


@router.get("/tasks/{task_id}", response_model=Task, operation_id="adminGetTask")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@router.put("/tasks/{task_id}", response_model=Task, operation_id="adminUpdateTask")
def update_task(task_id: int, task_data: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]

    if task_data.title is not None:
        task.title = task_data.title
    if task_data.completed is not None:
        task.completed = task_data.completed
    if task_data.priority is not None:
        task.priority = task_data.priority

    return task


@router.delete("/tasks/{task_id}", status_code=204, operation_id="adminDeleteTask")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
