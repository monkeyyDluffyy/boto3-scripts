import boto3

ec2 = boto3.client("ec2")

regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]

active_regions = []

for region in regions:

    client = boto3.client("ec2",region_name=region)

    instances = client.describe_instances()

    if instances["Reservations"]:
        active_regions.append(region)

print("Regions with resources:")
for r in active_regions:
    print(r)