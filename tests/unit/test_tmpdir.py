import pytest


def test_tempdir(tmpdir):
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is created when it's written to
    a_file = tmpdir.join('something.txt')

    # you can create directories
    a_sub_dir = tmpdir.mkdir('newsubdirectory')

    # you can create files in directories (created when written)
    another_file = a_sub_dir.join('something_else.txt')

    # this writes creates 'something.txt'
    a_file.write('contents may settle during shipping')

    # this creates 'newsubdirectory/something_else.txt
    another_file.write('something different')

    # you can read the files as well
    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"

