import random, sys, pathlib
from collections import defaultdict

def system_wordlist(path="/usr/share/dict/words"):
    p = pathlib.Path(path)
    if not p.exists():
        return []
    return [w.strip() for w in p.read_text(encoding="utf-8", errors="ignore").splitlines() if w.strip().isalpha()]

def word(wordlist):
    if not wordlist:
        return None
    return random.choice(wordlist)

def number(seed):
 return random.randint(2,seed)

def generate():
  sys_words = system_wordlist()
  password=""
  length=random.randint(3,8)
  for i in range(length):
    toss=random.randint(0,3)
    if toss==0 or toss==1:
      password+=word(sys_words)
    else:
      password+=str(number(3333))

  return password

if __name__ == "__main__":
    if len(sys.argv) > 1:
      length = int(sys.argv[1])
    else:
      length = 0
    password=generate()
    if length>1:
     password=password[:length]
    print("password: "+password)
