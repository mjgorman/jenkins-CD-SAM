pipeline {
    agent none
    stages {
        stage('Prepare') {
            steps {
                node('default') {
                    // Checkout the branch that caused this build to trigger
                    checkout scm
                    stash name: 'source', useDefaultExcludes: false, includes: '**,**/.*', allowEmpty: true
                    cleanWs externalDelete: 'rm -fr %s'
                }
            }
        }
        stage('Tests') {
            parallel {
                stage('Linting') {
                    steps {
                        node('small') {
                            unstash 'source'
                            sh '''
                                  virtualenv venv
                                  source venv/bin/activate
                                  pip install flake8
                                  flake8 --ignore=E501 hello_world/
                            '''
                            cleanWs externalDelete: 'rm -fr %s'
                        }
                    }
                }
                stage('Security') {
                    steps {
                        node('small') {
                            unstash 'source'
                            sh '''
                                  virtualenv venv
                                  source venv/bin/activate
                                  pip install safety
                                  safety check -r requirements.txt
                            '''
                            cleanWs externalDelete: 'rm -fr %s'
                        }
                    }
                }
                stage('Unit Tests') {
                    steps {
                        node('small') {
                            unstash 'source'
                            sh '''
                                  virtualenv venv
                                  source venv/bin/activate
                                  pip install pytest pytest-cov
                                  pip install -r requirements.txt
                            '''
                            sh '''
                                  source venv/bin/activate
                                  pytest --cov hello_world --cov-report html --cov-fail-under 100 tests/ -v
                            '''                                      
                            stash includes: '**/htmlcov/**', name: 'coverage'
                            cleanWs externalDelete: 'rm -fr %s'
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            node('default') {
                unstash 'coverage'
                publishHTML([allowMissing: true,
                             alwaysLinkToLastBuild: true,
                             keepAll: true,
                             reportDir: 'htmlcov',
                             reportFiles: 'index.html',
                             reportName: 'Coverage Report',
                             reportTitles: ''])
            }
        }
    }
}
