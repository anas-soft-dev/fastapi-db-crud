from app.database import Base
from sqlalchemy.orm import Mapped,MappedColumn, relationship

class Category(Base):
    __tablename__ = "categories"
    id:Mapped[int] = MappedColumn(
        primary_key = True
    )

    title:Mapped[str]

    order: Mapped[int]

    posts: Mapped[list["Post"]] = relationship(
        back_populates= "category"
    )