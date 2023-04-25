import sys

old_word = sys.argv[1]
new_word = sys.argv[2]
file_name = sys.argv[3]

with open(file_name, 'r', encoding='utf-8') as f:
    data = f.read()
    # 统计旧单词出现的次数
    word_count = data.count(old_word)

    # 替换旧单词为新单词
    data = data.replace(old_word, new_word)

    # 写入文件
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)

print(f'文件{file_name}中共有{word_count}个【{old_word}】,已经全部替换为【{new_word}】')
