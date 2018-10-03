def lines(a, b):
    """Return lines in both a and b"""

    numsa = a.splitlines()
    numsb = b.splitlines()
    retnums = []
    for line in numsa:
        for morelines in numsb:
            if line == morelines and morelines not in retnums:
                retnums.append(morelines)
                break
    return retnums


def sentences(a, b):
    """Return sentences in both a and b"""
    from nltk.tokenize import sent_tokenize

    numsa = sent_tokenize(a)
    numsb = sent_tokenize(b)
    retnums = []
    for sentences in numsa:
        for moresentences in numsb:
            if sentences == moresentences and moresentences not in retnums:
                retnums.append(moresentences)
    return retnums


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    #  numsa = a
    holder, retnums = [], []
    for i in range(len(a)):
        if (len(a[i:i+n]) == n):
            holder.append(a[i:i+n])
    for i in range(len(b)):
        if b[i:i+n] in holder and b[i:i+n] not in retnums:
            retnums.append(b[i:i+n])

    # TODO
    return retnums