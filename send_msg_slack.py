import os
import slack


def send_msg_slack(elb_without_tags, elb_with_tags):
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    env = os.environ['ENV']

    client.chat_postMessage(
        channel="channel-name-slack",
        text="ENV: " + env + "\n" +
             "Load Balances sem tags: " + str(elb_without_tags) +
             "\nLoad Balances com tags: " + str(elb_with_tags)
    )

    client.files_upload(
        channels="channel-name-slack",
        file="lbs-reports-tags.txt",
        title="Upload report"
    )

