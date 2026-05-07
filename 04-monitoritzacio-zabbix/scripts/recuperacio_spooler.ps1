$service = "Spooler" 
$log = "C:\zabbix\spooler_recovery.log" 

Add-Content $log "[$(Get-Date)] Intent de recuperacio del servei" 

if ((Get-Service $service).Status -ne "Running") { 
Start-Service $service 
} 

Add-Content $log "[$(Get-Date)] Estat final: $((Get-Service $service).Status)"
