Start-Process powershell -ArgumentList "-noexit -command ""& '$PSScriptRoot\authorization-server_api.ps1'"""
Start-Process powershell -ArgumentList "-noexit -command ""& '$PSScriptRoot\resource-server.ps1'"""
Start-Process powershell -ArgumentList "-noexit -command ""& '$PSScriptRoot\client_ui.ps1'"""
Start-Process powershell -ArgumentList "-noexit -command ""& '$PSScriptRoot\authorization-server_ui.ps1'"""