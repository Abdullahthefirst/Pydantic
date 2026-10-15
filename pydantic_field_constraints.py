from pydantic import BaseModel, EmailStr, AnyUrl, Field
#The url must have protocol specified
#Field is very important for meta data(data about data)
from typing import List, Dict
#Data Validation
def add_patient_info(info:Patient):
    print(info.name)
    print(info.age)
    print("Data successfully added")
class Patient(BaseModel):
    name: str = Field(max_length=50, )
    age: int = Field(gt=0, lt=120)
    linkedin_url = AnyUrl
    email: EmailStr
    weight: float = Field(gt=0)
    married: bool 
    allergies: List[str] = Field(max_length=5)
    contact_details: dict[str, str]

#
patient_info = {'name':'abdullah', 'age':30, 'weight':75.2,'email':'aka@x.com', 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'5626556'}, 'linkedin_url':'http://linkedin.com/in/abdullahthefirst'}
patient1 = Patient(**patient_info)

add_patient_info(patient1)
