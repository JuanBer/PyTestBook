import pytest
import tasks
from tasks import Task

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

tasks_ids = ['Tasks({},{},{})'.format(t.summary, t.owner, t.done)
             for t in tasks_to_try]


def id_func(fixture_value):
    """A function for generating ids."""
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """using no ids"""
    return request.param


@pytest.fixture(params=tasks_to_try, ids=tasks_ids)
def b_task(request):
    """using no ids"""
    return request.param


@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Using a function (id_func) to generate ids."""
    return request.param


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return (t1.summary == t2.summary) and (t1.owner == t1.owner) and (t1.done == t2.done)


def test_add_a(tasks_db, a_task):
    """Using b_task fixture (with ids)."""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


def test_add_b(tasks_db, b_task):
    """Using b_task fixture (with ids)."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


def test_add_c(tasks_db, c_task):
    """Using b_task fixture (with ids)."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)

