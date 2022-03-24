def fun(seq, rules):
    if len(seq) != 3:
        return False
    for ch, rule in zip(seq, rules):
        if ch not in rule:
            return False
    return seq[-1] not in seq[:-1]

if __name__ == "__main__":
    for s in ("ГВБ", "БАГ", "АББ", "ВГБ"):
        if fun(s, ("АВГ", "АБВ", "БВГ")):
            print(f" {s} правильно")
        else:
            print(f"{s} неправильно")
