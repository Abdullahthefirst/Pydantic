#Field Validator --> Specific data validation e.g. email@uet.com validation
#Field Validator can do both customization and validation of data

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Annotated, Optional
#Data Validation
def add_patient_info(info:Patient):
    print(info.name)
    print(info.age)
    print("Data successfully added")
class Patient(BaseModel):
    name: str
    age: int
    linkedin_url : AnyUrl
    email: EmailStr
    weight: float 
    married: bool
    allergies: Optional[List[str]]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['htfs.com', 'icsc.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        else:
            return value

    @field_validator('name', mode='after') # mode= 'after' gives the value to it after type cohersion ; mode= 'before' gives value to it before type cohersion
    @classmethod
    def name_validator(cls, value):
        return value.upper()


#
patient_info = {'name':'abdullah', 'age':30, 'weight':75.2,'email':'aka@htfs.com', 'married':True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@htfs.com', 'phone':'5626556'}, 'linkedin_url':'https://linkedin.com/in/abdullahthefirst'}
patient1 = Patient(**patient_info)

add_patient_info(patient1)
