lines = open('input.txt', 'r').readlines()

valid_fields = [
    "byr", #(Birth Year)
    "iyr", #(Issue Year)
    "eyr", #(Expiration Year)
    "hgt", #(Height)
    "hcl", #(Hair Color)
    "ecl", #(Eye Color)
    "pid", #(Passport ID)
    #"cid", #(Country ID)
]

def count_valid_passport(data, vf=valid_fields):
    invalid = 0
    total = 0
    p = ""
    for l in data:
        if l.strip() !=  "":
            p += l
        else:
            for f in vf:
                if (f+":") not in p:
                    invalid = invalid + 1
            p=""
            total = total + 1
    return total - invalid


if __name__ == '__main__':
    print('Total valid passport is ', count_valid_passport(lines))
