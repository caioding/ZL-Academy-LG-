$exclude = @("venv", "2Clima_Manaus_Bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "2Clima_Manaus_Bot.zip" -Force