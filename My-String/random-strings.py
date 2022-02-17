import random

# ---------------------------------------------------------------------#
def random_sentence(total=10):
    sentence = ''
    lines = open('/usr/share/dict/words').read().splitlines()

    for a in range(total):
        line = random.choice(lines)
        sentence = sentence + " " + line

    return sentence


# ---------------------------------------------------------------------#
if __name__ == "__main__":
    print(random_sentence(5))
