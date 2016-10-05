def print_stats(web_stats):
    s = 0
    for site in sorted(web_stats, key=web_stats.get, reverse=True)[:10]:
        s += web_stats[site]
        print(site, "was visited %.2f" % web_stats[site], "% times\n")
    others = 100 - s
    print("others were visited ", "%.2f" % others, "% times")
