import pytest
import tasks
import json
from tasks import Task


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by the database


@pytest.fixture()
def tasks_db_1(tmpdir):
    """Connect to db before tests, disconnect after"""
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is were the testing happens

    # Teardown: stop db
    tasks.stop_tasks_db()


# @pytest.fixture(scope='session')
@pytest.fixture(scope='session', params=['tiny'])
def tasks_db_session(tmpdir_factory, request):
    """Connect to db before tests, disconnect after"""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """An empty tasks db."""
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Coode review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michele'),
        Task('Inspire', 'Michele'),
        Task('Encourage', 'Michele'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }
    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))
    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file


# This is a hook function
def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", help="Some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")

@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt