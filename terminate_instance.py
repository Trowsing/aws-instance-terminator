#!/usr/bin/python3

import sys
import argparse
from pprint import pprint
import boto3


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="terminate-instance", description="Terminate a given AWS instance"
    )
    parser.add_argument("instance_name", type=str, help="Instance name tag")
    args = parser.parse_args()
    return args


def get_instance_id(instance_name: str) -> str:
    ec2 = boto3.client("ec2")
    instance = ec2.describe_instances(
        Filters=[
            {"Name": "tag:Name", "Values": [instance_name]},
            {"Name": "instance-state-name", "Values": ["running"]},
        ]
    )
    try:
        instance_id = instance["Reservations"][0]["Instances"][0]["InstanceId"]
        return instance_id
    except IndexError:
        pprint("Invalid instance name!")
        sys.exit()


def prompt_authorization():
    confirmation = input(
        f"Confirm termination of instance {INSTANCE_NAME} with ID: {INSTANCE_ID}? (y/n): "
    )
    if confirmation == "y":
        terminate_instance(INSTANCE_ID)
    elif confirmation == "n":
        sys.exit()
    else:
        pprint("Invalid input!")
        prompt_authorization()


def terminate_instance(instance_id: str):
    ec2 = boto3.client("ec2")
    response = ec2.terminate_instances(InstanceIds=[instance_id])
    pprint(response)


if __name__ == "__main__":
    ARGS = get_args()
    INSTANCE_NAME = ARGS.instance_name
    INSTANCE_ID = get_instance_id(INSTANCE_NAME)
    prompt_authorization()
