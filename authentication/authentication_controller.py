from fastapi import APIRouter

router = APIRouter(
    tags=["auth"],
)

@router.post("/gettoken")
def get_token():
    return {"message": "Hello World"}