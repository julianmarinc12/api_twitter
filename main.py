#python
from datetime import date, datetime
import json
from typing import Optional, List
from unittest import result
from uuid import UUID

#pydantic
from pydantic import BaseModel, EmailStr, Field

#FastApi
from fastapi import Body, FastAPI
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

class UserRegister(User):
    password : str =Field(
        min_length=8,
        max_length=20
    )
class  Tweet(BaseModel):
    tweet_id: UUID = Field()
    content: str = Field(
        ...,
        min_length=10,
        max_length=250)
    created_at: datetime =Field(default=datetime.now())
    updated_at: Optional[datetime] =Field(default=None)
    by: User =Field(...) 

## Register user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary= "registrer a user",
    tags= ["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup a user

    this path operation register a user un the app

    Parameter:
        -Request bodu parameter
            -user: UserRegister
    
    returns a json whit the basic user information:
        -user_id : UUID
        -email: Emailstr
        -first_name: str
        -last_name: str
        -birth_date: date

    """
    with open("users.json", "r+", encoding="utf-8") as f:

        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user



## login user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "login user",
    tags= ["Users"]
)
def login():
    pass

## show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary= "Show all users",
    tags= ["Users"]
)
def show_all_users():
    '''
    Get Users

    This path operation shows all users created in the app

    Parameters: None

    Returns a list with the basic user information of all users created in the app:
    - user_id: UUID
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birth_date: date

    '''
    with open("users.json","r",encoding="utf-8") as f:
        results= json.loads(f.read())
        return results


## show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "show a user",
    tags= ["Users"]
)
def show_a_user():
    pass

## Delete a user
@app.delete(
    path="/signup/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "Delete a user",
    tags= ["Users"]
)
def delete_a_user():
    pass

## Update a user
@app.put(
    path="/signup/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary= "Update a user",
    tags= ["Users"]
)
def delete_a_user():
    pass


# Tweets

## show all tweest
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary= "Show all tweets",
    tags= ["tweets"]
    )
def home():
    """"
    Post a Tweet

    This path operations show all tweet in the app

    Parameters:
    

    Return a json list with all tweets inte app, with the following:
    - tweet_id: UUID
    - content:str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json","r",encoding="utf-8") as f:
        results= json.loads(f.read())
        return results

## post a tweest
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary= "post a tweet",
    tags= ["tweets"]
)
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet

    This path operations post a tweet in the app

    Parameters:
    - Request body parameter
    - tweet: Tweet

    Return a json with the basic tweet information:
    - tweet_id: UUID
    - content:str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

## show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary= "Show a tweet",
    tags= ["tweets"]
)
def show_a_tweet():
    pass

## delete a tweet
@app.get(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary= "detele a tweet",
    tags= ["tweets"]
)
def delete_a_tweet():
    pass

## update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary= "Update a tweet",
    tags= ["tweets"]
)
def update_a_tweet():
    pass