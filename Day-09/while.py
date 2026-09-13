# while use when u dont know the number of rage
#it is base on condition

from time import sleep
from turtle import done


while ! aws ec2 describe-instance-status --instance-ids i-id | grep -q "running"; do
       echo "Waiting for the EC2 instance to be running..."
       sleep 10
   done                 

#log file checking for error and send alert if error found
while true; do
       if tail -n 1 /var/log/app.log | grep -q "ERROR"; then
           send_alert "Error detected in the log."
       fi
       sleep 5
   done
