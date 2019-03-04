import pytest


# pytestconfig is a fixture with session scope
def test_option(pytestconfig):
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt" set to:', pytestconfig.getoption('myopt'))


def test_fixtures_for_options(foo, myopt):
    print("Option 'foo' value set to: ", foo)
    print("Option 'myopt' value set to: ", myopt)


def test_pytestconfig(pytestconfig):
    print('args: ', pytestconfig.args )
    print('inifile: ', pytestconfig.inifile)
    print('invocation_dir: ', pytestconfig.invocation_dir)
    print('rootdir: ', pytestconfig.rootdir)
    print('-k EXPRESSION: ', pytestconfig.getoption('keyword'))
    print('-v --verbose: ', pytestconfig.getoption('verbose'))
    print('-q, --quiet: ', pytestconfig.getoption('quiet'))
    print('-l, --showlocals: ', pytestconfig.getoption('showlocals'))
    print('--tb=style :', pytestconfig.getoption('tbstyle'))


