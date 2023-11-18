#!/bin/bash
echo "Executing post deployment script"
# add rds creds to bashrc since aws doesn't do it
# while read -r line; do echo "export $line" >> ~/.bashrc; done < /opt/elasticbeanstalk/deployment/env
# add env vars to current session
# export $(cat /opt/elasticbeanstalk/deployment/env | xargs)
# apply migrations
cd /var/app/current
source /var/app/venv/*/bin/activate
python3 manage.py migrate
python3 manage.py createsuperuser --noinput || true #do not fail in case this the not the first deployment and username is taken
