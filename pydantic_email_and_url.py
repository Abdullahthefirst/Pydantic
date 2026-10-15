from pydantic import BaseModel, EmailStr, AnyUrl
#The url must have protocol specified
from typing import List, Dict
#Data Validation
def add_patient_info(info:Patient):
    print(info.name)
    print(info.age)
    print("Data successfully added")
class Patient(BaseModel):
    name: str 
    age: int 
    linkedin_url = AnyUrl
    email: EmailStr
    weight: float 
    married: bool 
    allergies: List[str]
    contact_details: dict[str, str]

patient_info = {'name':'abdullah', 'age':30, 'weight':75.2,'email':'aka@x.com', 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'5626556'}, 'linkedin_url':'http://linkedin.com/in/abdullahthefirst'}
patient1 = Patient(**patient_info)

add_patient_info(patient1)
