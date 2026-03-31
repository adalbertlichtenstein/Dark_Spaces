
# Source - https://stackoverflow.com/a/41110107
# Posted by Eric Blum
# Retrieved 2026-03-10, License - CC BY-SA 3.0

from setuptools import setup
import re
import Dark_Spaces
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result 
    

project_name = 'Dark_Spaces'
setup(
    
    version = get_property('__version__', project_name),
    
)
