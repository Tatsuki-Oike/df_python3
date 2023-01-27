# 成功
try:
    print("Hello")
except:
    print("ERROR")

# exceptの実行
try:
    print(Hello)
except:
    print("ERROR")

# exceptのエラー指定
try:
    print(Hello)
except NameError:
    print("存在しない変数です")

# 複数のエラー指定
try:
    print(Hello)
except IndexError:
    print("存在しないIndexです")
except NameError:
    print("存在しない変数です")