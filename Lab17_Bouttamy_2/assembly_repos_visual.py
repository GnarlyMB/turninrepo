import requests as rq
import plotly.express as px

url = 'https://api.github.com/search/repositories'
url += '?q=assembly+sort:stars+stars:>10000'

headers = {"Accept": "application/vnd.github.v3+json"}
response = rq.get(url, headers)
print(f'Status Code: {response.status_code}')
response_dict = response.json()
print(response_dict.keys())
print(f'Total Repo: {response_dict['total_count']}')
print(f'Complete resaults: {not response_dict['incomplete_results']}')

repo_dicts = response_dict['items']
print(f'Repos returned: {len(repo_dicts)}')

repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    owner = repo_dict['owner']['login']
    stars.append(repo_dict['stargazers_count'])
    description = repo_dict['description']
    hover_text = f"{owner}<br>{description}"
    hover_texts.append(hover_text)
    

title = "Most Starred Assembly Repos on Github"
labels = {'x': 'repository', 'y': 'stars'}
fig = px.bar(x=repo_links, y=stars, hover_name=hover_texts, title=title, labels=labels)
#fig.update(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()