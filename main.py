from warnings import warn






def add_number(a, b, c):
    warn(
        message="Warning: the add_number function is deprecated , and will be removed in a future release. Use add_number instead.",
       category= DeprecationWarning,
    )
    return a + b + c


print(add_number(1, 2, 3))