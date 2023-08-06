def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    min_raiting = ratings[0]
    min_raiting_p = 0
    for i, r in enumerate(ratings):
        if r == 0:
            min_raiting_p = i
            break

        if r < min_raiting:
            min_raiting_p = i
            min_raiting = r

    p = min_raiting_p
    cnt_candy = 1
    total_cnt_candy = 0
    l = len(ratings)
    while True:
        if p == 0 and p == l - 1:
            p_prev = 0
            p_next = 0
        elif p == 0:
            p_prev = -1
            p_next = p + 1
        elif p == l - 1:
            p_prev = p - 1
            p_next = 0
        else:
            p_prev = p - 1
            p_next = p + 1

        if ratings[p] < ratings[p_prev] and ratings[p] < ratings[p_next]:
            cnt_candy = 1
        else:
            if p_next == min_raiting_p:
                cnt_candy = max(ratings[p_prev], 1) + 1
            else:
                cnt_candy += 1

        total_cnt_candy += cnt_candy
        p = (p + 1) % l

        if p_next == min_raiting_p:
            break

    return total_cnt_candy



print(candy([1,0,2]))