from fastapi import FastAPI,Request

app = FastAPI()

#i am flying jatt

@app.post("/webhook")
def webhook(body:Request):
    return body

@app.get("/")
def home():
    return "hello world"