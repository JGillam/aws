# AWS Scripts
This repo contains scripts designed to simplify various AWS-related tasks.
These scripts leverage the boto3 python module.
The easiest way to make sure boto3 will work is to install with AWS CLI and run `aws configure`.
## Scripts
### aws-list-hosts.py
This script is for listing EC2 hosts (by ip address).  It supports a small number of useful filters through script
arguments.  E.g.:
```
> aws-list-hosts.py --region us-west-1
172.16.0.5
172.16.0.122
172.16.0.131
172.16.1.123
```