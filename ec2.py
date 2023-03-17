import boto3

# Set the AWS region
region = 'us-east-1'

# Set the instance details
instance_type = 't2.micro'
image_id = 'ami-0c94855ba95c71c99'
key_name = 'my-key-pair'
security_group_ids = ['sg-1234567890']

# Create the EC2 client
ec2 = boto3.client('ec2', region_name=region)

# Create the instance
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']

# Wait for the instance to be running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Print the instance ID and IP address
instance = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
print(f"Instance created with ID: {instance_id}")
print(f"Public IP address: {instance['PublicIpAddress']}")
