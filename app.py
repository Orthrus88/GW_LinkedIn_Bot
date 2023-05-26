import requests
import random
import openai
from dotenv import dotenv_values

# Load environment variables
config = dotenv_values('.env')
access_token = config['ACCESS_TOKEN']

# Load prompts from file
with open('prompts.txt', 'r') as file:
    prompts = file.readlines()

# Select a random prompt
prompt = random.choice(prompts).strip()

# Prompt ChatGPT for post content
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=100,
    temperature=0.7,
    n=1,
    stop=None,
)

if 'choices' in response and len(response.choices) > 0:
    content = response.choices[0].text.strip()


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