
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"
#db_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)