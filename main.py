from fastapi import FastAPI
from models import Data
from encrypt import encrypt

app = FastAPI()

@app.get("/")
async def main() -> dict:
    return {
        "message": "Start mini project encrypt"
    }


@app.post("/encrypt/hash")
async def hashing(body: Data) -> dict:
    hashed_data = await encrypt(algorithm=body.algorithm, data=body.text, salt=body.salt)
    if hashed_data:
        return {
            "header": {
                "isSuccess": "true",
                "errorCode": 0,
                "errorMessage": ""
            },
            "encrypt": {
                "algorithm": f"{body.algorithm}",
                "encData": f"{hashed_data}"
            }
        }
    else:
        return {
            "header": {
                "isSuccess": "false",
                "errorCode": 1,
                "errorMessage": "Failed encrypt"
            },
            "encrypt": {
                "algorithm": f"{body.algorithm}",
                "encData": None
            }
        }