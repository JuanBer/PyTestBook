"""Test the Task data type"""
from tasks import Task


def test_asdict():
    """_asdict should return a dictionary"""
    t_task = Task('do something', 'Okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'Okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """Replace() should change passed in fields"""
    t_before = Task('Finish the book', 'Brian', False)
    t_after = t_before._replace(id=10,done=True)
    t_expected = Task('Finish the book','Brian', True, 10)
    assert t_after == t_expected


def test_defaults():
    """Using no parameters should invoke defaults"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtumple"""
    t = Task('Buy milk', 'John')
    assert t.summary == 'Buy milk'
    assert t.owner == 'John'