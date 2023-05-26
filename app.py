import requests
import random
from dotenv import dotenv_values

# Load environment variables
config = dotenv_values('.env')
access_token = config['ACCESS_TOKEN']

# Load prompts from file
with open('prompts.txt', 'r') as file:
    prompts = file.readlines()

# Select a random prompt
prompt = random.choice(prompts).strip()

# Generate post content
content = f"🚀 [GeekWerkes] {prompt}"
if 'technology' in prompt.lower():
    content += ' #technology'
if 'devsecops' in prompt.lower():
    content += ' #devsecops'
if 'artificial intelligence' in prompt.lower():
    content += ' #artificialintelligence'
else:
    content += ' #SocialNetworking'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
}

data = {
    'author': 'urn:li:person:YOUR_LINKEDIN_USER_ID',  # Replace with your LinkedIn user ID
    'lifecycleState': 'PUBLISHED',
    'specificContent': {
        'com.linkedin.ugc.ShareContent': {
            'shareCommentary': {
                'text': content,
            },
            'shareMediaCategory': 'NONE',
        },
    },
    'visibility': {
        'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC',
    },
}

response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, json=data)

if response.status_code == 201:
    print('Post successful!')
else:
    print('Post failed:', response.json())