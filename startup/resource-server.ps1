.\venv\Scripts\Activate.ps1
Set-Location src\resource-server
uvicorn main:app --reload --port 8002