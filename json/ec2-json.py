import json

givenJSON = """
{
    "Reservations": [
        {
            "ReservationId": "r-0b9d09c7fbb123456",
            "Instances": [
                {
                    "InstanceId": "i-0123456789abcdef0",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.150",
                    "PublicIpAddress": "52.14.82.122",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-1"
                        },
                        {
                            "Key": "environment",
                            "Value": "dev"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                },
                {
                    "InstanceId": "i-0123456789abcdef1",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.151",
                    "PublicIpAddress": "54.14.82.123",
                    "State": {
                        "Code": 16,
                        "Name": "disabled"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-2"
                        },
                        {
                            "Key": "environment",
                            "Value": "stg"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                },
                {
                    "InstanceId": "i-0123456789abcdef2",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.152",
                    "PublicIpAddress": "52.14.82.124",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-3"
                        },
                        {
                            "Key": "environment",
                            "Value": "dev"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                }
            ]
        }
    ]
}
"""


data = json.loads(givenJSON)


# print(data['Reservations'])



# In One Function, Print the following questions/answers each on a new line:

# 1: The total number of instance ID's in input_json
# 2: The instance ID's where state is running
# 3: The instance ID's tagged with env stg, get the ip address of stg instance

def instance_counter(data):
    number_of_instances = 0
    list_of_instances = []
    for entry in data["Reservations"]:
        for instance in entry["Instances"]:
            list_of_instances.append(instance["InstanceId"])
    number_of_instances = len(list_of_instances)
    return f" The number of Instances is {number_of_instances}"

print(instance_counter(data))



def instance_ids(data):
    instances_ids = []
    for entry in data["Reservations"]:
        for instance in entry["Instances"]:
            if instance["State"]["Name"] == "running":
                instances_ids.append(instance["InstanceId"])
    return instances_ids
print(instance_ids(data))



def instance_env_stg(data):
    instance_ids = []
    for entry in data["Reservations"]:
        for instance in entry["Instances"]:
            for tags in instance["Tags"]:
                if tags["Key"] == "environment" and tags["Value"] == 'stg':
                    instance_ids.append(instance["InstanceId"])
    return instance_ids
print(instance_env_stg(data))                  




