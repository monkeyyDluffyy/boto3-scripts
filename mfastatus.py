import boto3
import csv

iam = boto3.client("iam")

rows=[]

users = iam.list_users()

for user in users["Users"]:

    mfa = iam.list_mfa_devices(UserName=user["UserName"])

    status = True if mfa["MFADevices"] else False

    rows.append([user["UserName"],status])

with open("iam_mfa_status.csv","w",newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["IAMUserName","MFAEnabled"])
    writer.writerows(rows)