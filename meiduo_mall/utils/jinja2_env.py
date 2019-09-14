from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        #静态文件的路由
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env