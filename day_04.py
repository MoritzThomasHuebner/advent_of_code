from copy import deepcopy

lines = []
with open('day_04_input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))

passports = []

passport = dict()
for line in lines:
    if line == '':
        passports.append(deepcopy(passport))
        passport = dict()
        continue
    entries = line.strip('\n').split(' ')
    for entry in entries:
        entry_key_value = entry.split(':')
        passport[entry_key_value[0]] = entry_key_value[1]

passports.append(passport)


passport_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
optional_keys = {'cid'}
required_keys = passport_keys.difference(optional_keys)

# Part 1
n_valid = 0
for passport in passports:
    keys = set(passport.keys())
    if required_keys.issubset(keys):
        n_valid += 1
print(n_valid)

# Part 2

n_valid = 0
for passport in passports:
    keys = set(passport.keys())
    if not required_keys.issubset(keys):
        continue
    if not 1920 <= int(passport['byr']) <= 2002:
        continue
    if not 2010 <= int(passport['iyr']) <= 2020:
        continue
    if not 2020 <= int(passport['eyr']) <= 2030:
        continue

    if passport['hgt'].endswith('cm'):
        if not 150 <= int(passport['hgt'].strip('cm')) <= 193:
            continue
    elif passport['hgt'].endswith('in'):
        if not 59 <= int(passport['hgt'].strip('in')) <= 76:
            continue
    else:
        continue

    if not passport['hcl'].startswith('#') or not len(passport['hcl']) or not passport['hcl'][1:].isalnum():
        continue
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue
    if not passport['pid'].isnumeric() or not len(passport['pid']) == 9:
        continue
    n_valid += 1

print(n_valid)
