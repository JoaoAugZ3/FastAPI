#FEITO

from ulid import ulid
from sqlmodel import SQLModel, Field, Relationship

class EnvironmenteBase(SQLModel):
    description: str
    icon: str | None = Field(default='icon.png')
    
    
class Environment(EnvironmenteBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)
    
    devices: list['Device'] = Relationship(back_populates='environment')
    
class EnvironmentRead(EnvironmenteBase):
    id: str
    
class DeviceBase(SQLModel):
    description: str
    icon: str | None = Field(default='icon.png')
    status_conn: bool | None = Field(default=True)
    status: bool | None = Field(default=False)
    
    environmet_id: str | None = Field(default=None, foreign_key='environment.id')
    
class DeviceWithEnvironment(DeviceBase):
    id: int
    environmet: EnvironmentRead | None = None   

class Device(DeviceBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    environment: Environment | None = Relationship( back_populates='device')
    