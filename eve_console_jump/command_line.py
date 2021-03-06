import argparse
import os
import sys

import mysql.connector


def get_parser():
    description = "Easily connect to EVE-ng VMs console port from terminal"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "-e", required=True, metavar="HOSTNAME", dest="host", help="EVE-ng host"
    )

    parser.add_argument(
        "-u",
        metavar="USERNAME",
        required=True,
        dest="username",
        help="EVE-ng database username",
    )

    parser.add_argument(
        "-p",
        metavar="PASSWORD",
        required=True,
        dest="password",
        help="EVE-ng database password",
    )

    parser.add_argument(
        "-i", required=False, metavar="INDEX", dest="index", help="VM index"
    )

    return parser


def connect(host, user, password):
    evedb = mysql.connector.connect(
        host=host, user=user, password=password, database="eve_ng_db"
    )
    return evedb


def get_vms(db):
    cursor = db.cursor()
    cursor.execute("select port, LabName, name from console")
    return list(cursor)


def print_summary(vms):
    for index, (port, lab, vm) in enumerate(vms):
        print("{:2}| {}: {}".format(index, lab[1:], vm))


def main():
    parser = get_parser()
    args = parser.parse_args()

    db = connect(args.host, args.username, args.password)
    vms = get_vms(db)
    db.disconnect()

    if not args.index:
        print_summary(vms)
    else:
        try:
            vm = vms[int(args.index)]
            ssh_command = 'ssh -t {}@{} "telnet localhost {}"'.format(
                args.username, args.host, vm[0]
            )
            print("Connecting to {}...".format(vm[2]))
            print(" - {}".format(ssh_command))
            os.system(ssh_command)
        except IndexError:
            print("VM index does not exist")


if __name__ == "__main__":
    main()
