from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int]

class Users(BaseModelModify):
    login: str
    password: str
    power_level: Optional[int]

class Applications(BaseModelModify):
    Application_number: Optional[str]
    Date_added: Optional[int]
    Fault_type: Optional[str]
    Description_problem: Optional[str]
    id_cars: Optional[int]
    id_client: Optional[int]
    id_application_status: Optional[int]


class Cars(BaseModelModify):
    brand: Optional[str]
    Model: Optional[int]


class Client(BaseModelModify):
    name: Optional[str]
    fio: Optional[str]
    phone: Optional[int]
    Email: Optional[int]

class Application_statuses(BaseModelModify):
    titles_applications: Optional[str]

