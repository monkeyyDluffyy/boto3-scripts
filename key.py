import boto3
import csv

ec2 = boto3.client("ec2")

keys = ec2.describe_key_pairs()["KeyPairs"]

instances = ec2.describe_instances()

used_keys=set()

for r in instances["Reservations"]:
    for i in r["Instances"]:
        if "KeyName" in i:
            used_keys.add(i["KeyName"])

unused=[]

for key in keys:
    if key["KeyName"] not in used_keys:
        unused.append([key["KeyName"]])

with open("unused_keys.csv","w",newline="") as f:

    writer=csv.writer(f)
    writer.writerow(["KeyName"])
    writer.writerows(unused)