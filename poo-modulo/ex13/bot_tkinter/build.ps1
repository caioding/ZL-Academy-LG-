$exclude = @("venv", "bot_tkinter.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_tkinter.zip" -Force