def checker_option(n, statement):
    x = int(input(statement))
    if x < 0 or x >= n:
        checker(n, statement)
    else:
        return x

