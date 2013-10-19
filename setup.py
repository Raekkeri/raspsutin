from setuptools import setup, find_packages

setup(name='raspsutin-project',
    version='0.01',
    description='A simple Django website',
    author='Teemu Husso',
    author_email='teemu.husso@gmail.com',
    url='',
    packages=find_packages(exclude=['ez_setup']),
    package_dir={
        '': 'src',
        },
    install_requires=[
        'setuptools',
        'django==1.5.4',
        'psycopg2==2.5.1',
        ],
)
