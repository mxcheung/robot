ec2_robot


https://www.geeksforgeeks.org/how-to-install-docker-on-aws-ec2/


```
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl status docker
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
