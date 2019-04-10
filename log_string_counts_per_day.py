#!/usr/bin/env python3

import sys

# Reads lines from gunicorn log such as:
# [2019-01-22 13:18:48,946] [smartcambridge.views] [INFO] - : |logger|pocket|VVKA-4702|stop_timetable|component_ref=0500CCITY527|

def log_date(line):
    return line[1:11]

def log_client(line):
    log_parts = line.split("|")
    return log_parts[3]

if __name__=="__main__":

    if len(sys.argv) != 3:
        print("Usage: ")
        print("  log_string_counts_per_day.py [input file] [search string] >output_file_name")
        sys.exit(0)

    INPUT_FILE = sys.argv[1]

    SEARCH_STRINGS = sys.argv[2].split(",")

    string_counts = [0]*len(SEARCH_STRINGS)

    current_date = None

    print(f'Date,{sys.argv[2]}')

    ####################################################################
    # iterate through file
    ####################################################################
    with open(INPUT_FILE, 'rU') as f:

        for line in f:

            line_date = log_date(line)

            for i in range(len(SEARCH_STRINGS)):
                SEARCH_STRING = SEARCH_STRINGS[i]
                if SEARCH_STRING in line:

                    if current_date is None:
                        current_date = line_date
                        string_counts[i] += 1

                    elif current_date == line_date:
                        string_counts[i] += 1

            if current_date is not None and line_date != current_date:
                # current_date is not None and current_date != line_date
                print(f'{current_date},{",".join([str(x) for x in string_counts])}')
                string_counts = [0] * len(SEARCH_STRINGS)
                current_date = line_date



