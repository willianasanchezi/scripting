Clear-Host
$anioHoy = (Get-Date).ToString("yyyy")
#$anioHoy
$anioAyer = (Get-Date).AddDays(-1).ToString("yyyy")
#$anioAyer
$mesHoy = (Get-Date).ToString("MM")
#$mesHoy
$mesAyer = (Get-Date).AddDays(-1).ToString("MM")
#$mesAyer
$diaHoy = (Get-Date).ToString("dd")
#$diaHoy
$diaAyer = (Get-Date).AddDays(-1).ToString("dd")
#$diaAyer

if (($anioHoy -eq $anioAyer) -and ($mesHoy -eq $mesAyer)){
    $fecha = $anioHoy + "-" + $mesHoy + "-" + $diaAyer
    #$fecha
}elseif(($anioHoy -eq $anioAyer) -and ($mesHoy -ne $mesAyer)){
    $fecha = $anioHoy + "-" + $mesAyer + "-" + $diaAyer
    #$fecha
}elseif(($anioHoy -ne $anioAyer) -and ($mesHoy -ne $mesAyer)){
    $fecha = $anioAyer + "-" + $mesAyer + "-" + $diaAyer
    #$fecha
}else{
    $fecha = $anioHoy + "-" + $mesHoy + "-" + $diaAyer
    #$fecha
}

function mensajeFinal {
    param (
        $fecha = [string]$fecha,
        $anioAyerc = [string]$var2
        )
        $fechaInicial = $fecha + 'T00:00:00'
        $fechaInicial

        $fechaFinal = $fecha + 'T23:59:59'
        $fechaFinal

        $fechaLogs = $fecha
        $fechaLogs
}
mensajeFinal $fecha
