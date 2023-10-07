
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"
#db_url = f"sqlite:///{sqlite_file_name}"
db_url = 'postgresql://postgres:JoaoAugustoELinfo@db.uukrdqjukgqmuqtsxjxy.supabase.co:5432/postgres'
engine = create_engine(db_url, echo=True)

SQLModel.metadata.create_all(engine)