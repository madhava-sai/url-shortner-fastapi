from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# Base class for all models
Base = declarative_base()

# Engine and sesison will be None initially
engine = None
AsyncSessionLocal = None

def init_db(database_url: str, echo: bool = False):
    """Initialize database engine and session factory.
    Call this from FastAPI app startup"""

    global engine, AsyncSessionLocal

    # Create async database engine
    engine = create_async_engine(
        database_url,
        echo=echo, # Log SQL queries in debug mode
        future=True,
        pool_pre_ping=True,
        pool_size=10, # Number of connections to keep open
        max_overflow=20 # Additional connections if pool is exhausted
    )

    # Create async session factory
    AsyncSessionLocal = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False, # Don't expire objects after commit
        autocommit=False,
        autoflush=False
    )

async def get_db():
    """Dependency function to get database session.
    Yields a session and ensures it's closed after use."""
    if AsyncSessionLocal is None:
        raise RuntimeError("Database is not initialized. Call init_db() first.")
    
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
