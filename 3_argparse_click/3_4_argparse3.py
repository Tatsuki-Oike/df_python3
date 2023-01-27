import argparse

def main():
    parser = argparse.ArgumentParser(
            prog='3_3_argparse2.py', # プログラム名
            usage='usage', # プログラムの利用方法
            description='description', # 引数のヘルプの前に表示
            epilog='end', # 引数のヘルプの後で表示
            add_help=True, # -h/-–helpの追加
            )

    parser.add_argument('--arg1', type=int, required=True, metavar='INT', help="int argument")
    parser.add_argument('--arg2', default="defalt_string", type=str, required=False, metavar='STR', help="str argument")

    parser.add_argument('--arg3', default=False, action="store_true", required=False, help="boolean argument")
    parser.add_argument('--arg4', default=0, action="store_const", const=10, required=False, help="const argument")

    parser.add_argument('--arg5', default="a", choices=['a', 'b', 'c'], type=str,
        required=False, metavar='CHOICE', help="choice argument")

    args = parser.parse_args()

    print(args)
    print(args.arg1, args.arg2, args.arg3, args.arg4, args.arg5)

if __name__ == "__main__":
    main()
    