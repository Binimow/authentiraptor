.\venv\Scripts\Activate.ps1
Set-Location src\authorizationserver\backend
uvicorn main:app --reload --port 8000