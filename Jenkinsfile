pipeline {
    agent { label 'agent-1' } // Specify the agent using a label
    // options {
    //     ansiColor('xterm') // Enable ANSI color in logs
    // }


    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }
    environment{
        key_user="jayanth"
    }
    stages {
        stage('init') {
            environment{
                useri="jey"
            }
            steps {
                echo "build for ${params.PERSON} and ${key_user}" // Fixed missing space and quotes
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
            when{
                branch 'master'
            }
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
