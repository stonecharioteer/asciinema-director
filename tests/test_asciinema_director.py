from asciinema_director import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_recording():
    test_commands = [
        "python",
        "import this",
        "exit()"
    ]
    import os
    if os.path.isfile("test.cast"):
        os.remove("test.cast")
    from asciinema_director import direct
    direct(test_commands, "test.cast", delay=0.01)
    assert os.path.isfile("test.cast"), "Test cast file not created!"
