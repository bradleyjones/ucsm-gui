.. image:: https://travis-ci.org/bradleyjones/ucsm-gui.svg?branch=master
    :target: https://travis-ci.org/bradleyjones/ucsm-gui

.. image:: https://coveralls.io/repos/github/bradleyjones/ucsm-gui/badge.svg
    :target: https://coveralls.io/github/bradleyjones/ucsm-gui

========
ucsm-gui
========

Usage: ucsm-gui [OPTIONS] HOST [USERNAME] [PASSWORD]

Launch UCSM GUI

Options:
 +-------------------+----------------------------+
 | -c, --config PATH | Path to config file        |
 +-------------------+----------------------------+
 | -h, --help        | Show this message and exit.|
 +-------------------+----------------------------+

************************
Arch Linux Install Notes
************************
Requires oracle java for gui to work (jdk8 from AUR)

Add /usr/lib/jvm/default/bin to path to get javaws binary

``export PATH=$PATH:/usr/lib/jvm/default/bin``

*******************
MacOS Install Notes
*******************
Works with system Java install just ensure it is up to date
