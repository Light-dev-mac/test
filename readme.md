# Pythonテスト

本問題はpythonの基本文法とアルゴリズムを問うコーディング演習である。以下の「問題」と「解答の提出」をよく読んで、解答してください。

制限時間はありませんが、解答時間は採点の基準の一つになります。提出gitの最終commit時間を解答終了時間として採点致しますので、最終提出後は変更のないようご注意ください。

## 問題

FizzBuzzというプログラムは、3の倍数が入力されると”Fizz”を出力し、5の倍数が入力されると”Buzz”を出力し、3の倍数でも5の倍数でもある数が入力されると”FizzBuzz”を出力します

FizzBuzzの拡張として、複数の(整数i , 文字列s)のペアと一つの整数$m$が渡され、mがiの倍数ならsを出力するプログラムを作成しなさい

- sはiの小さい順に出力してください(※iが小さい順に並んでいるとは限りません)
- どのsも出力されなければmを出力してください
- iとsのペアは"input.txt"に一行ずつ"i:s"形式で渡されます
- mは"input.txt"の下から２番目の行で渡されます
- "input.txt"の最終行は空行です

## 解答の提出

- 回答のプログラムは"test.py"に実行できる状態で書いてください
- 回答を任意の公開gitレポジトリにプッシュしてください（githubでもかまいません）
- 以下のリンクにある回答提出フォームに従い、"input.txt"に対するプログラムの出力とgitリポジトリのurlを提出してください。https://forms.gle/8kRiQAp5KLH1dLRCA

## 入力例と出力例

### 例1

入力

```txt:input.txt
5:buzz
3:fizz
8:hoge
2:huga
24

```

出力

hugafizzhoge

### 例2

入力

```txt:input.txt
3:yoshida
5:takuma
2

```

出力

2
