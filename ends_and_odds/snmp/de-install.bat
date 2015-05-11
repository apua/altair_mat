@echo off
 
:: (c) Copyright 2013 Hewlett-Packard Development Company, L.P.
 
set wdir=%windir%
set FEATURE=SNMP-Service
set RESULTFILE="%wdir%\SNMPUnInstallResult.xml"
 
:: Try PowerShell if exists
for %%X in (powershell.exe) do (set FOUND1=%%~$PATH:X)
if defined FOUND1 (
   echo Import-module servermanager > "%wdir%\FeatureUninstall.ps1"
   echo Remove-WindowsFeature -Name %FEATURE% -Restart >> "%wdir%\FeatureUninstall.ps1"
   powershell.exe -ExecutionPolicy Unrestricted -NoLogo -NonInteractive -NoProfile -WindowStyle Hidden -File "%wdir%\FeatureUninstall.ps1"
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
