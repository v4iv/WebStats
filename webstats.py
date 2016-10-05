import argparse

from count_gen import unique_count, visit_count
from graph_gen import print_stats
from rank_websites import rank_analytics


def get_parser():
    """Get parser for command line arguments."""
    arg_parser = argparse.ArgumentParser(description="Python Based Web Stats Generator")
    arg_parser.add_argument("-f",
                            "--file",
                            dest="filename",
                            help="Proxy Log File Name")
    return arg_parser


web_log = {}
arguments = get_parser()
args = arguments.parse_args()
FILE_NAME = args.filename

web_log = unique_count(FILE_NAME, web_log)
count = visit_count(FILE_NAME)
web_stats = rank_analytics(web_log, count)
print_stats(web_stats)
