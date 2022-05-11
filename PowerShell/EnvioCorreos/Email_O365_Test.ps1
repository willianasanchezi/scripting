Clear-Host
<#
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-5.1
#>

$credenciales = get-credential
$De = "williansanchez@outlook.com"
$Para = "willianasanchezi@gmail.com"
$Asunto = "Test Email"
$Mensaje = "Test"
$SMTP = "smtp.office365.com"
$Puerto = "587"
Send-MailMessage -From $De -To $Para -Subject $Asunto -Body $Mensaje -SmtpServer $SMTP -Credential $credenciales -UseSsl -Port $Puerto

