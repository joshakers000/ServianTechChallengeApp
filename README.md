# ServianTechChallengeApp

This is my take on the ServianTechChallengeApp.

# Architecture
- 1 VPC, 2 public subnets (EC2), 1 private subnet (RDS)
- Network segmentation: Only access private subnet from inside VPC
- High Availability: Not yet implemented, subnets are there to deploy.
- Secrets: Used parameters with password generator.  Parameter store not used.
- - Security issue with this is that the configuration files are still sitting on the Webservers.  
- WAF: Not implemented.  Not free tier.
- Disaster Recovery: Parameter for MultiAZ option available (not tested - should work though).
- Security Groups: Proper rules in place for basic filtering.
- NACLs - set to allow all for simplicity.

# Dependencies
- Python3
- - paramiko should be included in the install
- Deployed via ubuntu-20.04.2.0-desktop-amd64
- aws cli with configured role
- - specific role perms required unknown
- - Just run with Admin privs

# Deployment
- ```sudo python3 build.py```
- Trust the finger print when prompted -> occurs after stack creation.
- - ```yes```
- Wait until you are ssh'd into EC2
- - ```sudo bash deployAutomate.sh```

# Access Application
- Visit the EC2 endpoint or IP address.
- - Can be found in the terminal when accepting the fingerprint.


# Intended Changes
- Implement proper HA architecture.
- Clean up python.  It's a bit messy.
