import json
import subprocess
import time


#def generate_image(number_images, start_image):
number_images = 5
start_image = 152

cmd = 'aws ssm send-command --instance-ids i-01d6de0c8312b250c --region us-west-2 --document-name "AWS-RunRemoteScript" --comment "Generate Images" '
par = '--parameters commands=["runuser -l ubuntu -c \'python3.6 /home/ubuntu/stylegan/pretrained_example.py ' + str(number_images) + " " + str(start_image) + '\'"]'
cmdpar = cmd+par
print(cmdpar)

tmp = subprocess.Popen('aws ec2 start-instances --instance-ids i-01d6de0c8312b250c', shell=True, stdout=subprocess.PIPE).communicate()
time.sleep(120)

# Wait for instance to be set to running state
jstr = {'InstanceStatuses':[{'InstanceState':{'Name':'test'}}]}
while (jstr['InstanceStatuses'][0]['InstanceState']['Name'] != "running"):
    result = subprocess.Popen('aws ec2 describe-instance-status --instance-ids i-01d6de0c8312b250c', shell=True, stdout=subprocess.PIPE).communicate()
    jstr=json.loads(result[0])
    #wait
    time.sleep(30)

# Generate images
tmp = subprocess.Popen(cmdpar, shell=True, stdout=subprocess.PIPE).communicate()
    

