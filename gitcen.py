"""This module does a census/survey of a git repo"""
import os
import datetime
import click
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL


def date(path):
    """Function to find the commits done on each day"""
    data = {}
    repo = Repository(path)
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL):
        day = datetime.datetime.fromtimestamp(commit.commit_time).strftime('%A')
        number = data.get(day, 0)
        number += 1
        data[day] = number
    print("Sunday has {0} commits".format(data["Sunday"]))
    print("Monday has {0} commits".format(data["Monday"]))
    print("Tuesday has {0} commits".format(data["Tuesday"]))
    print("Wednesday has {0} commits".format(data["Wednesday"]))
    print("Thursday has {0} commits".format(data["Thursday"]))
    print("Friday has {0} commits".format(data["Friday"]))
    print("Saturday has {0} commits".format(data["Saturday"]))




def get_time(path):
    """Function to find the commits done on each hour"""
    times = {}
    repo = Repository(path)
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL):
        time = datetime.datetime.fromtimestamp(commit.commit_time).strftime('%-H')
        number = times.get(time, 0)
        number += 1
        times[time] = number
    for time in range(0, 24):
        print("%d hour has %d commits" % (time, times.get(str(time), 0)))

def authors(path):
    """Function to find the commits done on each authors, with their name and mail id"""
    info = {}
    repo = Repository(path)
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL):
        author = commit.author.name
        email = commit.author.email
        key = "{0} <{1}>".format(author, email)
        number = info.get(key, 0)
        number += 1
        info[key] = number
    for author, number in info.items():
        msg = "{0} has {1} commits".format(author, number)
        print(msg)

@click.command()
@click.option('--path', help="Will print the path provided.")
@click.option('--author', is_flag=True, help="Will print the which author has how many commits.")
def main(path, author):
    """This is the primary function from where I am calling the other functions"""
    if not path:
        click.echo("You need to provide the path.")
        return

   ##here means we have a path

    if os.path.exists(path):
        click.echo('{0} this is the path provided.'.format(path))

        if not path.endswith(".git" or ".git/"):
            path = os.path.join(path, ".git")
            if not os.path.exists(path):
                print("This is not a git repo")
                return
        print(path)
        if author:
            authors(path)
        else:
            date(path)
            get_time(path)

    else:
        print("Please provide a correct git repository path.")
