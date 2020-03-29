import boto3

client = boto3.client('elb', region_name='us-east-1')

def check_tags_elbs_v1(elb):

    try:

        response = client.describe_tags(
            LoadBalancerNames=[
                elb,
            ]
        )

        tags = str(response['TagDescriptions'][0]['Tags'])

        if 'Team' in tags and 'Team' != '':
            return True
        else:
            return False
    except Exception as ex:
        print(ex)

