from fastapi import FastAPI,Request,Body

app = FastAPI()

#i am flying jatt

@app.post("/webhook")
def webhook(body= Body(None)):
    print(body)
    return body

@app.get("/")
def home():
    return "hello world"

#i am 