## What this does?
This repo along with https://github.com/htaylor777/kubernetesmanifest creates a Jenkins pipeline with GitOps to deploy code into a Kubernetes cluster. CI part is done via Jenkins and CD part via ArgoCD (GitOps).

## Jenkins installation
Jenkins is installed on EC2. Follow the instructions on https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/ . You can skip "Configure a Cloud" part for this demo. Please note some commands from this link might give errors, below are the workarounds:

2. Install Docker on the EC2 after Jenkins is installed: instructions on https://serverfault.com/questions/836198/how-to-install-docker-on-aws-ec2-instance-with-ami-ce-ee-update

3. Run `sudo chmod 666 /var/run/docker.sock` on the EC2 after Docker is installed.

4. Install Git on the EC2 by running `sudo yum install git`

### Jenkins plugins installed:

- Amazon EC2 plugin (No need to set up Configure Cloud after)
- Docker plugin  
- Docker Pipeline
- GitHub Integration Plugin
- Parameterized trigger Plugin

## ArgoCD installation 

Install ArgoCD in Kubernetes cluster following this link - https://argo-cd.readthedocs.io/en/stable/getting_started/

