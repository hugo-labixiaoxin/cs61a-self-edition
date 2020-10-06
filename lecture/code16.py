def prefixes(x):
    if x:
        yield x
        yield from prefixes(x[:-1])
      