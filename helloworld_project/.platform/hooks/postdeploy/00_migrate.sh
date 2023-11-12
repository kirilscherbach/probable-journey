echo "Executing post deployment script"
export $(cat /opt/elasticbeanstalk/deployment/env | xargs)
cd /var/app/current
source /var/app/venv/*/bin/activate && python3 manage.py migrate
