import os
from setuptools import setup
from setuptools import find_packages

import aoml


setup(name='aoml',
      version=aoml.__version__,
      description='A Django app for sending newsletter by email to a contact list.',
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      keywords='django, newsletter, mailing',
      classifiers=[
          'Framework :: Django',
          'Programming Language :: Python',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules',],

      author=aoml.__author__,
      author_email=aoml.__email__,
      url=aoml.__url__,

      license=aoml.__license__,
      packages=find_packages(exclude=['demo']),
      include_package_data=True,
      zip_safe=False,
      test_suite="runtests.runtests",
      install_requires=['setuptools',
                        'html2text',
                        'python-dateutil',
                        'bs4',
                        'django',
                        'vobject',
                        'xlwt',
                        'xlrd'],
      dependency_links=[])
