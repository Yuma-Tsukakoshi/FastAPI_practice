from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index(): #非同期処理
    return {"message": "Hello, World"}