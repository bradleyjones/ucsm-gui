from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as rf:
        return rf.readlines()


setup(name='ucsm-gui',
      version='0.1',
      description='Launch UCSM GUI from cli',
      long_description=readme(),
      install_requires=requirements(),
      keywords='ucsm gui cisco',
      url='http://github.com/bradleyjones/ucsm-gui',
      author='Bradley Jones',
      author_email='jones.bradley@me.com',
      license='MIT',
      packages=['ucsm_gui'],
      entry_points={'console_scripts': 'ucsm-gui=ucsm_gui.command_line:main'},
      zip_safe=False)
