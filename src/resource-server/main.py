from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/potatoes")
async def root():
    return [
        {
            "id": 1,
            "name": "Beautiful Potato"
        },
        {
            "id": 2,
            "name": "Hummmfff Potato"
        }
    ]