#!/usr/bin/python

# Utility for listing hosts within ec2.
# Created: 10/2/16

import argparse
import boto3
import botocore

parser = argparse.ArgumentParser(description='List hosts from ec2.  Without any arguments it will attempt to list all '
                                             'running ec2 instances in the default profile and region that has been '
                                             'configured with AWS CLI.')
parser.add_argument('--region', default=None, help='The AWS region in which to look for ec2 instances (e.g. us-west-2')
parser.add_argument('--profile', default=None, help='The AWS profile to be used for this session.')
parser.add_argument('--state', choices=['pending', 'running', 'shutting-down', 'terminated','stopped', 'stopping',
                                        'all'], default='running', help='The state of instances to be listed.')
parser.add_argument('--group', default=None, help='The name of the security group to filter by.')
parser.add_argument('--public', action='store_const', const=True, help='List only instances with public IPs instead of all.')

args = parser.parse_args()

try:
    session = boto3.Session(region_name=args.region, profile_name=args.profile)
    ec2 = session.resource('ec2')

    filters = []
    if args.state == 'all':
        filters.append({'Name': 'instance-state-name', 'Values': ['running']})
    else:
        filters.append({'Name': 'instance-state-name', 'Values': [args.state]})
    if args.group is not None:
        filters.append({'Name': 'instance.group-name', 'Values': [args.group]})

    instances = ec2.instances.filter(Filters=filters)
    for instance in instances:
        if args.public is None:
            print '%s' % instance.private_ip_address
        elif instance.public_ip_address is not None:
            print '%s' % instance.public_ip_address
except botocore.exceptions.NoRegionError:
    print 'Region not set.  Either run "aws configure" and set it there or use the --region argument.'


