def prefixes(x):
    if x:
       yield from prefixes(x[:-1])
       yield x