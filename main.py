import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str, help="Input file (.xls)", required=True)
    parser.add_argument("--output", type=str, default="output.xlsx", help="Output file (.xlsx)")

    args = parser.parse_args()

    # Check if file ends with .xls
    if not args.input.endswith(".xls"):
        print("Input file must be .xls")
        exit(-1)

    # Check if file exists
    try:
        with open(args.input, "r") as f:
            pass
    except FileNotFoundError:
        print("Input file not found.")
        exit(-1)

    from cleaner import clean_transactions

    clean_transactions(args.input, args.output)

    # Open file in default program
    import os
    os.startfile(args.output)
