# OverSee

### University Final Year Project 
> Learning Management System for Teachers and Students - Backend API's

## Functionality
1. Admin: user management
2. Teacher: Create classroom, upload topics, create simple exam, create notices
3. Student: joun classroom to get the topics, attend exams, get notices  

## .env
```
SECRET_KEY = a7fc60e3f027b856de1a4815188321ea786bf25fa1860d31688fd98b2c530bd0
ALGORITHM = HS256
DATABASE_URL = mysql+mysqlconnector://root:@localhost:3306/oversee
URL_ONE = http://localhost:8000
URL_TWO = https://localhost:8000
```

## installation

```
pip3 install -r requirements.txt
```

## migration

```
cd src/
alembic upgrade head
```

## Run application

```
cd src/
python3 main.py
```
