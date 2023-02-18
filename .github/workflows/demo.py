import boto3


# Create IAM client
iam = boto3.client('iam')

# Get a policy
response = iam.get_policy(
    PolicyArn='arn:aws:iam::aws:policy/AWSLambdaExecute'
)
print(response['Policy'])