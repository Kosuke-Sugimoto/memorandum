import time
import tqdm


# 通常のtqdm
for _ in tqdm.tqdm(range(100), desc="sample"):
    time.sleep(0.01)


# ネスト構造でのtqdm
for i in tqdm.trange(3, desc="first"):
    s = "second-{}".format(i)
    for _ in tqdm.trange(100, desc=s):
        time.sleep(0.01)


# tqdmの各引数について
"""
    使用例：
        tqdm(iterable=None, desc=None, total=None, leave=True, file=None, ncols=None, mininterval=0.1,
        maxinterval=10.0, miniters=None, ascii=None, disable=False, unit='it', unit_scale=False, dynamic_ncols=False,
        smoothing=0.3, bar_format=None, initial=0, position=None, postfix=None, unit_divisor=1000)

    説明：
        iterable: プログレスバーの進捗表示に使うiter型のオブジェクト
        desc: 見出し
        total: iterableの最大値、指定されなければlen(iterable)が使われる
        leave: プログレスバーを出力された後も表示し続けるかどうか、デフォルトはTrue
        file: プログレスバーの出力をどこに書き込むか、io.TextIOWrapperかio.StringIOを引数として受け付ける
        ncols: 出力の幅、指定されなければ環境を勝手に読み込み、それにあった幅にしてくれる
        mininterval: プログレスバーを更新する最小の間隔、デフォルトは0.1
        maxinterval: プログレスバーを更新する最大の感覚、デフォルトは10 
        miniters: プログレスバーの表示を何回に1回更新するのか、その回数を表す、デフォルトは1
        ascii: プログレスバーの表示の埋め方、ascii="#"とやってやればプログレスバーがそれで埋まる(jupyterでなければ)
        disable: プログレスバーを処理中でも見えなくするか否か、デフォルトは勿論False
        unit: そのイテレーションにおける単位、デフォルトは"it"
        unit_scale: 上記のunitにキロやメガなどの単位を自動でつけるかどうか、デフォルトはFalse、Trueか1で動作する
        dynamic_ncols: 指定すると定期的にncolsとnrowsに従って変えてくれる、デフォルトはFalse
        smoothing: 推定終了時刻に関連？、maxが1であり、おそらくmaxの場合はその時点での速度のみ考慮し推定終了時刻を計算する
        bar_format: プログレスバーの表示の仕方、例えば"desc":100%とかを編集可能、デフォルトは\[{l_bar}{bar}{r_bar}\]
        initial: プログレスバーの進捗の初期値、再開する際に利用できる、デフォルトは勿論0
        position: 出力されるプログレスバーを何行目に出力するかを表す、notebookだと一つしか表示されないので関係なし
        postfix: descの逆、情報を後置する、つまりsuffixのこと、文字列型とか色々受け取れそう
        unit_divisor: unit_scaleがTrueのとき、単位をつける幅を指定する、キロとかは1000だが、10000とか大きく指定できる

"""

# 自力での実装に使える知識
"""
    pythonの標準出力は改行を認識すると、改竄権？を手放すらしい
    これを利用すれば実装は多分可能
    下の実装では"\r"と引数で指定することにより、現在編集している行の先頭に戻り、end=""と指定することによってデフォルトで末尾に入っている、改行の命令である"\n"を打ち消している。
    改行命令がないため、同じ行を編集し続けることが可能
"""
for i in range(100):
    time.sleep(0.5)
    print("\r", i, end="")


# DataLoaderに適用する際の注意点
# DataLoaderはiteratorではないので、何らかの方法でiteratorにする必要がある
# 例：tdqm(enumrate(data_loader), total=len(data_loader))