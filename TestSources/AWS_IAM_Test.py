import boto3


# Create IAM client
iam = boto3.client('iam')

def aws_iam_check_if_policy_exist():
    try:
        # Get a policy
        response = iam.get_policy(
            PolicyArn='arn:aws:iam::aws:policy/AWSLambdaExecute'
        )
        print(response['Policy'])
    except Exception as e:
        print("error occured while invoking aws_iam_check_if_policy_exist and error is {}".format(e))
        return False
    else:
         return True

def aws_iam_check_if_role_exist():
    try:
        # Get a policy
        response = iam.get_role(
            RoleName='github-oidc-role'
        )
        print(response['Role'])
    except Exception as e:
        print("error occured while aws_iam_check_if_role_exist and error is {}".format(e))
        return False
    else:
         return True