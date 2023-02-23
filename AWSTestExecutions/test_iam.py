import boto3

from AWSTestCases.AWS_IAM_Test import aws_iam_check_if_policy_exist, aws_iam_check_if_role_exist
# Create IAM client
iam = boto3.client('iam')

def test_aws_iam_check_if_policy_exist():
    assert aws_iam_check_if_policy_exist(iam) == True


def test_aws_iam_check_if_role_exist():
    assert aws_iam_check_if_role_exist(iam) == True
