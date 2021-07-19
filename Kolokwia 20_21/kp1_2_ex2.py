# 5 pkt

def single_vowel(word):
    cnt = 0
    for let in word:
        if let in ["o", "a", "e", "u", "i", "y"]:
            cnt += 1
        if cnt > 1:
            return False

    if cnt == 1:
        return True
    return False


def rec_cut(word, cnt):
    if word == "":
        return False

    for i in range(len(word)):
        if single_vowel(word[:i]) and rec_cut(word[i:], cnt):
            cnt[0] += 1

    if single_vowel(word):
        return True


def cutting(s):
    cnt = [0]
    _ = rec_cut(s, cnt)
    return cnt[0]
