pipeline {
    agent { label 'agent-1' } // Specify the agent using a label
    // options {
    //     ansiColor('xterm') // Enable ANSI color in logs
    // }
    enivronment{
        key_user="jayanth"
    }
    stages {
        stage('init') {
            environment{
                user-i="jey"
            }
            steps {
                echo "build for ${user-i} and ${key_user}" // Fixed missing space and quotes
            }
        }
        stage('plan') {
            steps {
                sh 'pwd'
                sh 'ls -lart'
                echo "plan" // Closed the echo statement properly
            }
        }
        stage('apply') {
            steps {
                sh '''
				chmod 777 practice.sh && ./practice.sh  // Ensure the script path is correct and executable
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
