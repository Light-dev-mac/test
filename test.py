"""
このファイルに解答コードを書いてください
"""



f =  open('input.txt', "rt")
str_text = f.read()
str_text_lines = str_text.split('\n')
m = int(str_text_lines[-2])
pairs = str_text_lines[:-2]
dict_pairs = {}

for pair in pairs:
    i, s  = pair.split(':')
    dict_pairs[int(i)] = s

dict_pairs = sorted(dict_pairs.items())
is_matched = False
for pair in dict_pairs:
    i, s = pair
    if m % i == 0:
        is_matched = True
        print(s, end='')

if not is_matched:
    print(m)