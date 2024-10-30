$exclude = @("venv", "API_Metropolitana_IFAM.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "API_Metropolitana_IFAM.zip" -Force