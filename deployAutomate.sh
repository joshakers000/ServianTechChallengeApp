#!bin/bash
cd dump/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771/TechChallengeApp-70138b5a1badeada55276a8275c6f2b6de47d771
sudo bash build.sh
cd dist
sudo ./TechChallengeApp updatedb -s
sudo ./TechChallengeApp serve