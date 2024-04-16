from invoke import task

@task
def local_command(c):
    c.local('ls -l')
