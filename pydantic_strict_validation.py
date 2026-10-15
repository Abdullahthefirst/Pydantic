#Avoiding the Pydantic type cohersion by strict=True in Field

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Annotated, Optional
#Data Validation
def add_patient_info(info:Patient):
    print(info.name)
    print(info.age)
    print("Data successfully added")
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of patient in less than 50 characters", examples=['abdullah', 'nitish'])]
    age: int = Field(gt=0, lt=120)
    linkedin_url : AnyUrl
    email: EmailStr
    weight: float = Field(gt=0, strict=True)
    married: Annotated[bool, Field(default=False, description="Is the patient married or not?")] 
    allergies: Annotated[Optional[List[str]], Field(max_length=5)]
    contact_details: dict[str, str]

#
patient_info = {'name':'abdullah', 'age':30, 'weight':75.2,'email':'aka@x.com', 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'5626556'}, 'linkedin_url':'https://linkedin.com/in/abdullahthefirst'}
patient1 = Patient(**patient_info)

add_patient_info(patient1)
