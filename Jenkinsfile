pipeline {
    agent { label 'agent-1' } // Specify the agent using a label
    stages {
        stage('init') {
            steps {
                echo "build" // Fixed missing space and quotes
            }
        }
        stage('plan') {
            steps {
                echo "plan" // Closed the echo statement properly
            }
        }
        stage('apply') {
            steps {
                sh '''
		chmod 777 practice.sh
                ./practice.sh  // Ensure the script path is correct and executable
                '''
            }
        }
    }
    post {
        success {
            echo "it will work for success"
        }
        failure {
            echo "it will work for failure"
        }
    }
}
