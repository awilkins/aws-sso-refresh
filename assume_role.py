import boto3

def assume_role(awscreds, config, profile):
    role_to_assume = config[profile]['assumes']

    session = boto3.Session(
      aws_access_key_id=awscreds[profile]['aws_access_key_id'],
      aws_secret_access_key=awscreds[profile]['aws_secret_access_key'],
      aws_session_token=awscreds[profile]['aws_session_token'],
    )
    sts_client = session.client('sts')
    account_id = config[profile]['account_id']

    assumed_role = sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{account_id}:role/{role_to_assume}",
        RoleSessionName=role_to_assume
    )

    if not awscreds.has_section(profile):
        awscreds.add_section(profile)

    awscreds[profile]['aws_access_key_id'] = assumed_role["Credentials"]["AccessKeyId"]
    awscreds[profile]['aws_secret_access_key'] = assumed_role["Credentials"]["SecretAccessKey"]
    awscreds[profile]['aws_session_token'] = assumed_role["Credentials"]["SessionToken"]

    print(f"Assume: {profile} now assuming {role_to_assume} role")
    return awscreds
