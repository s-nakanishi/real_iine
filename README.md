# リアル「いいね」ボタン

* amazon-dashのインストール

```
$ sudo pip3 install amazon-dash
```

* libdnetのインストール

```
brew install libdnet
```


* DASHボタンのMACアドレスを確認する

```
$ sudo amazon-dash discovery
```

* dashボタンのMACアドレス（ベンダー番号）

```
ac:63:be
```

* amazon-dash.xml作成

``` amazon-dash.xml
settings:
  delay: 10
devices:
  ac:63:be:bb:a9:47:
    name: group1
    user: shinya
    cmd: python /Users/shinya/work/python/dash/sample.py
```

* amazon-dash.xmlの所有者をrootに変更

```
$ sudo chown root amazon-dash.xml
```

* sample.pyの作成

``` sample.py
#! /Users/shinya/.pyenv/shims/python

print('Hello')
```

* 実行確認

```
$ sudo amazon-dash run
```

* DASHボタンを押す
