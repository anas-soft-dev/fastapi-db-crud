from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Column
# from app.models.post import Post

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name:Mapped[str] = mapped_column(String(50))

    email:Mapped[str] = mapped_column(
        unique=True
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )
