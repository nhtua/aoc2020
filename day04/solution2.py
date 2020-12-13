import re

def checkHeight(h):
    if "cm" in h:
        return 150 <= int(h.replace("cm","")) <= 193
    if "in" in h:
        return 59 <= int(h.replace("in","")) <= 76
    return False

def str_to_person(s):
    s = s.replace('\n',' ')
    attr = filter(None, s.split(' '))
    p = {}
    for x in attr:
        k,v = x.split(":")
        p[k] = v
    if 'cid' not in p:
        p['cid'] = None
    return p


def validate_person(p, vf):
    if set(p.keys()) != set(vf.keys()):
        return False
    for k in p:
        if not vf[k](p[k]):
            return False
    return True


valid_fields2 = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": checkHeight,
    "hcl": lambda x: re.match(r'^#[\da-f]{6}$',x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: re.match(r'^\d{9}$',x),
    "cid": lambda x: True
}

def count2(data, vf=valid_fields2):
    total = 0
    p = ""
    for l in data:
        if l.strip() !=  "":
            p += " "+l
        else:
            person = str_to_person(p)
            if validate_person(person, vf):
                total += 1
            p=""
    return total


if __name__ == '__main__':
    lines = open('input.txt', 'r').readlines()
    print('Total valid passport is ', count2(lines))
