"""
Program to compute the hamming distance between two strings.
"""

def get_hamming_distance(s1: str, s2: str) -> int:
    """
    Calculates the hamming distance between two equal length strings.

    s1: string - the first string to test
    s2: string - the second string to test

    returns: int representing hamming distance between s1 and s2
    """
    if len(s2) != len(s1):
        return -1

    distance = 0
    for i in range(len(s1)):
        distance += 1 if s1[i] != s2[i] else 0

    return distance


def main() -> bool:

    str1 = ""
    str2 = ""

    while True:
        str1 = input("Please enter the first string : ")
        str2 = input("Please enter the second string: ")

        if len(str2) != len(str1):
            print("Strings must be the same length!")
            continue
        else:
            break

    hamming_distance = get_hamming_distance(str1, str2)
    print("Distance: ", hamming_distance)

    return True

if __name__ == '__main__':
    main()
