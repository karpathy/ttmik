# compile notes.md into cards.txt, ready to be imported into Anki
# only cards (of the form front=back) are compiled
# both directions are compiled, so front=back and back=front

import os
import re

# read the input markdown
in_path = "notes.md"
lines = open(in_path, 'r').readlines()
line_from = 0 # we may wish to filter which lines to compile
line_to = len(lines)

# output file
out_path = "cards.txt"
output = open(out_path, 'w')

# process all the lines
ncards = 0
for line in lines[line_from:line_to]:

    if not "=" in line:
        # only lines with = denote cards we want to compile
        continue
    
    # preprocessing
    sline = line
    # get rid of any romanization, which is inside square brackets
    sline = re.sub(r'\[.*?\]', '', sline)
    # strip any whitespace on both ends
    sline = sline.strip()
    
    # find either the = delimiter, and add both the front and back of the card
    parts = [p.strip() for p in sline.split('=')]
    assert len(parts) == 2, 'Invalid line: ' + line

    # write to output both the normal and reversed order
    output.write(parts[0] + ';' + parts[1] + '\n') # normal order
    output.write(parts[1] + ';' + parts[0] + '\n') # reversed order
    ncards += 2

print(ncards, 'cards compiled')
