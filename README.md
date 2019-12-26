# AWS Instance Terminator

Simple CLI boto3 wrapper to terminate your EC2 instances by name tag.

## Getting Started

### Prerequisites

The `boto3` library is required to run the script.

### How to use it

This script takes one positional argument as the instance name and prompts for a `terminate` confirmation.

You can make it executable:

```bash
chmod -x terminate-instance.py

./terminate_instance.py my-instance-name-tag
```

Or call it directly:

```bash
python3 terminate-instance.py my-instance-name-tag
```

The `help` argument also contains the basic usage instructions:

```bash
python3 terminate-instance.py --help
```