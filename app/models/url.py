from sqlalchemy import Column, String, Integer, Boolean, Text
from app.models.base import BaseModel

class URL(BaseModel):
    """URL model for storing shortened URLs"""

    __tablename__ = "urls"

    # Original long URL
    original_url = Column(Text, nullable=False, index=True)

    # Short code (e.g., "asdh123")
    short_code = Column(String(20), unique=True, nullable=False, index=True)

    # Custom alias (optional, user-defined)
    custom_alias = Column(String(50), unique=True, nullable=True, index=True)

    # Click tracking
    click_count = Column(Integer, default=0, nullable=False)

    # Status flags
    is_active = Column(Boolean, default=True, nullable=False)

    # Optional: User who created (TODO: add this once user model is created)
    # user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Optional: Expiration
    # expires_at = Column(DateTime(timezone=True), nullable=False)

    def __repr__(self):
        return f"<URL {self.short_code} -> {self.original_url[:50]}...>"