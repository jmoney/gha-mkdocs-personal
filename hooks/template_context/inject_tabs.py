import os
import mkdocs.plugins


@mkdocs.plugins.event_priority(-50)        
def on_template_context(context, template_name, config):
    context['tabs'] = [
        {'title': 'Home', 'url': 'https://jmoney.dev/home'},
        {'title': 'Blogs', 'url': 'https://jmoney.dev/blogs'},
        {'title': 'Cloud', 'url': 'https://jmoney.dev/cloud'},
        {'title': 'Homebrew', 'url': 'https://jmoney.dev/homebrew'},
        {'title': 'TIL', 'url': 'https://jmoney.dev/til'},
        {'title': 'Resume', 'url': 'https://github.com/jmoney/resume/releases/download/latest/JonathanMonette_resume.pdf'}
    ]
    return context