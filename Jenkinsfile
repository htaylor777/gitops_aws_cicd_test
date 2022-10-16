node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       //app = docker.build("gitops/testing")
        app = "sh 'docker build -t ltartsmusic/gitopsTest:$BUILD_NUMBER'" 
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }
    

    stage('Push image') {
        // @note 'dockerhub' below is my Jenkins credentials keyword to login to DockerHub
       docker.withRegistry('https://hub.docker.com/repositories', 'DockerHub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
