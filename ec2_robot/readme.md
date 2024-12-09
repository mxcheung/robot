ec2_robot


```
sudo yum -y install git
git clone https://github.com/mxcheung/robot.git
cd /home/ec2-user/robot/ec2_robot/
. ./set_up.sh
```

```
sudo docker build -t python-docker-app .
sudo docker run --rm python-docker-app

robot hello.robot
```

```
pip install -r requirements.txt
```
```
sudo yum update -y 

sudo amazon-linux-extras install docker 

sudo yum install docker -y

sudo service docker start 

sudo usermod -a -G docker ec2-user 

sudo yum -y install python3-pip python3-devel nginx git


```



```
t3.small or t3.medium
30 gb
```


## quick start

https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LaunchInstances:

Instance Type:
   - t3.medium

Key pair (login) 
   - MyKeyPair.pem

Network settings
  - Allow SSH traffic from
  - Allow HTTPS traffic from the internet
  - Allow HTTP traffic from the internet

Configure storage
  - 30gb

```
ssh -i "MyKeyPair.pem" ec2-user@ec2-54-172-100-112.compute-1.amazonaws.com
```

```
project/
│
├── Dockerfile
├── app.py              # Main execution script
├── test.robot          # Robot Framework test suite
├── test.py             # Supporting Python file for custom Robot Framework libraries

```

## reference
https://www.geeksforgeeks.org/how-to-install-docker-on-aws-ec2/
https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker/
https://github.com/robotframework/BeginnersGuide

