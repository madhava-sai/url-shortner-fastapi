from fastapi import FastAPI
from app.core.config import settings

# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0",
    description="A production-grade URL shortner with analytics"
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
        "database": "not connected yet",
        "redis": "not connected yet"
    }