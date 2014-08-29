CoreOS and Kubernetes on Amazon EC2
=====================

This how-to guide describes how to set-up a CoreOS cluster running Kubernetes on Amazon EC2.

**The *provision-ec2.sh* script will create :**
- 4 instances (1 *kubernetes-master* & 3 *kubernetes-minion*)
- 2 security groups (*KubernetesMasterSecurityGroup*,*KubernetesMinionSecurityGroup*)


> **This is currently a work in progress, I successfully tested it but use it at your own risks**

### Notes
This documentation is based on the [how-to guide provided by kelseyhightowaer] (https://github.com/kelseyhightower/kubernetes-coreos) and the [Deis provisionning documentation] (https://github.com/deis/deis/tree/master/contrib/ec2)

## Install the [AWS Command Line Interface](https://github.com/aws/aws-cli):
```console
$ pip install awscli
Downloading/unpacking awscli
  Downloading awscli-1.3.6.tar.gz (173kB): 173kB downloaded
  ...
```

## Configure aws-cli
Run `aws configure` to set your AWS credentials:
```console
$ aws configure
AWS Access Key ID [None]: ***************
AWS Secret Access Key [None]: ************************
Default region name [None]: us-west-1
Default output format [None]:
```

## Upload keys
If required, upload a new keypair to AWS. In the following example, the key name is "Kubernetes".
```console
$ export AWS_PUBLIC_KEY = '~/.ssh/id_rsa.pub'
$ export AWS_KEY_NAME = 'Kubernetes'
$ aws ec2 import-key-pair --key-name $AWS_KEY_NAME --public-key-material file://$AWS_PUBLIC_KEY
```

## Configure [custom.json](custom.json)
- Change the "KeyPair" value to "Kubernetes", or to another key you would like to connect with.
- Browse to https://discovery.etcd.io/new and set the token provided into the "DiscoveryURL" value.

## Run the provision script
```console
$ ./provision-ec2.sh
{
    "StackId": "arn:aws:cloudformation:eu-west-1:584689320675:stack/kubernetes/8bc79630-2f80-11e4-bf62-507bb00bdc04"
}
Your Kubernetes cluster has successfully deployed to AWS CloudFormation.
```

Open [Cloudformation](https://console.aws.amazon.com/cloudformation/home) to see the creation status of your Kubernetes Stack


### Useful resources
- [Kubernetes Web Visualizer by Azure](https://github.com/Azure/azure-kubernetes-visualizer).
