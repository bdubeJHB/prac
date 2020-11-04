import sys


def sqrt(num) -> float:
    """returns the square root of natural number, correct to two decimal points"""
    root = 1

    if num < 1 or not isinstance(num, int):
        return 0
    elif num == 1:
        return root

    def check_decimal(start):
        increment_value = 0.1

        while start < root:
            #print(f"Current root is: {start}.  Which goes to {start * start}")
            if start * start > num and increment_value == 0.1:
                start -= increment_value
                increment_value = 0.01
            elif start * start + increment_value > num:
                return start

            start += increment_value
        return start

    while root < num / 2 + 1:
        if root * root == num:
            break

        if root * root > num:
            root = check_decimal(root - 1)
            break

        root += 1

    return root


if __name__ == "__main__":
    #print(sqrt(1))
    #print(sqrt(4))
    #print(sqrt(9))
    print(sqrt(10))
    #print(sqrt(5421345678))
    #pass
