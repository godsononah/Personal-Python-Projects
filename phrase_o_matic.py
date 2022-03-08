import random

def main():
    wordlist1 = ["24/7", "multi-Tier", "30,000 foot", "B-to-B", "win-to-win", "front-end", "web-based", "pervasive", "smart", "six-sigma", "critical-path", "dynamic"]
    wordlist2 = ["empowered", "sticky", "value-added", "oriented", "centric", "distributed", "networked", "focused", "leveraged", "aligned", "targeted", "shared", "cooperative", "accelerated"]
    wordlist3 = ["process", "tipping-point", "solution", "architecture", "core competency", "strategy", "mindshare", "portal", "space", "vision", "paradigm", "mission"]

    while True:
        check = input('Do you want a phrase? ')
        if check.lower().startswith('y'):
            phrase = " ".join([random.choice(wordlist1), random.choice(wordlist2), random.choice(wordlist3)])
            print("What we need is a {}!".format(phrase))
        else:
            break
    
if __name__ == '__main__':
    main()