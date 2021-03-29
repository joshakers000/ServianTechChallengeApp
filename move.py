# Author: Josh Akers
# Date: 3/29/21
# Description: A short script that takes in an EC2 endpoint and pushes some files over to the webserver.

import os
import sys
try:
	EC2 = sys.argv[1].strip()
except:
	print()

try:
	os.system("sudo scp -i WebSeverKeyPair.pem -r /dump ec2-user@" + EC2 + ":/home/ec2-user")
	os.system("sudo scp -i WebSeverKeyPair.pem  deploy.sh ec2-user@" +  EC2 + ":/home/ec2-user")
	# Recursive scp has strange functionality when it comes to updated files.
	os.system("sudo scp -i WebSeverKeyPair.pem dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/"
		  "TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/conf.toml  ec2-user@" + EC2 + "
		  ":/home/ec2-user/dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-
		  "70138b5a1badeada55276a8275c6f2b6de47d771/")
	os.system("ssh -i WebSeverKeyPair.pem ec2-user@" + EC2)
except Exception as e:
	print(e)
