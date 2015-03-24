@echo off
 
:: (c) Copyright 2013 Hewlett-Packard Development Company, L.P.
 
set wdir=%windir%
set FEATURE1=SNMP-Service -IncludeManagementTools
set FEATURE2=SNMP-WMI-Provider
set RESULTFILE="%wdir%\SNMPInstallConfigureResult.xml"

:: Try PowerShell if exists
for %%X in (powershell.exe) do (set FOUND1=%%~$PATH:X)
if defined FOUND1 (
   echo Import-module servermanager > "%wdir%\SNMPFeatureInstall.ps1"
   echo Add-WindowsFeature -Name %FEATURE1% -logPath %RESULTFILE% >> "%wdir%\SNMPFeatureInstall.ps1"
   echo Add-WindowsFeature -Name %FEATURE2% -logPath %RESULTFILE% >> "%wdir%\SNMPFeatureInstall.ps1"
   echo reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ValidCommunities" /v Private /t REG_DWORD /d 4 /f >> "%wdir%\SNMPFeatureInstall.ps1"
   echo reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ValidCommunities" /v Public /t REG_DWORD /d 8 /f >> "%wdir%\SNMPFeatureInstall.ps1"
   powershell.exe -ExecutionPolicy Unrestricted -NoLogo -NonInteractive -NoProfile -WindowStyle Hidden -File "%wdir%\SNMPFeatureInstall.ps1"
   set rc=%errorlevel%
   goto EndWithFailureMessage
   
  
)
if NOT defined rc (
   echo PowerShell and ServerManagerCmd were not found and could not set %FEATURE%
   set rc=999
   goto End
)
  
:EndWithFailureMessage
if NOT %rc%==0 (
   echo PowerShell and ServerManagerCmd Add Windows Feature failed to install %FEATURE%:  error code %rc%
   echo Refer to %RESULTFILE% log file.
)
  
:End
exit /B %rc%
