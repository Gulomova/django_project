import time

from invoke import task, run


def wait_port_is_open(host, port):
    import socket
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return
        time.sleep(1)


@task
def init_db(ctx, recreate_db=False):
    wait_port_is_open('db', 5432)
    if recreate_db:
        ctx.run('python manage.py dbshell < clear.sql')
        ctx.run('python manage.py dbshell < db.dump')
    ctx.run('python manage.py makemigrations')
    ctx.run('python manage.py migrate')


@task
def collect_static_element(ctx):
    ctx.run('python manage.py collectstatic --noinput')


@task
def run(ctx):
    init_db(ctx, recreate_db=False)
    collect_static_element(ctx)
    ctx.run('python manage.py runserver 0.0.0.0:9000')
