import logging
import os
import ghapi.all as ghapi
import mkdocs.plugins

GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
log = logging.getLogger('mkdocs')

@mkdocs.plugins.event_priority(-50)        
def on_config(config, **kwargs):
    log.info(f"Injecting git repo info into config: {GITHUB_REPOSITORY}")
    config['repo_name'] = GITHUB_REPOSITORY
    config['repo_url'] = f"https://github.com/{GITHUB_REPOSITORY}"
    return config