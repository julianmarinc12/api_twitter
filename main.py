#python
from datetime import date, datetime
from typing import Optional, List
from uuid import UUID

#pydantic
from pydantic import BaseModel, EmailStr, Field

#FastApi
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

#models
class UserBase(BaseModel):
    user_id : UUID =Field(...)
    email : EmailStr =Field(...)

class UserLogin(UserBase):
      password : str =Field(
        min_length=8,
        max_length=20
    )

class User(UserBase):

    firt_name : str =Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name : str =Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class  Tweet(BaseModel):
    tweet_id: UUID = Field()
    content: str = Field(
        ...,
        min_length=10,
        max_length=250)
    creared_at: datetime =Field(default=datetime.now())
    update_at: Optional[datetime] =Field(default=None)
    by: User =Field(...)

#path Operations
@app.get(path="/")
def home():
    return {"Twitter API":"working"}

# Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary= "registrer a user",
    tags= ["Users"]
)
def signup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "login user",
    tags= ["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary= "Show all users",
    tags= ["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "show a user",
    tags= ["Users"]
)
def show_a_user():
    pass

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary= "registrer a user"
    tags= ["Users"]
)
def signup():
    pass

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary= "registrer a user"
    tags= ["Users"]
)
def signup():
    pass

# Tweets

