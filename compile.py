# basically we want to reverse all the cards too, before we import to anki
# so e.g. we don't import level1.txt, but level1_compiled.txt, the output of this script
# we also do some basic error checking, like making sure there's only one = delimiter

import os

# output directory
in_dir = 'cards'
out_dir = 'compiled'
os.makedirs(out_dir, exist_ok=True)

# get all the sections from cards/
sections = os.listdir(in_dir)

for section in sections:

    in_path = os.path.join(in_dir, section)
    out_path = os.path.join(out_dir, section)

    lines = open(in_path, 'r').readlines()
    output = open(out_path, 'w')

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

    print(section, ncards, 'cards compiled')
