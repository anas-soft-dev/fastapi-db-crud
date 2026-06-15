from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.database import Base
# from app.models.user import User

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(String(50))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    description: Mapped[str]

    user: Mapped["User"] = relationship(
        back_populates="posts"
    )

    category: Mapped["Category"] = relationship(
        back_populates="posts"
    )