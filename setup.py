import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ALRecipes',
      version='0.2.0',
      description=('A docassemble extension.'),
      long_description='# docassemble.ALRecipes\r\n\r\n## Content\r\nThis repository includes both short examples you can insert directly into\r\nyour own playground, and longer examples that you can discover from its landing page: Quinten please add the link here.\r\n\r\n  - Some Playground examples for the Document Assembly Line project.\r\n  - Generic docassemble recipe interviews to address a particular need.\r\n  \r\nTo learn more, visit the [ALDocumentation website - ALRecipes](https://suffolklitlab.org/docassemble-AssemblyLine-documentation/docs/framework/alrecipes) page.\r\n\r\n## Add examples to your own playground\r\n\r\nEdit the /config, and add the following: \r\n\r\n```yaml\r\nplayground examples:\r\n  - docassemble.ALRecipes:data/questions/examples.yml\r\n  - docassemble.base:data/questions/example-list.yml  \r\n```\r\n\r\n',
      long_description_content_type='text/markdown',
      author='AssemblyLine',
      author_email='52798256+plocket@users.noreply.github.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['mechanize>=0.4.5'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ALRecipes/', package='docassemble.ALRecipes'),
     )

