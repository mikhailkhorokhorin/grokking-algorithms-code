def countdown(i: int) -> None:
    print(i)
    if i <= 1:
        return
    countdown(i - 1)


def fact(x: int) -> int:
    return 1 if x == 1 else x * fact(x - 1)
