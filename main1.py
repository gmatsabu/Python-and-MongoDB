from mongoengine import *

from datetime import datetime

import os

import json

connect(db ="umuziprospect",username="root",password="pass",authentication_source="admin",host="localhost",port=27018)

# Defining Documents

class Visitor(Document):
    visitor_name = StringField(unique=True,required=True)
    age = IntField(required=True)
    email = EmailField(unique=True)
    date_of_visit = DateTimeField(default=datetime.utcnow)
    name_of_a_person_who_assigned_the_visit = StringField(required=True)
    comments = StringField(max_length=50)
    admin = BooleanField(default=False)
  

    def json(self):
        visitor_dict = {
            "visitor_name":self.visitor_name,
            "age":self.age,
            "email":self.email,
            "date_of_visit":self.date_of_visit,
            "name_of_a_person_who_assigned_the_visit":self.name_of_a_person_who_assigned_the_visit,
            "comments":self.comments
        }
        return json.dumps(visitor_dict)

    meta = {
        "indexes": ["visitor_name","email"],
        "ordering":["-date_of_visit"]
    }    

visitor = Visitor(
    visitor_name = "Thabo",
    email = "thabo@gmail.com",
    age = 25,
    name_of_a_person_who_assigned_the_visit="Tshepiso",
    comments="I looking for a new accomodation",
)    

visitor.admin = True

try:
   visitor.save()

except NotUniqueError:
    print("Username or email is not Unique Please try again")