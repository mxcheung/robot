#!/bin/bash

sudo yum update -y 

sudo amazon-linux-extras install docker 

sudo yum install docker -y

sudo service docker start 

sudo usermod -a -G docker ec2-user 

sudo yum -y install python3-pip python3-devel nginx git

sudo yum install -y postgresql15

pip install gdown


sudo docker build -t python-docker-app .

sudo docker run --rm python-docker-app
