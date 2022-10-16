pipeline {
    agent any
    environment{
        DOCKERHUB_CREDS=credentials('DockerHub')
    }
    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
                sh 'ls *'
            }
        }
        stage('Build Image') {
            steps {
                //sh 'docker build -t raj80dockerid/jenkinstest ./pushdockerimage/' (this will use the tag latest)
		sh 'docker build -t ltartsmusic/gitopstesting:$BUILD_NUMBER ./gitops_aws_cicd_test/'  
            }
        }
        stage('Docker Login') {
            steps {
                //sh 'docker login -u $DOCKERHUB_CREDS_USR -p $DOCKERHUB_CREDS_PSW' (this will leave the password visible)
                sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'
                }
            }
        stage('Docker Push') {
            steps {
		//sh 'docker push raj80dockerid/jenkinstest' (this will use the tag latest)    
            
                sh 'docker push ltartsmusic/gitopstesting:$BUILD_NUMBER'
                }
            }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
}
