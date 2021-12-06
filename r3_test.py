
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: # 文字檔檔頭若有怪符號或空格時 + sig 可以消除
    for line in f:
        lines.append(line.strip())      # .strip() 可刪除跳行符號


for line in lines:
    s = line.split(' ')         # .split() 把每一行用空格去切開,存成清單
    # 在 Python 裡 str 字串可以把它當作清單來看待
    time = s[0][:5]
    name = s[0][5:]
    print(time, name)
    # print(name)