## gitcen

A project to find git information. This project finds the git information about authors' commits, most active days and time.

### Dependecies

- Click
- pygit2==0.24

### How to use?

```
$ gitcen --help
Usage: gitcen [OPTIONS]

  This is the primary function from where I am calling the other functions

Options:
  --path TEXT  Will print the path provided.
  --author     Will print the which author has how many commits.
  --all        Will print all the informations.
  --help       Show this message and exit.
```

Use the ```--path``` flag to point to a git directory.
