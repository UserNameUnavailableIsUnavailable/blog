#!pwsh
$static = Get-Content ./static.json | ConvertFrom-Json -AsHashTable
foreach ($i in $static.keys)
{
    $filename = Join-Path "./static" $i
    Write-Host $static.$i
    Invoke-WebRequest -Uri $static.$i -OutFile $filename -Proxy http://proxy.macrohard.fun:60000
}
