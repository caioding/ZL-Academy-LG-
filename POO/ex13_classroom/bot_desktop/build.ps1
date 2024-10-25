$exclude = @("venv", "bot_desktop.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_desktop.zip" -Force