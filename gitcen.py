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
        day = datetime.datetime.fromtimestamp(commit.commit_time).strftime("%A")
        number = data.get(day, 0)
        number += 1
        data[day] = number
    print(f"Sunday has {data.get('Sunday', 0)} commits")
    print(f"Monday has {data.get('Monday', 0)} commits")
    print(f"Tuesday has {data.get('Tuesday', 0)} commits")
    print(f"Wednesday has {data.get('Wednesday', 0)} commits")
    print(f"Thursday has {data.get('Thursday', 0)} commits")
    print(f"Friday has {data.get('Friday', 0)} commits")
    print(f"Saturday has {data.get('Saturday', 0)} commits")


def get_time(path):
    """Function to find the commits done on each hour"""
    times = {}
    repo = Repository(path)
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL):
        time = datetime.datetime.fromtimestamp(commit.commit_time).strftime("%-H")
        number = times.get(time, 0)
        number += 1
        times[time] = number
    for time in range(0, 24):
        print(f"{time} hour has {times.get(str(time), 0)} commits")


def authors(path):
    """Function to find the commits done on each authors, with their name and mail id"""
    info = {}
    repo = Repository(path)
    for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL):
        author = commit.author.name
        email = commit.author.email
        key = f"{author} <{email}>"
        number = info.get(key, 0)
        number += 1
        info[key] = number
    for author, number in info.items():
        msg = f"{author} has {number} of commits"
        print(msg)


@click.command()
@click.option("--path", help="Will print the path provided.")
@click.option(
    "--author", is_flag=True, help="Will print the which author has how many commits."
)
@click.option("--all", is_flag=True, help="Will print all the informations.")
def main(path, author, all):
    """This is the primary function from where I am calling the other functions"""
    if not path:
        click.echo("You need to provide the path.")
        return

    ##here means we have a path

    if os.path.exists(path):
        click.echo("{0} this is the path provided.".format(path))

        if not path.endswith(".git" or ".git/"):
            path = os.path.join(path, ".git")
            if not os.path.exists(path):
                print("This is not a git repo")
                return
        #  Now we have the correct path for a git repository.
        #  The value for path/the file path has .git or .git/ at the end.
        if author:
            authors(path)
        elif all:
            date(path)
            get_time(path)
            authors(path)
        else:
            date(path)
            get_time(path)

    else:
        print("Please provide a correct git repository path.")


if __name__ == "__main":
    main()
