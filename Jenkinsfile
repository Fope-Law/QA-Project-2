// declarative pipeline
pipeline {
    agent any;
        args "--user root --privileged";
            stages{
                stage('Compose Docker images'){
                            steps{
                                sh "docker-compose build"
                            }
                        }
                        stage('Deploy Docker stack'){
                            steps{
                                sh "docker stack deploy --compose-file docker-compose.yaml stack"
                        }
                    }
                }
            }