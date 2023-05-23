# basically we want to reverse all the cards too, before we import to anki
# so e.g. we don't import level1.txt, but level1_compiled.txt, the output of this script
# we also do some basic error checking, like making sure there's only one = delimiter

# input output
lines = open('level1.txt', 'r').readlines()
output = open('level1_compiled.txt', 'w')

# process all the lines
ncards = 0
for line in lines:

    # next line, strip any whitespace on both ends
    sline = line.strip()

    # skip empty lines
    if len(sline) == 0:
        continue

    # preserve comments
    if sline[0] == '#':
        output.write(line)
        continue

    # find either the = delimiter, and add both the front and back of the card
    parts = [p.strip() for p in sline.split('=')]
    assert len(parts) == 2, 'Invalid line: ' + line

    # write to output both the normal and reversed order
    output.write(parts[0] + ';' + parts[1] + '\n') # normal order
    output.write(parts[1] + ';' + parts[0] + '\n') # reversed order
    ncards += 2

print(ncards, 'cards compiled')
