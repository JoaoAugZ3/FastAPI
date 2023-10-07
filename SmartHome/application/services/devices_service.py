from fastapi import FastAPI
from sqlmodel import select, delete, Session, update
from ...persistence.utils import get_engine
from ...presentation.viewmodels.models import *

class DeviceService:
    def __init__(self):
        self.session = Session(get_engine())


    def get_all_devices(self):
        sttm = select(Device)
        devices = self.session.exec(sttm).fetchall()
        self.session.close()

        return devices


    def get_devices_for_environment(self):
        sttm = select(Device).where(Device.environmet_id == Environment.id)
        devices = self.session.exec(sttm).fetchall()
        self.session.close()

        return devices


    def create_device(self, device:Device):
        self.session.add(Device)
        self.session.commit()
        self.session.refresh(device)


    def move_device(self, id_origem: str, id_dispo: int, id_destino:str):
        environment = self.session.exec(select(Environment).where(Environment.id == id_origem))
        environment_destiny = self.session.exec(select(Environment).where(Environment.id == id_destino))
        device = self.session.exec(select(Device).where(Device.environmet_id == environment.id and id_dispo == Device.id)).one()
        device.environmet_id = environment_destiny.id
        self.session.add(device)
        self.session.commit()
        self.session.refresh(device)
        self.session.close()

        # d = self.session.update(device).where
        # sttm =self.session.delete(device).where(environment.id == id_origem)
        # sttm = self.session.add(device).where(environment_destiny)

    