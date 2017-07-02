from setuptools import setup

setup(
    name="gitcen",
    version='0.1',
    description="A project to find git information.",
    long_description="A project to find git information about authors' commits,most active days and time.",
    author="Anwesha Das.",
    author_email="anwesha@das.community",
    url="https://github.com/anweshadas/gitcen",
    license="GPLv3+",
    py_modules=['gitcen'],
    install_requires=[
        'Click',
        'pygit2==0.24'
    ],
    entry_points='''
        [console_scripts]
        gitcen=gitcen:main
    ''',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment:: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language:: Python:: 3.6'
    )
)