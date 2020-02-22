


def wOBA(row):
    """
    parameters
    ------------
    row: row of a DataFrame object
        row must contain BB, HBP, 1B, 2B, 3B, HR, AB, SF, and IBB

    return
    ------------
        weighted on base average given a player's stats
    """
    bbwgt = 0.69
    hbpwgt = 0.719
    wgt1b = 0.870
    wgt2b = 1.217
    wgt3b = 1.529
    hrwgt = 1.940
    return ((bbwgt * row['BB'] + hbpwgt * row['HBP'] + wgt1b * row['1B'] + wgt2b * row['2B']
             + wgt3b * row['3B'] + hrwgt * row['HR']) /
            (row['AB'] + row['BB'] - row['IBB'] + row['SF'] + row['HBP']))


def wRAA(row):
    """
    parameters
    ------------
    row: row of a DataFrame object
        row must contain the calculated wOBA and also PA

    return
    ------------
        weighted runs above average
    """
    lgwOBA = .321
    wOBA_scale = 1.21
    return ((row['wOBA'] - lgwOBA) / wOBA_scale) * row['PA']