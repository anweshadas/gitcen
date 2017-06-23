import click
import os

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
        print(path)
    else:
        print("Please provide a correct git repository path.")



