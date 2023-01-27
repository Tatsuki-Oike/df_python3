import argparse

def main():
    parser = argparse.ArgumentParser(
            prog='3_3_argparse2.py', # プログラム名
            usage='usage', # プログラムの利用方法
            description='description', # 引数のヘルプの前に表示
            epilog='end', # 引数のヘルプの後で表示
            add_help=True, # -h/-–helpの追加
            )

    parser.add_argument('arg1')
    parser.add_argument('--arg2')
    parser.add_argument('-a', '--arg3')

    args = parser.parse_args()

    print(args)
    print(args.arg1, args.arg2, args.arg3)

if __name__ == "__main__":
    main()
    