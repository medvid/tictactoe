def get_int(max = None):
    while True:
        try:
            val = int(input("> "))
            if max is None or val <= max:
                return val
            else:
                print("Value should not exceed " + max)
        except ValueError:
            print("Not an integer")

