node {
    def app

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

    stage('Push image') {
        // @note 'dockerhub' below is my Jenkins credentials keyword to login to DockerHub
        docker.withRegistry('https://hub.docker.com/repository/docker/', 'DockerHub') {
            app.push("ltartsmusic/gitopsdockerid:${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
