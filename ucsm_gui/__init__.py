import socket
import sys

from six.moves.urllib.error import URLError

from ucsmsdk import ucsexception
from ucsmsdk import ucshandle
from ucsmsdk.utils import ucsguilaunch

socket.setdefaulttimeout(5)


def _check_host_reachable(host):
    try:
        socket.gethostbyaddr(host)
        return True
    except socket.herror:
        return False
    except socket.gaierror:
        return False


def launch(hostname, username, password):
    if not _check_host_reachable(hostname):
        sys.exit("UCSM is unreachable check network/config")

    # Login to the server
    handle = ucshandle.UcsHandle(hostname, username, password)

    try:
        handle.login()
    except URLError:
        sys.exit("Error logging into UCSM. Check hostname/ip is correct.")
    except ucsexception.UcsException:
        sys.exit("Authentication error. Check username/password.")

    # launch the UCSM GUI
    ucsguilaunch.ucs_gui_launch(handle)
