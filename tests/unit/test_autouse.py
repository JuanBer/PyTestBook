import pytest
import time

@pytest.fixture(scope='session', autouse=True)
def footer_session_scope():
    """Report the time at the end of a session"""
    yield
    now = time.time()
    print('--')
    print('finish: {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('--------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report tests duration after each function"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration: {:0.3} seconds'.format(delta))


def test_1():
    """Simulate long-ish running test."""
    time.sleep(2)


def test_2():
    """Simulate slightly longer test."""
    time.sleep(2.50)


