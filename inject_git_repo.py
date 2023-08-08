import os
import ghapi.all as ghapi
from mkdocs.config import base, config_options as c

GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')

class InjectGitRepoPlugin(base.BasePlugin):
        
        def on_config(self, config, **kwargs):
            config['repo_name'] = GITHUB_REPOSITORY
            config['repo_url'] = f"https://gitbug.com/{GITHUB_REPOSITORY}"
            config.theme.icon.repo = "simple/github"
            return config