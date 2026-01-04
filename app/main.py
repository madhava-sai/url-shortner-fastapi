from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.db.session import engine, init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""

    # Startup: Initialize database
    init_db(settings.database_url, echo=settings.debug)

    print("Application starting up...")
    print(f"Database: Connected to {settings.database_url.split('@')[1]}")

    yield # Application runs here

    # Shutdown: Clean up resources
    print("Application shutting down...")
    if engine:
        await engine.dispose()

# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0",
    description="A production-grade URL shortner with analytics",
    lifespan=lifespan
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return{
        "message": "URL Shortner API is running!",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "redis": "not connected yet"
    }