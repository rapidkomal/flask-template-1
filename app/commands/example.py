import datetime

import click


def record_time(fn):
    def inner(*args, **kwargs):
        print('Entering at ' + str(datetime.datetime.utcnow()))
        fn(*args, **kwargs)
        print('Exiting at ' + str(datetime.datetime.utcnow()))

    return inner


@click.command()
@click.option('--name', default='NA', help="Your name")
@record_time
def hello(name):
    """
    command: python example.py --name=<name>
    :param name:
    :return:
    """
    print(f"Hello {name}")


if __name__ == '__main__':
    hello()
