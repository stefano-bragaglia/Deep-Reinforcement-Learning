from reinforce import __version__


def test_version():
    assert isinstance(__version__, str)
