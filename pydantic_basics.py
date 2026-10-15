from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age: int


patient_info = {'name':'abdullah', 'age':30}
patient1 = Patient(**patient_info)
# Alternate method of above is to pass name, age by keyword arguments
print(patient1.name)
print(patient1.age)


#Pydantic also does type casting if possible to avoid always raising error
