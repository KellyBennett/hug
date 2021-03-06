import hug

API = hug.API('git')


@hug.object(name='git', version='1.0.0', api=API)
class GIT(object):
    """An example of command like calls via an Object"""

    @hug.object.cli
    def push(self, branch='master'):
        return 'Pushing {}'.format(branch)

    @hug.object.cli
    def pull(self, branch='master'):
        return 'Pulling {}'.format(branch)


if __name__ == '__main__':
    API.cli()
