import os

list_content = []
with open(r'sorted\1.txt', encoding='utf8') as f:
    content_1 = f.readlines()
    list_content.append(content_1)
with open(r'sorted\2.txt', 'rt', encoding='utf8') as f:
    content_2 = f.readlines()
    list_content.append(content_2)
with open(r'sorted\3.txt', 'rt', encoding='utf8') as f:
    content_3 = f.readlines()
    list_content.append(content_3)

file_names = os.listdir(r'C:/Users/ВладОкс/Desktop/НЕТОЛОГИЯ практики/work with files/sorted')
files = dict(zip(file_names, list_content))
len_files = {}
for key, val in files.items():
    len_files[key] = len(val)

with open('result_file', 'w', encoding='utf8') as f:
    while len_files:
        min_count_lines = min(len_files, key=len_files.get)
        res = f'{min_count_lines}\n{len_files[min_count_lines]}\n{"".join(files[min_count_lines]).strip()}\n'
        f.writelines(res)
        len_files.pop(min_count_lines)
