from pprint import pprint

def parse(inp):
    foods = []

    for line in inp.splitlines():
        a_idx = line.find('(')
        ingrs = line[:a_idx-1].split()
        allergs = line[a_idx+10:-1].split(', ')
        foods.append( (ingrs, allergs) )
    return foods

def check_labels(foods):
    ingredients = set()
    allergens = dict()
    for ingrs, allergs in foods:
        ingredients |= set(ingrs)
        for a in allergs:
            if a not in allergens:
                allergens[a] = set(ingrs)
            else:
                allergens[a] &= set(ingrs)
    return ingredients, allergens


def part1(inp):
    foods = parse(inp)
    ingredients, allergens = check_labels(foods)

    unsafe = set(ingr for ingrs in allergens.values() for ingr in ingrs)
    safe   = ingredients - unsafe

    total = 0
    for ingrs, _ in foods:
        total += sum(ingr in safe for ingr in ingrs)
    return total


def part2(inp):
    foods = parse(inp)
    _, allergens = check_labels(foods)

    unsafe = dict()
    while allergens:
        allerg, ingrs = min(allergens.items(), key=lambda x:len(x[1]))
        ingr = next(iter(ingrs))
        unsafe[ingr] = allerg
        del allergens[allerg]
        for k in allergens:
            allergens[k].discard(ingr)

    return ','.join(x[0] for x in sorted(unsafe.items(), key=lambda x:x[1]))
