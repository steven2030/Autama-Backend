import json
import subprocess
import time


def generate_image(number_images, start_image):

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
    tmp = subprocess.Popen(f'aws ssm send-command --document-name "AWS-RunShellScript" --document-version "1" --targets \'[{{"Key":"InstanceIds","Values":["i-01d6de0c8312b250c"]}}]\' --parameters \'{{"commands":["runuser -l ubuntu -c \'"\'"\'python3.6 /home/ubuntu/stylegan/pretrained_example.py {start_image} {number_images}\'"\'"\'"],"workingDirectory":[""],"executionTimeout":["3600"]}}\' --timeout-seconds 600 --max-concurrency "50" --max-errors "0" --region us-west-2', shell=True, stdout=subprocess.PIPE).communicate()
    

