from fastapi import FastAPI
from presentation.viewmodels.models import *
from persistence.utils import get_engine


from presentation.controllers.environments_controllers import \
    router as environments_router, prefix as environment_prefix
# from presentation.controllers.devices_controllers import\
#     router as devices_router, prefix as device_prefix

app = FastAPI()
engine = get_engine()
SQLModel.metadata.create_all(engine)

app.include_router(environments_router, prefix=environment_prefix)
# app.include_router(devices_router, prefix=device_prefix)