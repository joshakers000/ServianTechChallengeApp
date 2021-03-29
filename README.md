# ServianTechChallengeApp

This is my take on the ServianTechChallengeApp.

# Architecture
- 1 VPC, 2 public subnets (EC2), 1 private subnet (RDS)
- Proper network segmentation, only access private subnet from inside VPC
- High Availability: Not yet implemented, subnets are there to deploy.
- Secrets: Went against this method to simply implementation by allowing the user to set their own PW when running the script.
- - Security issue with this is that the configuration files are still sitting on the Webservers.  
- WAF: Not implemented.  It's easy enough to setup but that costs money.
- Disaster Recovery: Parameter for MultiAZ option available (not tested - should work though).
- Security Groups: Proper rules in place for basic filtering.
- NACLs - set to allow all for simplicity.

# Dependencies
- Python3
- Deployed via ubuntu-20.04.2.0-desktop-amd64
- aws cli with configured role
- - specific role perms required unknown
- - Just run with Admin privs

# Instructions!
- Please follow closely.
- Clone reposity.
- Edit stackparams.json for customization.
- - Change the DBPw and PersonalSSHCIDR ParameterValues.
- - Each parameter shouuld be self explanatory.
- ```sudo python3 build.py```
- This will create an ssh key and create the stack.  
- Stack creation will take approximately eight minutes to complete.
- Obtain your RDS endpoint and EC2 endpoint.
- Update conf.toml w/ Database password and RDS endpoint.
- - conf.toml is found in dump/Te.../Te...
- ```sudo python3 move.py <EC2-Endpoint>```
- Once this finishes you should now be ssh'd into your web server.
- ```sudo bash deploy.sh```
- This will install all the dependencies and run the server.

# Access Application
- Visit the EC2-Endpoint from earlier and you should be good to go!
- Congrats you have just deployed my rarely available webserver!
