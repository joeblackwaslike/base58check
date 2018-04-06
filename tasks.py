from invoke import task


@task
def test(ctx):
    ctx.run('pytest')
    ctx.run('pyroma .')
    ctx.run('pylint')


@task
def clean(ctx):
    ctx.run('rm -rf build dist')


@task(pre=[clean])
def build(ctx):
    ctx.run('python3 setup.py sdist bdist_wheel')


@task
def upload(ctx, environment='production'):
    if environment == 'production':
        server = 'pypi'
    elif environment == 'test':
        server = 'test'
    ctx.run(
        'twine upload -r {} --sign --identity E23F8CA8 dist/*'.format(server))
