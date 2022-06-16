# Blue Sky Analytics Assignment Documentation

## Objective

### Create a To-Do application with the following features:

1. Create a To-Do with unique UUID, Title and Task.
2. Read all To-Do's.
3. Read To-Do with unique UUID.

## Tech Stack

1. AWS DynamoDB (NoSql database for storing To-Dos).
2. AWS Lambda function (Serverless function to do CRUD operations on DynamoDB - Direct Invocation).
3. AWS Cloudformation - IaC.

## Project Directory Structure

```bash
.
├── cloudformation-template.yaml
├── create-todo.py
├── Makefile
├── README.md
├── read-todo.py
├── Self-Evaluation.pdf
├── template-packaged.yaml
├── test-cases.txt
├── todo-stack-config.yml
└── todo-stack-template.yml

```

The `cloudformation-template.yaml` consists of the yaml configuration to provision the resources required for the application.

It is provisioning the following resources:

1. AWS DynamoDB (for storing To-Do's).
2. Lambda Function - CREATE-TODO (for creating To-Do's).
3. Lambda Function - READ-TODO (for reading To-Do's).

The code for Lambda functions can be found at `create-todo.py` and `read-todo.py`, further these codes are inline embedded into the cloudformation template for better packaging and deployment. 

## Test-Cases

Please refer to `test-cases.txt` for info on test cases

## Packaging

The cloudformation template is packaged using `aws cloudformation package --template-file < name of template file > --s3-bucket < a s3 bucket to store the package > --output-template-file < name of packaged template > ` 

Executing the above command will result in creating a packaged template file -> uploads the packaged template to specified s3 bucker -> creates a local copy of the package.

In this case `template-packaged.yaml` is the packaged cloudformation template.

## Deployment

Please ensure the following before deploying the template:

1. AWS CLI is installed and configured
2. Account configured in AWS CLI should have appropriate permissions on the following AWS resources:

    a. IAM

    b. Cloudformation

    c. Lambda

    d. DynamoDB

    e. S3

To deploy the cloudformation package execute the following:

`aws cloudformation deploy --template-file < name of the generated package template file > --capabilities CAPABILITY_IAM --stack-name {any name you wish to give the stack}`

### Using Make to deploy

The above template can also be deployed using `make`, To deploy using make please ensure the following dependencies are met:

    1. aws
    
    2. jq

    3. shasum

    4. cfn-include (npm install --global cfn-include)

* The file `todo-stack-template.yml` contains cloudformation template to be deployed by makefile.
* Similarly `todo-stack-config.yml` references the above file for template and adds additional configuration of deployment parameters.

To deploy using *make* please follow the below steps:

1. Export environment variable `CONFIG` using `export CONFIG=todo-stack-config.yml`.
2. Run `make create`.