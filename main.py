from fastapi import FastAPI
from typing import Optional #パラメータは任意となる

app = FastAPI()

@app.get("/")
async def index(): #非同期処理
    return {"message": "Hello, World"}

# パスパラメータの取得
@app.get("/countries/{country_name}")
async def country(country_name : str):
    return {"country_name": country_name}

# クエリパラメータの取得 パラメータの中には含めず、関数の引数に入れる！
@app.get("/countries/")
async def country(country_name : Optional[str] = None, country_num: Optional[int]=None):
    return {
        "country_name": country_name,
        "country_number": country_num
    }

