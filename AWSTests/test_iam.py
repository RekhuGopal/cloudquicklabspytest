from TestSources.AWS_IAM_Test import aws_iam_check_if_policy_exist, aws_iam_check_if_role_exist

def test_aws_iam_check_if_policy_exist():
    assert aws_iam_check_if_policy_exist() == True


def test_aws_iam_check_if_role_exist():
    assert aws_iam_check_if_role_exist() == True
