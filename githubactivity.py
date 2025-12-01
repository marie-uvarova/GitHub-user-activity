import requests
import argparse
import json

def send_request(name):
    
    url = f'https://api.github.com/users/{name}/events'
    response = requests.get(url)
    
    json_data = json.loads(response.text)
    data = response.json()
    
    if response.status_code == 200:
        for event in data:
            timestamp = ' '.join(event['created_at'][:-1].split('T'))
            if event['type'] == 'PushEvent':
                print(f'{timestamp}: {name} pushed to {event['repo']['name']}')
            elif event['type'] == 'CreateEvent':
                print(f'{timestamp}: {name} created {event['payload']['ref_type']} {event['payload']['ref']} at {event['repo']['name']}')
            elif event['type'] == 'IssuesEvent':
                print(f'{timestamp}: {name} created issue {event['payload']['issue']['number']} at {event['repo']['name']}')
            elif event['type'] == 'ForkEvent':
                print(f'{timestamp}: {name} forked {event['repo']['name']}')
            elif event['type'] == 'IssueCommentEvent':
                print(f'{timestamp}: {name} commented on issue {event['payload']['issue']['number']} at {event['repo']['name']}')
            elif event['type'] == 'PullRequestEvent':
                print(f'{timestamp}: {name} created pull request {event['payload']['pull_request']['number']} at {event['repo']['name']}')
            elif event['type'] == 'PullRequestReviewEvent':
                print(f'{timestamp}: {name} reviewed pull request {event['payload']['pull_request']['number']} at {event['repo']['name']}')
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f'{timestamp}: {name} commented on pull request {event['payload']['pull_request']['number']} at {event['repo']['name']}')
            elif event['type'] == 'WatchEvent':
                print(f'{timestamp}: {name} starred {event['repo']['name']}')
            else:
                print(f'{timestamp}: {event['type']} happened')
    else:
        print(f'The requested URL returned error {response.status_code}: {data.get('message')}')
    
    with open('test.json', 'w+', encoding='utf-8') as tt:
        json.dump(json_data, tt, indent=4)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='This app can help you view recent GitHub user activity.',
        prog='GitHub activity',        
    )  

    parser.add_argument('name', help='')

    args = parser.parse_args()
    send_request(args.name)