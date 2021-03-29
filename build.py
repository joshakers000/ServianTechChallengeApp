# Author: Josh Akers
# Date: 03/29/21
# Description: This starts the build process by creating a key pair and creating the CloudFormation stack.

import os
# 1. Make Keypair and change perms
try:
	os.system("sudo aws ec2 create-key-pair --key-name WebServerKP198 --query 'KeyMaterial' --output text > WebSeverKeyPair.pem")
	os.system("sudo chmod 400 WebSeverKeyPair.pem")
except Exception as e:
	print(e)
# 2. Run CloudFormation script
os.system("sudo aws cloudformation create-stack --stack-name WebServerDeployment --template-body file://techchallenge_CF.yaml --parameters file://stackparams.json --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_NAMED_IAM")
print("Please obtain the dns endpoint for the postgres instance and the EC2 instance.  Stack completion will take approximately eight minutes.")
print("Reminder!  Please update the conf.toml file.")
