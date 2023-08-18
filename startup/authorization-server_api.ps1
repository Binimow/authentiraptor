.\venv\Scripts\Activate.ps1
Set-Location src\authorization-server\backend
uvicorn main:app --reload --port 8000