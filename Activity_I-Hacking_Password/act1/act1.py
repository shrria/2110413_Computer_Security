import hashlib

def sha1hash(word: str) -> str:
    return hashlib.sha1(word.encode('utf-8')).hexdigest()

def md5hash(word: str) -> str:
    return hashlib.md5(word.encode('utf-8')).hexdigest()

def every_possible_from_word(word: str) -> set:
    if len(word) == 0:
        return set()
    elif len(word) == 1:
        return { word.upper(), word.lower() }
    else:
        ch = word[0:1]
        s = set()
        words = every_possible_from_word(word[1:])
        for w in words:
            s.add(ch.upper() + w)
            s.add(ch.lower() + w)
            if ch.lower() == "o":
                s.add("0" + w)
            elif ch.lower() == 'l':
                s.add("1" + w)
            elif ch.lower() == 'i':
                s.add("1" + w)
            elif ch.lower() == '0':
                s.add("o" + w)
                s.add("O" + w)
            elif ch.lower() == '1':
                s.add("l" + w)
                s.add("i" + w)
                s.add("L" + w)
                s.add("I" + w)
        return s

def prob1() -> None:
    prob1str = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"

    fp = open("10k-most-common.txt", "r")
    done = False

    for line in fp:
        if done:
            break
        s = line.strip()
        li = list(every_possible_from_word(s))
        for word in li:
            if done:
                break
            sha1 = sha1hash(word)
            md5 = md5hash(word)
            if sha1 == prob1str:
                print(word, "in sha1")
                done = True
            elif md5 == prob1str:
                print(word, "in md5")
                done = True
            

    fp.close()
    pass

def prob2() -> None:
    fp = open("10k-most-common.txt", "r")
    rt = open("sha1-rainbow-table.txt", "w")
    
    for line in fp:
        s = line.strip()
        li = list(every_possible_from_word(s))
        for word in li:
            rt.write(sha1hash(word) + " " + word + "\n")
    
    fp.close()
    rt.close()
    pass

def prob3() -> None:
    for i in range(1000000):
        p = sha1hash("password")

# prob1()
# prob2()
# Problem 2 Measure: 2.72s user 0.08s system 98% cpu 2.845 total
# prob3()
# 0.54s user 0.01s system 99% cpu 0.555 total
