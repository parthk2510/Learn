'''Given a decimal number convert to Binary and count the number of 1 in the binary number '''
def get_bianry(nums):
    binary_str = ""
    while nums > 0:
        rem = nums % 2
        binary_str = str(rem)+binary_str
        nums = nums // 2
    return binary_str


if __name__ == "__main__":
    n = int(input("Enter the decimal number "))
    Binary_Number = get_bianry(n)
    print("The Binary number is", Binary_Number)

    Count=Binary_Number.count("1")
    print(Count)