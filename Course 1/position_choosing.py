npd = input().split() 
n = int(npd[0])  # 總共有 n 個城鎮
p = int(npd[1])  # 選出 p 個城鎮設基地台
d = int(npd[2])  # 基地台半徑 d 公里

data = []
for i in range(n):
    data.append(input().split())
    for j in range(3):
        data[i][j] = int(data[i][j])

town_list = []
for i in range(n):
    town_list.append(i)

if 2 <= n <= 1000 and 2 <= p <= n:
    total_cover_num = 0
    towns = []
    for base_stand in range(p):
        cover_num = 0
        for i in town_list:
            cover_num_tmp = 0
            cover_stand_tmp = []
            x = data[i][0]
            y = data[i][1]
            num = data[i][2]
            for j in town_list:
                x_cmp = data[j][0]
                y_cmp = data[j][1]
                num_cmp = data[j][2]
                dis = ((x - x_cmp)**2 + (y - y_cmp)**2)**(1/2)
                if dis <= d:
                    cover_num_tmp += num_cmp
                    cover_stand_tmp.append(j)
            if cover_num_tmp > cover_num:
                cover_stand = []
                cover_num = cover_num_tmp
                stand_set = i
                for c in cover_stand_tmp:
                    cover_stand.append(c)
        # print("----")
        # print(stand_set, cover_stand, cover_num)
        towns.append(stand_set+1)
        total_cover_num += cover_num
        if cover_num != []:
            for c in cover_stand:
                town_list.remove(c)
        # print(stand_set, total_cover_num)
        # print("-------------------------------------")
    for t in towns:
        print(t, end=" ")
    print(total_cover_num)