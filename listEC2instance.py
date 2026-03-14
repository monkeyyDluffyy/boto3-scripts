import boto3
import csv

ec2 = boto3.client("ec2")

regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]

rows = []

for region in regions:

    regional_ec2 = boto3.client("ec2", region_name=region)

    paginator = regional_ec2.get_paginator('describe_instance_types')

    instance_set = set()

    for page in paginator.paginate():
        for instance in page["InstanceTypes"]:
            instance_set.add(instance["InstanceType"])

    for instance in instance_set:
        rows.append([region, instance])


with open("ec2_instance_types.csv","w",newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["region","instance_type"])
    writer.writerows(rows)

print("CSV created: ec2_instance_types.csv")