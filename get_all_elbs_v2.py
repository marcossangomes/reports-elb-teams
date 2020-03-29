import boto3

client = boto3.client('elbv2', region_name='us-east-1')

def get_all_elbs_v2():

    response = client.describe_load_balancers()

    elbs = []

    for name in response['LoadBalancers']:
        elbs.append(name['LoadBalancerArn'])


    return elbs;
