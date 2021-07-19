jump_count = 0
for j in range(N):
    i = 0
    mode = 1
    while i < 3**N:
        jump = 3**jump_count
        for _ in range(jump):
            if mode == 1:
                mieszanka[i][j] = tab1[j]
            elif mode == 2:
                mieszanka[i][j] = tab2[j]
            else:
                mieszanka[i][j] = (tab1[j] + tab2[j])
            i += 1
        mode += 1
        if mode > 3:
            mode = 1
    jump_count += 1
