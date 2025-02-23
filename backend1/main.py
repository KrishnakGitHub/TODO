from fastapi import FastAPI
from dotenv import load_dotenv
from database import SessionLocal, engine, DBContext

load_dotenv()

app = FastAPI()

def get_db():
    with DBContext() as db:
        yield db

@app.get('/')
def root():
    return {"Status": 200, "Message": "Request Successfull!"}


@app.get("/register")
def get_register():
    return {"Status": 200, "title": "Register"}