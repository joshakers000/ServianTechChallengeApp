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
