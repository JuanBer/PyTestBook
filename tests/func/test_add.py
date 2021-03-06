import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set(tasks_db):
    """Make sure the task id field is set by tasks.add()"""
    # GIVEN an initialized tasks db
    # AND a new tasks is added
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # GIVEN a db with 3 tasks
    # WHEN another task is added
    tasks.add(Task('throw a party'))

    # THEN the count increases by one
    assert tasks.count() == 4



# @pytest.fixture(autouse=True)
# def initialized_tasks_db(tmpdir):
#     """Connect to to database before testing, disconnect after."""
#     # Setup: start db
#     tasks.start_tasks_db(str(tmpdir), 'tiny')
#
#     yield # this is where the testing happens
#
#     # Teardown: stop db
#     tasks.stop_tasks_db()

