import pytest
from collections import namedtuple
import datetime
import time
import random

# implementation of the fixture check_duration
# in test_slower.py but it only writes once in the cache file
# instead of each time for each test case

Duration = namedtuple('Duration', ['current', 'last'])


@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/testdurations'
    # read previous entry, if not cache data then
    # a empty dictonary
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    node_id = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[node_id] = duration
    if d.last.get(node_id, None) is not None:
        error_string = "test duration over 2x last duration"
        assert duration <= (d.last[node_id] * 2), error_string


@pytest.mark.parametrize('i', range(10))
def test_slow_stuff(i):
    time.sleep(random.random())
