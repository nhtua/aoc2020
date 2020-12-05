from solution import *

def test_01():
    input= [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        ""
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
        ""
    ]
    expect = 2
    assert count_valid_passport(input) == expect

def test_02():
    input = [
        "aa:123 bb:32 cc:sfsdf", # no new line
    ]
    fields = ["aa","bb"]
    assert count_valid_passport(input, fields) == 0

def test_02b():
    input = [
        "aa:123 bb:32 cc:sfsdf",
        "",
        "aa:123 bb:32 cc:sfsdf",
        ""
    ]
    fields = ["aa","bb"]
    assert count_valid_passport(input, fields) == 2

def test_03():
    input = [
        "aa:123 bb:32 cc:sfsdf",
        "",
        "aa:123 bb:23432",
        ""
    ]
    fields = ["aa","bb"]
    assert count_valid_passport(input, fields) == 2

def test_04():
    input = [
        "aa:123 bb:32 cc:sfsdf",
        "",
        "aa:123 bb:23432",
        ""
    ]
    fields = ["aa","cc"]
    assert count_valid_passport(input, fields) == 1

def test_05():
    input = [
        "xx:aa zz:bb",
        ""
    ]
    fields = ["aa","bb"]
    assert count_valid_passport(input, fields) == 0
