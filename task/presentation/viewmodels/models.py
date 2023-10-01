from sqlmodel import SQLModel, Field
from ulid import ULID


class UserBase(SQLModel):
    login: str = Field(nullable=False, unique=True)
    name: str = Field(min_length=6)

class User(UserBase, table=True):
    id: str | None = Field(default=ULID(), primary_key=True)
    password: str = Field(unique=True)


class UserRead(UserBase):
    id: str


class TaskBase(SQLModel):
    decription: str = Field(min_length=6)
    done: bool = Field(default=False)

class Task(TaskBase, table=True):
    id: str | None = Field(default=ULID(), primary_key=True)
    user_id: str | None = Field(default=None ,foreign_key=User.id)

class TaskRead(SQLModel):
    id: str
    owner: User | None = None