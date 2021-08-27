"""
セイウチ演算子
変数の代入と使用を同時に実行できる
"""

# nに10を代入するのとn>5の比較を同時に実行している
if (n := 10) > 5:
    print("test")

# よく使うパターンは、while文で使用する


n = 0
while (n := n + 1) < 10:
    print(n)

# セイウチを使用しなかった場合
n = 1
while n < 10:
    print(n)
    n + 1

