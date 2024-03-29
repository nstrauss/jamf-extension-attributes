#!/usr/bin/env python

# Note - This EA is not being updated to Python 3 as `--ignore`` no longer works on newer macOS versions

"""
Jamf Pro extension attribute to return a list of ignored softwareupdates added
by using something like `softwareupdate --ignore "Security Update 2019-001"

Useful to manage ignored software updates by scoping smart groups to specific
updates as needed.
"""

import subprocess


def main():
    """Returns list of ignored software updates"""

    result = "None"
    updates = []

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/softwareupdate", "--ignore"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    d = str(stdout.split("(", 1)[-1].rsplit(")", 1)[0])
    if d.isspace():
        result = None
    else:
        d = [x.strip() for x in d.split(",")]
        for swu in d:
            swu = swu.strip('"')
            updates.append(swu)

    if not updates:
        updates.append("None")

    result = "\n".join(updates)
    print("<result>%s</result>" % result)


if __name__ == "__main__":
    main()
