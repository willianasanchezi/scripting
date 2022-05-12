<#
Inicio rápido: Introducción a la CLI de Voz de Azure
https://docs.microsoft.com/es-es/azure/cognitive-services/speech-service/spx-basics?tabs=windowsinstall%2Cterminal
https://docs.microsoft.com/es-es/azure/cognitive-services/speech-service/spx-batch-operations
#>

<#
# En este script se convierte audio a texto
# Primero instalar CLI
dotnet tool install --global Microsoft.CognitiveServices.Speech.CLI
#>
spx

#spx config @key --set SUBSCRIPTION-KEY
#spx config @region --set REGION

spx --% config @key --set 123ab456cdef789ghi
spx --% config @region --set centralus

spx --% config @key
spx --% config @region

spx recognize --file E:\Audios\Audio_test01.wav --output file E:\Audios\ResultadoAudio.tsv --source es-ES

spx --% config @key --clear
spx --% config @region --clear
