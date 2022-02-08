import argparse
from src import constants


# Definition of arguments used in the cli executable
def get_arguments():
    parser = argparse.ArgumentParser(description=constants.PROJECT_DESCRIPTION)

    # Main argument of the cli. Use this to search for stuff
    parser.add_argument("-s", "--search", metavar="QUERY", type=str, nargs=1, default=None,
                        help="The search query to be parsed by youtube api.")
    return parser
