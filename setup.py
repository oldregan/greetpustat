from setuptools import find_packages, setup

with open('greetpustat/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

REQUIRES = ['bs4','requests','argparse','ascii']

setup(
    name='greetpustat',
    version=version,
    description='',
    long_description=readme,
    author='Min',
    author_email='renmin0424@gmail.com',
    maintainer='Min',
    maintainer_email='renmin0424@gmail.com',
    url='https://github.com/oldregan/greetpustat',
    license='MIT/Apache-2.0',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    entry_points={
        'console_scripts': [ 'greetpustat = greetpustat.__main__:main' ]
        },
    packages=find_packages(),
)
