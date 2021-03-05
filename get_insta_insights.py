#!/usr/bin/env python3

from getopt import getopt
import sys
import os

import constant

from instagram import instagram_data
from insights import hashtags
from insights import timings
from insights import htmlutils

options = "mh"
long_options = ["machine-learning", "help", "page-id=", "token=", "num-timings=", "num-tags=", "graphs"]


def usage():
    print(f"""usage:

insta-insights --page-id=<page-id> --token=<token> --num-timings=<integer> --num-tags=<integer>

Entering page ID and token everytime when insta-insights is invoked can be avoided by setting them as env variables.
    
Environment variables supported:
FB_TOKEN
FB_PAGE_ID

Read more at: https://github.com/PardhuMadipalli/instagram-insights#quickstart
""")


def main():
    token = None
    page_id = None
    timing_indices = 3
    tag_indices = 5
    graphs = False
    try:
        """ Parse Arguments """
        arguments, values = getopt(sys.argv[1:], options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ["-h", "--help"]:
                usage()
                sys.exit(0)
            if currentArgument in ["-m", "--machine-learning"]:
                raise RuntimeError('Machine learning is not supported yet. Use -h for help.')
            if currentArgument == "--page-id":
                page_id = currentValue
            if currentArgument == "--token":
                token = currentValue
            if currentArgument == "--num-tags":
                tag_indices = int(currentValue)
            if currentArgument == "--num-timings":
                timing_indices = int(currentValue)
            if currentArgument == "--graphs":
                graphs = True
        if token is None:
            token = os.environ.get("FB_TOKEN")
        if page_id is None:
            page_id = os.environ.get("FB_PAGE_ID")

        """ Main function starts here"""

        instagram_data.get_insights(token, page_id)

        htmlutils.create_html()

        timings.get_timing_insights(constant.INSIGHTS_CSV, timing_indices)
        hashtags.get_best_tags(constant.INSIGHTS_CSV, graphs, tag_indices)

        htmlutils.end_html()

    except Exception as ex:
        usage()
        raise ex


if __name__ == "__main__":
    main()
