import boto3
from datetime import datetime, timedelta

# Clients
ec2 = boto3.client("ec2")
cloudwatch = boto3.client("cloudwatch")
rds = boto3.client("rds")
lambda_client = boto3.client("lambda")
s3 = boto3.client("s3")

low_cpu_instances = []
idle_rds_instances = []
unused_lambda_functions = []
empty_buckets = []


# -------------------------------
# 1. EC2 Low CPU Utilization
# -------------------------------
print("Checking EC2 CPU utilization...")

instances = ec2.describe_instances()

for reservation in instances["Reservations"]:
    for instance in reservation["Instances"]:

        instance_id = instance["InstanceId"]

        metrics = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
            StartTime=datetime.utcnow() - timedelta(days=30),
            EndTime=datetime.utcnow(),
            Period=86400,
            Statistics=["Average"]
        )

        if metrics["Datapoints"]:

            avg_cpu = sum(d["Average"] for d in metrics["Datapoints"]) / len(metrics["Datapoints"])

            if avg_cpu < 10:
                low_cpu_instances.append(instance_id)


# -------------------------------
# 2. Idle RDS Instances
# -------------------------------
print("Checking idle RDS databases...")

dbs = rds.describe_db_instances()

for db in dbs["DBInstances"]:

    db_id = db["DBInstanceIdentifier"]

    metrics = cloudwatch.get_metric_statistics(
        Namespace="AWS/RDS",
        MetricName="DatabaseConnections",
        Dimensions=[{"Name": "DBInstanceIdentifier", "Value": db_id}],
        StartTime=datetime.utcnow() - timedelta(days=7),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=["Average"]
    )

    if metrics["Datapoints"]:
        avg_conn = sum(d["Average"] for d in metrics["Datapoints"]) / len(metrics["Datapoints"])

        if avg_conn == 0:
            idle_rds_instances.append(db_id)


# -------------------------------
# 3. Lambda Not Invoked in 30 Days
# -------------------------------
print("Checking unused Lambda functions...")

functions = lambda_client.list_functions()

for func in functions["Functions"]:

    name = func["FunctionName"]

    metrics = cloudwatch.get_metric_statistics(
        Namespace="AWS/Lambda",
        MetricName="Invocations",
        Dimensions=[{"Name": "FunctionName", "Value": name}],
        StartTime=datetime.utcnow() - timedelta(days=30),
        EndTime=datetime.utcnow(),
        Period=86400,
        Statistics=["Sum"]
    )

    if metrics["Datapoints"]:
        total = sum(d["Sum"] for d in metrics["Datapoints"])

        if total == 0:
            unused_lambda_functions.append(name)
    else:
        unused_lambda_functions.append(name)


# -------------------------------
# 4. Empty S3 Buckets
# -------------------------------
print("Checking empty S3 buckets...")

buckets = s3.list_buckets()

for bucket in buckets["Buckets"]:

    bucket_name = bucket["Name"]

    objects = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" not in objects:
        empty_buckets.append(bucket_name)


# -------------------------------
# Final Summary Report
# -------------------------------
print("\n===== COST OPTIMIZATION REPORT =====\n")

print("EC2 Instances with Low CPU (<10%):")
for i in low_cpu_instances:
    print(i)

print("\nIdle RDS Instances (no connections 7 days):")
for db in idle_rds_instances:
    print(db)

print("\nUnused Lambda Functions (no invocations 30 days):")
for f in unused_lambda_functions:
    print(f)

print("\nEmpty S3 Buckets:")
for b in empty_buckets:
    print(b)

print("\n===== END REPORT =====")