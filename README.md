# boto3-scripts
Python Advance 
Q1. Write a python program using boto3 to list all available types of ec2 instances in each region. Make sure the instance type won’t repeat in a region. Put it in a csv with these columns. 
region,instance_type 
Q2. Implement transitive switching using multiple aws accounts. Let you have account A and you have to access account C via account B. Write a step by step process of creating roles and other required things. After all the process completes fetch any AWS resources list from account C. 
Q3. Write a python script which will fetch all the regions in which a customer billed for any resources. Or a customer has any resources. 
Q4. AWS Security Best Practices 
Question: 
Your company is looking to improve its AWS security posture by ensuring the following best practices are implemented across the AWS environment: 
1. Ensure IAM roles have least privilege permissions. Identify any roles with overly permissive policies (e.g., AdministratorAccess). 
2. Check that MFA (Multi-Factor Authentication) is enabled for all IAM users and roles with sensitive access. 
3. Ensure that security groups are properly configured to restrict public access to sensitive services (e.g., databases, private EC2 instances). 
4. Identify and report any unused EC2 key pairs in the AWS account. Use Boto3 to: 
● List all IAM roles and analyze their policies to check for overly permissive permissions. 
● Verify that MFA is enabled for IAM users and roles. 
● Check the inbound rules of security groups to detect potential public access (e.g., port 22, 80, 443 open to 0.0.0.0/0). 
● List all EC2 key pairs and report any that are not in use.
Outcome: 
● Create a csv file for each check which lists down all critical threats which need to take action. 
Example : 
● for 1st check (eg. IAM roles have least privilege permissions) 
IAMRoleName, Policy Name (only those which have AdministratorAccess) 
● for 2nd check (eg. IAM User have MFA Enabled or not) 
IAMUserName, MFAEnabled (all users MFA status either True/False) 
● for 3rd check (eg. Security Group have inbound 0.0.0.0/0 allowed for ports 22,80,443) 
SGName, Port, AllowedIP 
Q5. Cost Optimization for an AWS Environment 
Your company is running multiple AWS services (EC2, RDS, Lambda, and S3) in a development account, and you have been asked to perform cost optimization by identifying unused or underutilized resources. 
Create a Python script using Boto3 to: 
1. Identify EC2 instances with low CPU utilization (e.g., below 10% over the past 30 days). 
2. List any RDS instances that are running but have been idle (i.e., no connections for over 7 days). 
3. Identify Lambda functions that have not been invoked in the last 30 days. 4. Check for unused S3 buckets that have no objects or recent access. 
Requirements: 
● Use Boto3’s CloudWatch to monitor EC2 and Lambda utilization. ● Use Boto3’s RDS and S3 APIs to retrieve the state of RDS instances and S3 buckets. 
● Print a summary report listing resources that are candidates for cost-saving actions (e.g., stopping EC2 instances, deleting unused RDS databases).
