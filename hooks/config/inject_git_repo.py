import os
import ghapi.all as ghapi
import mkdocs.plugins

GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')

@mkdocs.plugins.event_priority(-50)        
def on_config(config, **kwargs):
    config['repo_name'] = GITHUB_REPOSITORY
    config['repo_url'] = f"https://github.com/{GITHUB_REPOSITORY}"
    config['repo_owner'] = GITHUB_REPOSITORY.split('/')[0]
    config['repo'] = GITHUB_REPOSITORY.split('/')[1]
    return config