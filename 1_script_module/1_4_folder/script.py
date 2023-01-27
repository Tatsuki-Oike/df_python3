from function import module
# import function.module
# import function.module as fm
# from function.module import add

def main():
    y = module.add(1, 3)
    # y = function.module.add(1, 3)
    # y = fm.add(1, 3)
    # y = add(1, 3)
    print(y)

if __name__ == "__main__":
    main()