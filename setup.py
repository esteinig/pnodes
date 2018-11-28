from setuptools import setup, find_packages


setup(
    name='pnodes',
    url='https://github.com/esteinig/pnodes',
    author='Eike J. Steinig',
    author_email='eikejoachim.steinig@my.jcu.edu.au',
    packages=find_packages(),
    install_requires=['colorama', 'delegator.py', 'tqdm', 'python-dateutil', 'click'],
    version='0.1',
    license='MIT',
    include_package_data=True,
    description="Pretty print pbsnodes (-a) on Torque/PBS.",
    entry_points='''
        [console_scripts]
        pnodes=pnodes.terminal.client:terminal_client
    ''',
)