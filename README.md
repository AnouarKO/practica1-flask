"GroupId": "sg-02c549557f4c68355"

"GroupId": "sg-02c549557f4c68355",
    "SecurityGroupArn": "arn:aws:ec2:us-east-1:495672285986:security-group/sg-02c549557f4c68355"

AMI ID:    ami-0f3caa1cf4417e51b

"InstanceId": "i-0eb6794d3a157e09e",

Ip pubilica: 13.220.51.135

.
.


aws ec2 run-instances --image-id ami-0f3caa1cf4417e51b --count 1 --instance-type t2.micro --key-name practica1-key --security-group-ids sg-02c549557f4c68355
{
    "ReservationId": "r-0bcf126bb4a1b180e",
    "OwnerId": "495672285986",
    "Groups": [],
    "Instances": [
        {
            "Architecture": "x86_64",
            "BlockDeviceMappings": [],
            "ClientToken": "f83c99f4-7088-45e6-9540-d55880568fd0",
            "EbsOptimized": false,
            "EnaSupport": true,
            "Hypervisor": "xen",
            "NetworkInterfaces": [
                {
                    "Attachment": {
                        "AttachTime": "2026-03-03T08:47:21+00:00",
                        "AttachmentId": "eni-attach-0b6fbe979bc1877b2",
                        "DeleteOnTermination": true,
                        "DeviceIndex": 0,
                        "Status": "attaching",
                        "NetworkCardIndex": 0
                    },
                    "Description": "",
                    "Groups": [
                        {
                            "GroupId": "sg-02c549557f4c68355",
                            "GroupName": "practica1.sg"
                        }
                    ],
                    "Ipv6Addresses": [],
                    "MacAddress": "0a:ff:dd:dc:12:07",
                    "NetworkInterfaceId": "eni-0b889b5b200348116",
                    "OwnerId": "495672285986",
                    "PrivateDnsName": "ip-172-31-29-218.ec2.internal",
                    "PrivateIpAddress": "172.31.29.218",
                    "PrivateIpAddresses": [
                        {
                            "Primary": true,
                            "PrivateDnsName": "ip-172-31-29-218.ec2.internal",
                            "PrivateIpAddress": "172.31.29.218"
                        }
                    ],
                    "SourceDestCheck": true,
                    "Status": "in-use",
                    "SubnetId": "subnet-031120b48810a41d7",
                    "VpcId": "vpc-04f39d03cf713344c",
                    "InterfaceType": "interface",
                    "Operator": {
                        "Managed": false
                    }
                }
            ],
            "RootDeviceName": "/dev/xvda",
            "RootDeviceType": "ebs",
            "SecurityGroups": [
                {
                    "GroupId": "sg-02c549557f4c68355",
                    "GroupName": "practica1.sg"
                }
            ],
            "SourceDestCheck": true,
            "StateReason": {
                "Code": "pending",
                "Message": "pending"
            },
            "VirtualizationType": "hvm",
            "CpuOptions": {
                "CoreCount": 1,
                "ThreadsPerCore": 1
            },
            "CapacityReservationSpecification": {
                "CapacityReservationPreference": "open"
            },
            "MetadataOptions": {
                "State": "pending",
                "HttpTokens": "required",
                "HttpPutResponseHopLimit": 2,
                "HttpEndpoint": "enabled",
                "HttpProtocolIpv6": "disabled",
                "InstanceMetadataTags": "disabled"
            },
            "EnclaveOptions": {
                "Enabled": false
            },
            "BootMode": "uefi-preferred",
            "PrivateDnsNameOptions": {
                "HostnameType": "ip-name",
                "EnableResourceNameDnsARecord": false,
                "EnableResourceNameDnsAAAARecord": false
            },
            "MaintenanceOptions": {
                "AutoRecovery": "default",
                "RebootMigration": "default"
            },
            "CurrentInstanceBootMode": "legacy-bios",
            "Operator": {
                "Managed": false
            },
            "InstanceId": "i-0eb6794d3a157e09e",
            "ImageId": "ami-0f3caa1cf4417e51b",
            "State": {
                "Code": 0,
                "Name": "pending"
            },
            "PrivateDnsName": "ip-172-31-29-218.ec2.internal",
            "PublicDnsName": "",
            "StateTransitionReason": "",
            "KeyName": "practica1-key",
            "AmiLaunchIndex": 0,
            "ProductCodes": [],
            "InstanceType": "t2.micro",
            "LaunchTime": "2026-03-03T08:47:21+00:00",
            "Placement": {
                "AvailabilityZoneId": "use1-az4",
                "GroupName": "",
                "Tenancy": "default",
                "AvailabilityZone": "us-east-1b"
            },
            "Monitoring": {
                "State": "disabled"
            },
            "SubnetId": "subnet-031120b48810a41d7",
            "VpcId": "vpc-04f39d03cf713344c",
            "PrivateIpAddress": "172.31.29.218"
        }
    ]
}