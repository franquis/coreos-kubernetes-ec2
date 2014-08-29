#!/usr/bin/env python
import json
import os

template = json.load(open("template-kubernetes.json",'r'))

with open('./cloud-init/master.yaml','r') as f:
  master = f.readlines()

with open('./cloud-init/minion.yaml','r') as f:
  minion = f.readlines()

template['Resources']['KubernetesMasterServerLaunchConfig']['Properties']['UserData']['Fn::Base64']['Fn::Join'] = [ '', master ]
template['Resources']['KubernetesMinionServerLaunchConfig']['Properties']['UserData']['Fn::Base64']['Fn::Join'] = [ '', minion ]
template['Parameters']['ClusterSize']['Default'] = str(os.getenv('KUBERNETES_MINION_INSTANCES', 3))

"""
VPC_ID = os.getenv('VPC_ID', None)
VPC_SUBNETS = os.getenv('VPC_SUBNETS', None)
VPC_ZONES = os.getenv('VPC_ZONES', None)

if VPC_ID and VPC_SUBNETS and VPC_ZONES and len(VPC_SUBNETS.split(',')) == len(VPC_ZONES.split(',')):
  # skip VPC, subnet, route, and internet gateway creation
  del template['Resources']['VPC']
  del template['Resources']['Subnet1']
  del template['Resources']['Subnet2']
  del template['Resources']['Subnet1RouteTableAssociation']
  del template['Resources']['Subnet2RouteTableAssociation']
  del template['Resources']['InternetGateway']
  del template['Resources']['GatewayToInternet']
  del template['Resources']['PublicRouteTable']
  del template['Resources']['PublicRoute']
  del template['Resources']['CoreOSServerLaunchConfig']['DependsOn']
  del template['Resources']['DeisWebELB']['DependsOn']

  # update VpcId fields
  template['Resources']['DeisWebELBSecurityGroup']['Properties']['VpcId'] = VPC_ID
  template['Resources']['VPCSecurityGroup']['Properties']['VpcId'] = VPC_ID

  # update subnets and zones
  template['Resources']['CoreOSServerAutoScale']['Properties']['AvailabilityZones'] = VPC_ZONES.split(',')
  template['Resources']['CoreOSServerAutoScale']['Properties']['VPCZoneIdentifier'] = VPC_SUBNETS.split(',')
  template['Resources']['DeisWebELB']['Properties']['Subnets'] = VPC_SUBNETS.split(',')
"""
print json.dumps(template)