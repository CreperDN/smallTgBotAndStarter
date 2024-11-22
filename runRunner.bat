@echo off

echo Set WshShell = CreateObject("WScript.Shell") >start.vbs
echo WshShell.Run "cmd.exe /c run.bat", 0, false>>start.vbs

cscript.exe //b //nologo start.vbs