from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI! I am bhaskar! Hello !I have made changes to bhaskar file"}
