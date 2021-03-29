# Author: Josh Akers
# Date: 03/29/21
# Description: This starts the build process by creating a key pair and creating the CloudFormation stack.

import os
import sys

# 1. Make Keypair and change perms
try:
	os.system("sudo aws ec2 create-key-pair --key-name WebServerKP198 --query 'KeyMaterial' --output text > WebSeverKeyPair.pem")
	os.system("sudo chmod 400 WebSeverKeyPair.pem")
except Exception as e:
	print(e)
	sys.exit(1)
	
# 2. Run CloudFormation script
os.system("sudo aws cloudformation create-stack --stack-name WebServerDeployment --template-body file://techchallenge_CF.yaml --parameters file://stackparams.json --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_NAMED_IAM")
print("Reminder!  Please update the conf.toml file.")
