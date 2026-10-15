from pydantic import BaseModel
from typing import List, Dict
def add_patient_info(info:Patient):
    print(info.name)
    print(info.age)
    print("Data successfully added")
class Patient(BaseModel):
    name: str 
    age: int 
    weight: float 
    married: bool 
    allergies: List[str]
    contact_details: dict[str, str]

patient_info = {'name':'abdullah', 'age':30, 'weight':75.2, 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'5626556'}}
patient1 = Patient(**patient_info)

add_patient_info(patient1)
