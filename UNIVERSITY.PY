def min_extra_seats(X, Y):
    return max(0, Y - X)

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        X, Y = map(int, input().strip().split())
        extra_seats = min_extra_seats(X, Y)
        print(extra_seats)

if __name__ == "__main__":
    main()
