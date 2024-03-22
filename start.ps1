#!/usr/bin/pwsh
Start-Process -FilePath "/usr/bin/nohup" -ArgumentList "/usr/local/bin/docsify serve $HOME/blog" -RedirectStandardOutput /dev/null
