from setuptools import setup

setup(
    name="gitcen",
    version='0.1',
    py_modules=['gitcen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gitcen=gitcen:main
    ''',
)