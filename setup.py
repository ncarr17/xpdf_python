from setuptools import setup, find_packages
from codecs import open
from os import path
import sys
import subprocess
from setuptools.command.install import install


__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


class XPDFInstall(install):
    def run(self):
        if path.isfile('/usr/local/bin/pdftotext'):
            print("Detected xpdf library.")
        else:
            print("Did not detect xpdf library. Now attempting to install...")
            try:
                if sys.platform.startswith('linux'):
                    bash_script = 'linux_install.sh'
                elif sys.platform.startswith('darwin'):
                    bash_script = 'mac_install.sh'
                full_path = path.join(path.join(here,'xpdf_python/install_xpdf/'), bash_script)
                subprocess.call(['bash',full_path])
            except Exception as e:
                print(e)
                print("Error installing xpdf.  Please follow custom installation instructions at: https://github.com/ecatkins/xpdf_python.")

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='xpdf_python',
    version=__version__,
    description='Python wrapper for xpdf',
    long_description=long_description,
    url='https://github.com/ecatkins/xpdf_python',
    download_url='https://github.com/ecatkins/xpdf_python/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Edward Atkins',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='ecatkins@gmail.com',
    #run custom code
    package_data = {
        'install_xpdf':['install_xpdf/mac_install.sh','install_xpdf/linux_install.sh']
    },
    cmdclass={'install': XPDFInstall},
)


