#! /bin/bash
VIRTUAL_ENVS=.venvs/vlogger

if [ -d  ${VIRTUAL_ENVS} ]; then
    echo "激活虚拟环境"
    source ${VIRTUAL_ENVS}/bin/activate
else 
    echo "创建虚拟环境"
    python3 -m virtualenv ${VIRTUAL_ENVS}
    source ${VIRTUAL_ENVS}/bin/activate
    pip install django django-recaptcha mysqlclient django-simple-captcha
fi