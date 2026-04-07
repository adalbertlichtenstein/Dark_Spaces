from setuptools import setup
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import os
import re
import Dark_Spaces
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result
class CMakeBuild(build_ext):
    def run(self):
        subprocess.check_call(['cmake', '.'])
        subprocess.check_call(['cmake', '--build', '.'])
        super().run()

setup(
    name="Dark_Spaces",
    version="0.1.0",
    ext_modules=[Extension('univers', sources=[])],
    cmdclass={'build_ext': CMakeBuild},
)
