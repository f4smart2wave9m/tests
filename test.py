#行数カウント
line_num = sum([1 for _ in open("input.txt")])

#ファイルを開く
file = open("input.txt", 'rt')

lines = file.readlines()

# 整数と文字のリストを作る
lists = []
for i in range(0, line_num):
    lists.append(lines[i].split(":"))

#文字列を整数にし，\nを剥ぐ
for i in range(0, line_num-1):
    number = int(lists[i][0])
    lists[i][0] = number
    moji = lists[i][1]
    lists[i][1] = moji[:-1]

#入力文字を取得
input = int(lists.pop(-1)[0])
#整数と文字列のリストをソート
lists.sort()

#実質的なFizzBuzz
output = ''
count = 0
for  key in lists:
    if (input % key[0] == 0):
        output += key[1]
        count +=1
    #一つも割り切れなければcount = 0
if (count > 0):
    print(output)
else:
    print(input)