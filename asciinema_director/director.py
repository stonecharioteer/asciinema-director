#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""director file, contains core logic.
"""


def direct(commands, destination, delay=0.001):
    """Converts a source instruction file into destination recording."""
    import pexpect
    import time
    client = pexpect.spawn(f"asciinema rec {destination}")
    time.sleep(2)
    for command in commands:
        print(command)
        time.sleep(1)
        for char in command:
            client.send(char)
            time.sleep(delay)
        client.sendline("")
        # client.sendline(command)
    client.sendline("exit")
    client.close()


def direct_from_file(src_file, destination, delay=0.001):
    """Create asciicast file from source file."""
    with open(src_file) as f:
        commands = list(f.readlines())
    direct(commands, destination, delay)
