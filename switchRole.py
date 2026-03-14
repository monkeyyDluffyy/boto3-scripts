import boto3

sts = boto3.client("sts")

# Assume Role B
role_b = sts.assume_role(
    RoleArn="arn:aws:iam::489157521330:role/roleB",
    RoleSessionName="SessionB"
)

creds_b = role_b['Credentials']

sts_b = boto3.client(
    "sts",
    aws_access_key_id=creds_b["AccessKeyId"],
    aws_secret_access_key=creds_b["SecretAccessKey"],
    aws_session_token=creds_b["SessionToken"]
)

# Assume Role C
role_c = sts_b.assume_role(
    RoleArn="arn:aws:iam::295655331682:role/RoleInAcc3",
    RoleSessionName="SessionC"
)

creds_c = role_c["Credentials"]

ec2 = boto3.client(
    "ec2",
    aws_access_key_id=creds_c["AccessKeyId"],
    aws_secret_access_key=creds_c["SecretAccessKey"],
    aws_session_token=creds_c["SessionToken"]
)

instances = ec2.describe_instances()

print("Instances in Account C:")
print(instances)