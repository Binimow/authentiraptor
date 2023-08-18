.\venv\Scripts\Activate.ps1
Set-Location src\authorization-server
uvicorn main:app --reload --port 8000