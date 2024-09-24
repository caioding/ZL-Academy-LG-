$exclude = @("venv", "Clima_Manaus_Bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Clima_Manaus_Bot.zip" -Force