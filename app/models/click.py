from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import BaseModel

class Click(BaseModel):
    """Click tracking model for analytics
    Stores each click/redirect event"""

    __tablename__ = "clicks"

    # Foreign key to URL
    url_id = Column(Integer, ForeignKey("urls.id", ondelete="CASCADE"), nullable=False, index=True)

    # Request metadata
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(500), nullable=True)
    referer = Column(String(500), nullable=True)

    # Geo-location (TODO: Popolate this later with an API)
    country = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)

    # Timestamp (separate from BaseModel's created_at for clarity)
    clicked_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)

    # Relationship to URL model
    url = relationship("URL", backref="clicks")

    def __repr__(self):
        return f"<Click {self.url_id} from {self.ip_address} at {self.clicked_at}>"