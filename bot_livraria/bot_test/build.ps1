$exclude = @("venv", "bot_test.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_test.zip" -Force