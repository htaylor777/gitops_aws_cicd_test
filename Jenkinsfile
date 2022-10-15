node {
    def app
    agent any
   environment{
        DOCKERHUB_CREDS=credentials('DockerHub')
    }
  
    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("ltartsmusic/gitopsdockerid")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    
     stage('Docker Login') {
         
     sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'
     }
    
    stage('Push image') {  
        
        // @note 'dockerhub' below is my Jenkins credentials keyword to login to DockerHub
         //  docker.withRegistry('https://hub.docker.com/repository/docker', 'DockerHub') {
        //    app.push("${env.BUILD_NUMBER}")
               
           app.push('docker push ltartsmusic/gitopsdockerid:$BUILD_NUMBER')     
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
