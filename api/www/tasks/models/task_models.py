from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    priority: str = "medium"


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
    priority: str | None = None


class Task(BaseModel):
    id: int
    title: str
    completed: bool
    priority: str
