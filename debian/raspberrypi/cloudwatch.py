import boto3
from datetime import datetime, timedelta
import json
from pprint import pprint

ec2 = boto3.client("ec2")

response = ec2.describe_instances(
    Filters = [
        {
            "Name": "instance-state-name", "Values": ["running", "stopped"]
        }
    ]
)
# Structure of response:
# response["Reservations"][0]["Instances"][0]["InstanceId"]
names =  [
    instance["InstanceId"] 
    for reservation in response["Reservations"] 
    for instance in reservation["Instances"]
]

def buildDimension(instanceId):
    return {
        'Name': "InstanceId",
        "Value": instanceId
    }

cloudwatch = boto3.client("cloudwatch")
now = datetime.utcnow()
response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=list(map(buildDimension, names)),
    StartTime=now - timedelta(days=10),
    EndTime=now,
    Period=86400,
    Statistics=['Average'],
    Unit='Percent'
)

# pprint(now)
# pprint(now - timedelta(days=10))

pprint(response)
# print(json.dumps(json.loads(response), indent=2))