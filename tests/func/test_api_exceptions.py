import pytest
import tasks
from tasks import Task


class TestUpdate:
    """Test expected exceptions with tasks.update()"""

    def test_bad_id(self):
        """A non int id should raise an exception"""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1}, task=tasks.Task())

    def test_bad_task(self):
        """A non-task task should raise an exception"""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='Not a task')


def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a task object')


def test_task_with_id_raises():
    """add() should raise an exception when adding a task with an id already set"""
    with pytest.raises(ValueError):
        task = Task("Clean house", "John", True, 15)
        tasks.add(task)


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param"""
    """it expects None or a String"""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=1234)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


def test_delete_raises():
    """delete() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.delete(task_id=(1, 2, 3))



