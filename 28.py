def correct(seq, rules):
    if len(seq) != 3:
        return False
    for ch, rule in zip(seq, rules):
        if ch[0] in ["O", "U"]:
            rules[1] = ["OU"]
        if ch[0] in ["M", "N", "P"]:
            rules[1] = ["MNP"]
        if ch not in rule:
            return False
    return seq[-1] not in seq[:-1]

if __name__ == "__main__":
    for s in ("NPO", "MUN", "ONP", "NON"):
        if correct(s, ["MNO", "NOP", "MNOPU"]):
            print(f" {s} правильно")
        else:
            print(f"{s} неправильно")
