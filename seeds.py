from models import User, Meal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)  # enables communication with the db
session = Session()

import random 
import json # https://www.w3schools.com/python/python_json.asp
import requests # https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
from faker import Faker

fake = Faker()

print("🌱 Seeding DB...") 

# Reset DB
session.query(User).delete()

# Use faker to seed 30 Users
for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name}_{last_name}"
   

    user = User(first_name=first_name, last_name=last_name, username=username, email=fake.ascii_company_email())
    # Now let save all our users to our db
    session.add(user)
    session.commit()

    # first_name
    # last_name
    # username - could do first_name_last_name
    # email - username@gmail.com

# Use the Meals DB to populate the meals
# Link: https://www.themealdb.com/api/json/v1/1/search.php?f=a
# Random element from list: https://docs.python.org/3/library/random.html?highlight=random#random.sample
letters = ["a", "b", "c", "d", "e", "f", "g",]
request =  requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={random.choice(letters)}")
meal_data = json.loads(request.text)

#print(meal_data["meals"])
print(len(meal_data["meals"])) # print the number of meals
print(meal_data["meals"][0]["strMeal"]) # print just the name

meal = Meal(name=meal_data["meals"][0]["strMeal"])

# YOu do this to populate the db and make the data persist
session.add(meal)
session.commit()
print(meal)


print("✅ Done seeding!")

import ipdb; ipdb.set_trace()