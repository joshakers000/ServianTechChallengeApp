#!bin/bash
sudo yum -y install go
cd ../
mkdir root
mkdir root/go
mkdir root/go/bin
cd ec2-user
mkdir go
mkdir go/bin
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
cd dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771
sudo bash build.sh
cd dist
sudo ./TechChallengeApp updatedb -s
sudo ./TechChallengeApp serve
