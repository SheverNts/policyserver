import argparse
import sys
import logging
from policyserver import logger


import policyserver.config as conf
from policyserver.commands.server import server


def main():
    parser = argparse.ArgumentParser(
        prog="policyserver", usage=argparse.SUPPRESS, add_help=True
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {conf.VERSION}"
    )
    parser.add_argument(
        "-l",
        "--log-level",
        dest="log_level",
        default="info",
        help="log level.",
        required=False,
        choices=["info", "debug", "error", "warn"],
    )

    subparsers = parser.add_subparsers(dest="subparser_name", help="sub-commands")
    server_parsers = subparsers.add_parser("server", help="run server.")
    server_parsers.add_argument(
        "-r", "--rules", dest="rules", help="rules path", metavar="", required=True
    )
    server_parsers.add_argument(
        "-p",
        "--port",
        dest="port",
        help="port to listen.",
        metavar="",
        required=False,
        default=8081,
    )
    server_parsers.add_argument(
        "-H",
        "--host",
        dest="host",
        help="ip to bind.",
        metavar="",
        required=False,
        default="0.0.0.0",
    )
    server_parsers.set_defaults(func=server)

    arguments = parser.parse_args()
    if arguments.subparser_name:
        logger.set_level(arguments.log_level)
        arguments.func(arguments)


if __name__ == "__main__":
    main()
