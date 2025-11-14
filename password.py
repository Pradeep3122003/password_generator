import random, sys, pathlib, gzip

def gz_wordlist(path):
    p = pathlib.Path(path)
    if not p.exists():
        return []

    with gzip.open(p, "rt", encoding="utf-8", errors="ignore") as f:
        return [w.strip() for w in f.readlines() if w.strip().isalpha()]

def word(wordlist):
    if not wordlist:
        return ""
    return random.choice(wordlist)


def number(seed):
    return random.randint(2, seed)

def generate(wordlist):
    password = ""
    length = random.randint(3, 8)

    for _ in range(length):
        toss = random.randint(0, 3)

        if toss == 0 or toss == 1:
            password += word(wordlist)
        else:
            password += str(number(3333))

    return password


if __name__ == "__main__":
    words = gz_wordlist("./source/words.txt.gz")

    if len(sys.argv) > 1:
        maxlen = int(sys.argv[1])
    else:
        maxlen = 0

    password = generate(words)

    if maxlen > 1:
        password = password[:maxlen]

    print("password:", password)
