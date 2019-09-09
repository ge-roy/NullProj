$PCInfo = gwmi win32_OperatingSystem
$MemGb = ($PCInfo.FreePhysicalMemory / 1024) / 1024

$CPUInfo = Get-WmiObject win32_processor
$CPUPerc = $CPUInfo.LoadPercentage

#$MemGb
#$CPUPerc

If (($MemGb -le 10) -or ($CPUPerc -ge 95)){
    net stop MSSQLSERVER
    net start MSSQLSERVER
    C:\Py\MemoryUsageControl\WPy-3662\python-3.6.6.amd64\python.exe C:\Py\MemoryUsageControl\report.py
}
