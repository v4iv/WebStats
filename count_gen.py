import re


def unique_count(filename, websites):
    pattern = re.compile("\shttps?://(.+?)/.+\s")
    with open(filename,"r",encoding='utf-8',errors='ignore') as fp:
        for line in fp:
            match_object = pattern.search(line)
            if match_object:
                websites[match_object.group(1)] = websites.get(match_object.group(1), 0) + 1
    return websites


def visit_count(filename):
    no_of_lines = (sum(1 for line in open(filename,encoding='utf-8',errors='ignore')))
    return no_of_lines
