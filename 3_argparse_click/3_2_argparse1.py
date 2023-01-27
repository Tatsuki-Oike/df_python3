import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('arg1')
    parser.add_argument('--arg2')
    parser.add_argument('-a', '--arg3')

    args = parser.parse_args()

    print(args)
    print(args.arg1, args.arg2, args.arg3)

if __name__ == "__main__":
    main()
    