import collections

family = [('bob', 'mary'), ('bob', 'tom'), ('bob', 'judy'), ('alice', 'mary'),
          ('alice', 'tom'), ('alice', 'judy'), ('renee', 'rob'), ('renee', 'bob'),
          ('sid', 'rob'), ('sid', 'bob'), ('tom', 'ken'), ('ken', 'suzan'), ('rob', 'jim')]


######################################################################

def family_tree(druzina):
    druzinsko_drevo = collections.defaultdict(list)
    for stars, otrok in druzina:
        druzinsko_drevo[stars].append(otrok)
    return druzinsko_drevo


print(family_tree(family))

fm_tree = family_tree(family)


######################################################################

def children(tree, name):
    if name in tree:
        return tree[name]
    return []


def children_get(tree, name):
    return tree.get(name, [])


print(children_get(fm_tree, 'tom'))


######################################################################

def grandchildren(tree, name):
    names = []
    for child in children_get(tree, name):
        for grandchild in children_get(tree, child):
            names.append(grandchild)
    return names


def grandchildren_extend(tree, name):
    names = []
    for child in children(tree, name):
        names.extend(children(tree, child))
    return names


######################################################################


def successors(tree, name):
    names = []
    for child in children(tree, name):
        names.append(child)
        names.extend(successors(tree, child))
    return names


print(successors(fm_tree, 'bob'))


######################################################################
