from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    url="sqlite:///database_v2.db",
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush= False,
    autocommit=False
)

Base = declarative_base()