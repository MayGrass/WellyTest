# python 3.10.2

def fibonacci(n: int) -> int:
    """
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
    """
    # O(n**2)
    # if n > 1:
    #     return fibonacci(n - 1) + fibonacci(n - 2)
    # return n

    # O(n)
    final_three = [0, 1, 1]
    if n > 2:
        for _ in range(2, n):
            final_three[0] = final_three[1]
            final_three[1] = final_three[2]
            final_three[2] = final_three[0] + final_three[1]
    return final_three[2]


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
