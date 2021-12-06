import os # operation system

#讀取檔案

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())  # .strip() 去除換行符號
    return lines   


def convert(lines):
    new = []
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen 說了：', allen_word_count, '個字') 
    print('Allen 傳了：', allen_sticker_count, '則貼圖') 
    print('Allen 傳了：', allen_image_count, '張貼圖')            
    print('Viki 說了：', viki_word_count, '個字') 
    print('Viki 傳了：', viki_sticker_count, '則貼圖')
    print('Viki 傳了：', viki_image_count, '張貼圖')
        # print(s)
    return new


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output2.txt', lines)


main()