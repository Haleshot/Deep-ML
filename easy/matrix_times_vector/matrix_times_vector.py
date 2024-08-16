def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float]:
    if len(a) == len(b):
        l = []
        for i in a:
            temp, c = 0, 0
            for j in i:
                temp += j * b[c]
                c += 1
            l.append(temp)
        return l
    return -1  # type: ignore


if __name__ == "__main__":
    a = [[1, 2], [2, 4]]
    b = [1, 2]
