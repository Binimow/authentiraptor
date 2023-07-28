from fastapi import FastAPI
import authentication.authentication_controller as authentication_controller

app = FastAPI()
app.include_router(
    router=authentication_controller.router,
    prefix="/auth"
)