def correct(seq, rules):
    if len(seq) != 3:
        return False
    for ch, rule in zip(seq, rules):
        if ch[0] in ["A", "E"]:
            rules[1] = ["BCD"]
        if ch not in rule:
            return False
    return seq[-1] not in seq[:-1]

if __name__ == "__main__":
    for s in ("BCA", "AEC", "BAD", "DED"):
        if correct(s, ["ABD", "AE", "ACD"]):
            print(f" {s} правильно")
        else:
            print(f"{s} неправильно")
