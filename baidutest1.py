# 现在给你一段英文短文，请统计出现次数最多的单词，输出该单词和出现次数。注意：在统计时不需要区分单词的大小写。

# 如果存在两个或多个高频词的出现次数一样，则输出字典序最小的词和出现次数。

# 如果一个单词在短文中存在多种不同的大小写形式，请以第一次出现的形式为准。
def highFrequency(sent):
    if not sent:
        print("  0")
    sent = sent.split(" ")
    freq = {}
    origin = {}
    cur_best = None
    for word in sent:
        orig = ""
        for c in word:
            if c.isalpha():
                orig += c
        
        word = orig.lower()
        if word not in origin:
            origin[word] = orig
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
        if not cur_best or freq[word] > freq[cur_best]:
            cur_best = word
        elif freq[word] == freq[cur_best] and word<cur_best:
            cur_best = word
    
    print(origin[cur_best] + " " + str(freq[cur_best]))

if __name__ == "__main__":
    # five five abc abc ........             
    sent = input()
    clean = ""
    for c in sent:
        if c.isalpha() or c == " ":
            clean += c
    import re
    clean = re.sub(" +", " ", clean)
    highFrequency(clean.strip())

'''
Five Little Monkeys Jumping on the Bed. It was bedtime. So five little monkeys took a bath. Five little Monkeys put on their pajamas.

Five 3
'''