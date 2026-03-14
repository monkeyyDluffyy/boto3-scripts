import boto3
import csv

ec2 = boto3.client("ec2")

rows=[]

groups = ec2.describe_security_groups()

for sg in groups["SecurityGroups"]:

    for perm in sg["IpPermissions"]:

        port = perm.get("FromPort")

        for ip in perm.get("IpRanges",[]):

            if ip["CidrIp"] == "0.0.0.0/0" and port in [22,80,443]:

                rows.append([sg["GroupName"],port,"0.0.0.0/0"])


with open("sg_public_access.csv","w",newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["SGName","Port","AllowedIP"])
    writer.writerows(rows)