from fastapi import FastAPI

app = FastAPI()

app.post("/webhook")
def webhook(body:any):
    return body

app.get("/")
def home():
    return "hello world"