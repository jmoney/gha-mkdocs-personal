import os
import ghapi.all as ghapi
import mkdocs.plugins

GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')

@mkdocs.plugins.event_priority(-50)        
def on_config(config, **kwargs):
    config['repo_name'] = GITHUB_REPOSITORY
    config['repo_url'] = f"https://gitbug.com/{GITHUB_REPOSITORY}"
    config.theme.icon.repo = "simple/github"
    return config