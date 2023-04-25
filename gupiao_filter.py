list1 = ['万','亿', '损']
list2 = []
with open("gupiao2.txt", "r", encoding='utf-8') as f:
    gupiao = f.readlines()
    list2.append(gupiao)

g = open("gupiao3.txt", "a", encoding='utf-8')
g.write(str(list2[0]).replace('\n', '').strip())
# g.write(str(list2[1]))

# for gupiao1 in list2:
#     if gupiao1[0] not in list1:
#         print(gupiao1[0])
#         gupiao1.replace('\n', '').strip()
#         g.write(gupiao)
#     else:
#         print(2)
#         num = len(gupiao)
#         print(num)
#         g.seek(num - 1)
#         print(g.tell())
#         g.write(gupiao)



    #
    #     line = line.strip().split('\n')
    #     list1.append(line)
    # print(list1)
    # print(list1[1][0][0])
    # print(list1[0])
    # print(list1[1])
    # new_list = str(list1[0])+str(list1[1])
    # print(new_list)
    #
    # if list1[1][0][0] == '万' or list1[1][0][0] == '亿' or list1[1][0][0] == '损':
    #     new_list = list1[0].extend(list1[1])
    #     # print(new_list)
    #     # list2.append()
    #     # print(list2)