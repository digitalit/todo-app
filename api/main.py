from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.admin.routes import router as admin_router
from api.www.routes import router as www_router

app = FastAPI()

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Admin endpoints: /admin/...
app.include_router(admin_router, prefix="/admin", tags=["admin"])

# Public/www endpoints: /...
app.include_router(www_router, tags=["www"])
