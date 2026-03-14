import boto3
import csv

iam = boto3.client("iam")

rows=[]

roles = iam.list_roles()

for role in roles["Roles"]:

    policies = iam.list_attached_role_policies(RoleName=role["RoleName"])

    for p in policies["AttachedPolicies"]:

        if "AdministratorAccess" in p["PolicyName"]:

            rows.append([role["RoleName"],p["PolicyName"]])

with open("iam_admin_roles.csv","w",newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["IAMRoleName","PolicyName"])
    writer.writerows(rows)