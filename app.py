from get_all_elbs_v1 import get_all_elbs_v1
from get_all_elbs_v2 import get_all_elbs_v2
from check_tags_elbs_v1 import check_tags_elbs_v1
from check_tags_elbs_v2 import check_tags_elbs_v2
from send_msg_slack import send_msg_slack

arquivo = open('lbs-reports-tags', 'w')

elb_without_tags = 0
elb_with_tags = 0

elbs_v1 = get_all_elbs_v1();

elbs_v2 = get_all_elbs_v2();

elbs_msg_v1 = []

elbs_msg_v2 = []


for elbs_v1_aux in elbs_v1:
    try:
        if check_tags_elbs_v1(elbs_v1_aux) == False:
            arquivo.write('Loadbalancer has no tag: ' + elbs_v1_aux + '\n')
            elb_without_tags += 1
            print(elbs_msg_v1)
        else:
            elb_with_tags += 1
    except Exception as err:
        elb_without_tags += 1
        arquivo.write(str(err))

for elbs_v2_aux in elbs_v2:
    try:
        if check_tags_elbs_v2(elbs_v2_aux) == False:
            arquivo.write('Loadbalancer has no tag: ' + elbs_v2_aux + '\n')
            elb_without_tags += 1
            print(elbs_msg_v2)
        else:
            elb_with_tags += 1
    except Exception as err:
        elb_without_tags += 1
        arquivo.write(err)

arquivo.write('--------------------------------------------------------------------\n')
arquivo.write('Load balancers without tags: ' + str(elb_without_tags))
arquivo.write('\n')
arquivo.write('\nLoad Balances with tags: ' + str(elb_with_tags))
arquivo.write('\n')
arquivo.close()

send_msg_slack(elb_without_tags, elb_with_tags)

