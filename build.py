#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")

name = "python-workshop"
default_task = "publish"


@task
def hello():
    print("Hello!!!")


@task
def publish_to_testpypi():
    import os
    os.system(f"twine upload -r testpypi target/dist/{name}-1.0.dev0/dist/{name}-1.0.dev0.tar.gz")


@init
def set_properties(project):
    project.build_depends_on('twine')
