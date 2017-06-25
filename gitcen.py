import click
import os
import datetime
from pygit2 import Repository
from pygit2 import GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE


def date(path):
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




def time(path):
    times = {}
    repo = Repository(path)
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL):
        time = datetime.datetime.fromtimestamp(commit.commit_time).strftime('%-H')
        number = times.get(time, 0)
        number += 1
        times[time] = number
    for time in range(0, 24):
        print("%d has %d commits" % (time, times.get(str(time), 0)))

def authors(path):
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
@click.option('--path',help="Will print the path provided.")
def main(path):
    if not path:
        click.echo("You need to provide the path.")
        return

   ##here means we have a path

    if os.path.exists(path):
        click.echo('{0} this is the path provided.'.format(path))

        if not path.endswith(".git" or ".git/"):
            path = os.path.join(path, ".git")
            if os.path.exists(path):
                date(path)
                authors(path)
    else:
        print("Please provide a correct git repository path.")



