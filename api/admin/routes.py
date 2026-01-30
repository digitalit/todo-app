from fastapi import APIRouter

from api.admin.todos.routes.todo_routes import router as todo_router
from api.admin.tasks.routes.task_routes import router as task_router

router = APIRouter()


@router.get("/health", operation_id="adminHealth")
def health():
    return {"status": "ok"}


router.include_router(todo_router)
router.include_router(task_router)
