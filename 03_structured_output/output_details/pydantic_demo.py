from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Student(BaseModel):
    name: str = Field(..., description="The full name of the student")
    age:Optional[int]= None
    email: EmailStr = Field(..., description="The email address of the student")
    cGpa:float = Field(..., ge=0.0, le=4.0, description="The cumulative GPA of the student")

new_student = {'name':"waseem_akram",'email':"waseemshzad@gmail.com",'age':21,'cGpa':3.5}   


Student = Student(**new_student)
print(Student) # name='waseem_akram' age=21 email='waseemshzad@gmail.com' cGpa=3.5
print(type(Student)) # <class '__main__.Student'>

student_dict = dict(Student)

print(student_dict['name'])
Student_json = Student.model_dump_json()