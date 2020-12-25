def parse(inp):
    lines = inp.splitlines()
    return int(lines[0]), int(lines[1])

def transform(val, subj_num):
    return (val * subj_num) % 20201227

def part1(inp):
    pub_card, pub_door = parse(inp)

    subj_num = 7
    loop_cnt = 0
    val = 1

    while val != pub_card and val != pub_door:
        val = transform(val, subj_num)
        loop_cnt += 1

    if val == pub_card:
        subj_num = pub_door
    else:
        sub_num = pub_door

    enc_key = 1
    for _ in range(loop_cnt):
        enc_key = transform(enc_key, subj_num)

    return enc_key
