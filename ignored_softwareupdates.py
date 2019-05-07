#!/usr/bin/env python

import subprocess


def main():
    """Returns list of ignored software updates"""

    result = "None"

    try:
        proc = subprocess.Popen(
            ["/usr/sbin/softwareupdate", "--ignore"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, _ = proc.communicate()
    except (IOError, OSError):
        stdout = None

    if stdout:
        d = str(stdout.split("(", 1)[-1].rsplit(")", 1)[0])

        if d.isspace():
            result = None
        else:
            d = [x.strip() for x in d.split(",")]
            updates = []
            for swu in d:
                swu = swu.strip('"')
                updates.append(swu)

    result = "\n".join(updates)
    print("<result>%s</result>" % result)


if __name__ == "__main__":
    main()
