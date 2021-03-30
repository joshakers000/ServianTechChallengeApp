# Author: Josh Akers
# Date: 03/29/21 -> Updated: 03/31/21
# Description: This nearly takes care of all automation for building and deploying the web application.

import os
import time
import json
import random
import string
from paramiko import SSHClient, AutoAddPolicy

stackStatus = ""
minutesLapsed = 0

def get_random_password(length):
    # Return random password from upper/lower/digits
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

password = get_random_password(random.randint(20,30))


# 1. Make Keypair and change perms
try:
	os.system("sudo aws ec2 create-key-pair --key-name WebServerKP777 --query 'KeyMaterial' --output text > WebSeverKeyPair.pem")
	os.system("sudo chmod 400 WebSeverKeyPair.pem")
except Exception as e:
	print(e)

##########
#### Get my ip and update parameterFile
##########

import urllib.request

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')




my_file = open("stackparams.json")
lines = my_file.readlines()
my_file.close()

lines[23] = '        "ParameterValue": "' + external_ip.strip() + '/32"\n'
lines[39] = '        "ParameterValue": "' + password + '"\n'

newFileContent = "".join(lines)
my_file = open("stackparams.json", "w")
my_file.write(newFileContent)
my_file.close()


# 2. Run CloudFormation script
os.system("sudo aws cloudformation create-stack --stack-name WebServerDeployment2 --template-body file://techchallenge_CF.yaml --parameters file://stackparams.json --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_NAMED_IAM")





while stackStatus != "CREATE_COMPLETE":
	print("Stack creation in progress.  Minutes lapsed: " + str(minutesLapsed))
	time.sleep(60)
	#while stackStatus != "CREATE_COMPLETE"
	stack = json.loads((os.popen("sudo aws cloudformation describe-stacks --stack-name WebServerDeployment2 --region us-east-1").read()))
	#print(stack)
	stackStatus = stack["Stacks"][0]["StackStatus"]
	minutesLapsed = minutesLapsed + 1

##########
#### Stack completed
##########

Outputs = stack["Stacks"][0]["Outputs"]

RdsEndpoint = Outputs[0]["OutputValue"]
EC2Endpoint = Outputs[1]["OutputValue"]

print(RdsEndpoint, EC2Endpoint)

my_file = open("dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/conf.toml")
lines = my_file.readlines()
my_file.close()

lines[4] = '"DbHost" = "' + RdsEndpoint +'"\n'
lines[1] = '"DbPassword" = "' + password + '"\n'

newFileContent = "".join(lines)
my_file = open("dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/conf.toml", "w")
my_file.write(newFileContent)
my_file.close()

##########
#### scp files over
##########

try:
	os.system("sudo scp -i WebSeverKeyPair.pem -r /dump ec2-user@" + EC2Endpoint + ":/home/ec2-user")
	os.system("sudo scp -i WebSeverKeyPair.pem  deployAutomate.sh ec2-user@" +  EC2Endpoint + ":/home/ec2-user")
	# Recursive scp has strange functionality when it comes to updated files.
	os.system("sudo scp -i WebSeverKeyPair.pem dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/"\
		  + "TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/conf.toml  ec2-user@"\
                  + EC2Endpoint\
		  + ":/home/ec2-user/dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-"\
		  + "70138b5a1badeada55276a8275c6f2b6de47d771/")
	#os.system("ssh -i WebSeverKeyPair.pem ec2-user@" + EC2Endpoint)
except Exception as e:
	print(e)


##########
#### ssh and deploy
##########

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(EC2Endpoint, username="ec2-user", key_filename="WebSeverKeyPair.pem")
stdin, stdout, stderr = client.exec_command('sudo yum -y install go')
stdin, stdout, stderr = client.exec_command('mkdir go')
stdin, stdout, stderr = client.exec_command('mkdir go/bin')
stdin, stdout, stderr = client.exec_command('curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh')

print("Please wait for packages to install.")
time.sleep(85)

os.system("ssh -i WebSeverKeyPair.pem ec2-user@" + EC2Endpoint)
#stdin, stdout, stderr = client.exec_command('sudo bash deployAutomate.sh')

#stdin, stdout, stderr = client.exec_command('cd dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771')
#----------------
#stdin, stdout, stderr = client.exec_command('sudo bash build.sh')
#stdin, stdout, stderr = client.exec_command('cd dist')
#stdin, stdout, stderr = client.exec_command('sudo ./TechChallengeApp updatedb -s')
#stdin, stdout, stderr = client.exec_command('sudo ./TechChallengeApp serve')