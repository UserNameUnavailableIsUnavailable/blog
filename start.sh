#!/usr/bin/bash
# 仅供测试使用，部署时应使用用户服务
BashScriptRoot=$(dirname "$(readlink -f "$0")")
docsify --port 32768 serve $BashScriptRoot/contents
