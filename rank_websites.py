def rank_analytics(websites, total):
    for site in (websites.keys()):
        websites[site] = (websites[site] / total) * 100
    return websites
