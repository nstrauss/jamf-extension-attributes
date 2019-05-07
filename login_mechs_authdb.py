#!/usr/bin/env python

"""
Jamf Pro extension attribute to return a list of login authorization mechanisms
used in macOS login window authentication process.

Useful for reporting on authorization database modifications like when using
NoMAD Login/Jamf Connect.
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

    # Loop through mechs and format for EA. None if mech list is empty
    try:
        if authdb_mechs:
            results = "\n".join(authdb_mechs)
        else:
            results = None
    except (TypeError, KeyError):
        results = None
    print("<result>%s</result>" % results)


if __name__ == "__main__":
    main()
