# 1 venvによる仮想環境

* 仮想環境の作成
```sh
pwd
ls
cd <working directory>
python3 -m venv venv (python3 -m venv 仮想環境名)
```

* 仮想環境に移動
```sh
source venv/bin/activate (source 仮想環境名/bin/activate)
```

* ライブラリのインストール
```sh
python3 -m pip install --upgrade pip
pip3 install click
pip3 install black
pip3 install mypy
```

* requirements.txt
```sh
pip3 freeze
pip3 freeze > requirements.txt
# pip3 install -r requirements.txt
```

* 確認
```sh
python3 -c "import click"
```

* 環境離脱、最activate
```sh
deactivate
# rm -rf venv
source venv/bin/activate
```

* black, mypy
```sh
python3 -m black 6_clean_code/6_1_black_before.py
python3 -m mypy 6_clean_code/6_3_static.py
```