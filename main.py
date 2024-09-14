from fastapi import FastAPI,Request,Body

app = FastAPI()

#i am flying jatt

@app.post("/webhook")
def webhook(body= Body(None)):
    print(body)
    return body

#test api 
@app.get("/")
def home():
    return "hello world"


@app.get("/welcome")
def welocme():
    return "Welcome......"
