"""Use the Task type to show test failures"""
from tasks import Task


def test_task_equality():
    """Different tasks should be not equal."""
    t1 = Task('Sit here', 'Brian')
    t2 = Task('Do something', 'Okken')
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal"""
    t1_dict = Task('Make a sandwich', 'John')._asdict()
    t2_dict = Task('Make a sandwich', 'Maria')._asdict()
    assert t1_dict == t2_dict


