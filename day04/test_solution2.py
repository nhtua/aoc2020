from solution2 import *

def test_byr():
    assert valid_fields2['byr'](1919) == False
    assert valid_fields2['byr'](2003) == False
    assert valid_fields2['byr'](1920) == True
    assert valid_fields2['byr'](1980) == True
    assert valid_fields2['byr'](2002) == True

def test_height():
    assert checkHeight("149cm") == False
    assert checkHeight("194cm") == False
    assert checkHeight("150cm") == True
    assert checkHeight("160cm") == True
    assert checkHeight("193cm") == True

    assert checkHeight("58in") == False
    assert checkHeight("77in") == False
    assert checkHeight("59in") == True
    assert checkHeight("70in") == True
    assert checkHeight("76in") == True

def test_person():
    p = dict(pid="087499704", hgt="74in", ecl="grn", iyr="2012", eyr="2030", byr="1980", hcl="#623a2f")
    assert validate_person(p, valid_fields2) == True

    p = dict(eyr=1972, cid=100, hcl="#18171d", ecl="amb", hgt="170", pid="186cm", iyr="2018", byr="1926")
    assert validate_person(p, valid_fields2) == False

def test_str_person():
    s = """eyr:1972 cid:100

        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
        """
    p = str_to_person(s)
    assert '' not in p
    assert ' ' not in p
    assert 'eyr' in p
    assert 'cid' in p
    assert 'hcl' in p
    assert 'ecl' in p
    assert 'hgt' in p
    assert 'pid' in p
    assert 'iyr' in p
    assert 'byr' in p
