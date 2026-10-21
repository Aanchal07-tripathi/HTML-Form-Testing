
pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                bat 'dir'
            }
        }

        stage('Automated HTML Form Tests') {
            steps {
                bat 'python --version'
                bat 'python -m unittest -v test_form'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
    }
}
