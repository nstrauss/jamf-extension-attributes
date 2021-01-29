#!/usr/bin/python

"""
Jamf Pro extension attribute to return a list of NoMAD Login and Jamf Connect 
authorization mechanisms used during macOS login window authentication process.
"""

import subprocess
import plistlib


def get_login_authdb(format="string"):
    """Gets the specified authorization right from plist format."""
    try:
        cmd = ["/usr/bin/security", "authorizationdb", "read", "system.login.console"]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = proc.communicate()
        if stdout:
            return plistlib.readPlistFromString(stdout)
    except (IOError, OSError):
        pass


def main():
    # Get list of authorization mechanisms
    authdb = get_login_authdb()
    authdb_mechs = authdb["mechanisms"]

    # Find all non-default NoMAD/Jamf mechs
    try:
        xtra_mechs = []
        for mech in authdb_mechs:
            if "NoMADLogin" in mech or "JamfConnect" in mech:
                xtra_mechs.append(mech)
    except (AttributeError, KeyError):
        pass

    # Loop through mechs and format for EA. None if mech list is empty
    try:
        if xtra_mechs:
            results = "\n".join(xtra_mechs)
        else:
            results = None
    except (TypeError, KeyError):
        results = None
    print("<result>%s</result>" % results)


if __name__ == "__main__":
    main()
