# Infrastructure-Lambda-Samples
Sample Project that should act as a skeleton and starting point for new microservices.

# Technology Stack
## [Jenkins Declarative Pipeline](https://jenkins.io/doc/book/pipeline/syntax/)
Jenkinsfile is used for PR builds

Jenkinsfile-cd is used for continuous delivery deployments on merge to master.

Both contain a parallel testing step that runs Linting, Security checks and Unit tests. 

The Jenkinsfile-cd contains additional steps to deploy the application stack and to do a canary deployment to production.

## [AWS SAM (Serverless Application Model)](https://github.com/awslabs/serverless-application-model)
Application structure declared in template.yaml

sam packages this and converts it to a full cloudformation stack, as well as deploys it.

We are creating a staging and prod environment in the example. Could easily be extended to others.

The format being used is a single function for the whole app. The idea being a router would be written in the handler to get to the specific functions needed rather than having and endless amount of separate functions for the same stack. This could be changed and would require adding more function statements as well as changing the API GW method to be more specific and not rely on {proxy+}, This would require a new method for each route to direct it to the specific function.

## [Lambda](https://aws.amazon.com/documentation/lambda/)
Lambda is used along with python3.6 runtime. 

## [AWS Lambda Deployer](https://github.com/aws-samples/aws-lambda-deploy)
Uses a combination of lambda jobs and AWS Stepfunctions to do a canary deployment by adjusting the weight of a lambda alias to version, allowing for a slow rollout and monitoring for execution errors in cloudwatch.

The workflow is checks weights, increases them by specific amount after a specified interval of time, then checks for any execution errors and repeats till weight is 100% on the new version.

## [Python3.6](https://docs.python.org/3.6/)
Python3.6 for the sample project as well as some of the steps to achieve deployment. 

pip for package installs

virtualenv for environment/package isolation

## [Pytest](https://pytest.org/)
Pytest + pytest-cov packages are used to test and provide coverage reports.

Pytest is set to fail builds without coverage of 100%

## [Safety](https://pyup.io/safety/)
Safety is used to check the project's requirement's file for known vulnerabilities.

## [Flake8](http://flake8.pycqa.org/en/latest/)
Flake8 is used for Style guide (PEP8) enforcement. We are ignoring line too long errors as the length constraint is antiquated
