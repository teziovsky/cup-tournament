from pybuilder.core import use_plugin, init

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')
use_plugin("python.unittest")
use_plugin('python.pydev')
use_plugin('python.pycharm')
use_plugin('python.pylint')
use_plugin('pypi:pybuilder_django_enhanced_plugin')

default_task = ['analyze']


@init
def initialize(project):
    # django settings
    project.set_property('django_project', 'cupTournament')
    project.set_property('django_apps', ['tournament'])

    # Set source directory
    project.set_property('dir_source_main_python', 'cupTournament')

    # install dependencies
    project.depends_on_requirements("requirements.txt")
