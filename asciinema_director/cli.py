#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Command line interface.
"""

import click


@click.command("asciinema-director")
@click.option("--delay", "-D", type=click.FLOAT, default=0.01)
@click.argument("src")
@click.argument("dest")
def cli(delay, src, dest):
    from asciinema_director.director import direct_from_file
    direct_from_file(src, dest, delay=delay)
