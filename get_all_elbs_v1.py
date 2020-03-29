import boto3

client = boto3.client('elb', region_name='us-east-1')

def get_all_elbs_v1():

    response = client.describe_load_balancers()

    elbs = []

    for name in response['LoadBalancerDescriptions']:
        elbs.append(name['LoadBalancerName'])

    return elbs
