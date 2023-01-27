import sys

def print_args(args):
    print(f"input {args}")
    for i, arg in enumerate(args):
        print(f"arg{i} {arg}")

if __name__ == "__main__":
    print_args(sys.argv)
    