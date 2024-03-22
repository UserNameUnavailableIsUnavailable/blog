#!/usr/bin/pwsh
Start-Process -FilePath "/usr/bin/nohup"`
-WorkingDirectory "$Env:HOME/blog"`
-ArgumentList "./markdown-blog web --index `"00@欢迎`" --cache 1 --dir `"$Env:HOME/blog/files/`" --fdir `"assets`" --title `"Macrohard`" --icp `"苏ICP备2023037770号-1`" --port 5006"
