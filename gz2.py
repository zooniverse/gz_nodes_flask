def valid_path(p):
        l=len(p)
        p2=p+[-1]
        valid=True
        for i in range(l):
            valid = (valid) and (p2[i+1] in vp[p2[i]])
            if not valid:
                return valid
        return valid

vp={0:[1,2,3],
    1:[16,17,18],
    2:[4,5],
    3:[-1],
    4:[25,26,27],
    5:[6,7],
    6:[8,9],
    7:[8,9],
    8:[28,29,30],
    9:[10,11,12,13],
    10:[14,15],
    11:[14,15],
    12:[14,15],
    13:[14,15],
    14:[19,20,21,22,23,24,38],
    15:[-1],
    16:[14,15],
    17:[14,15],
    18:[14,15],
    19:[-1,20,21,22,23,24,38],
    20:[-1,19,21,22,23,24,38],
    21:[-1,19,20,22,23,24,38],
    22:[-1,19,20,21,23,24,38],
    23:[-1,19,20,21,22,24,38],
    24:[-1,19,20,21,22,23,38],
    25:[14,15],
    26:[14,15],
    27:[14,15],
    28:[31,32,33,34,36,37],
    29:[31,32,33,34,36,37],
    30:[31,32,33,34,36,37],
    31:[10,11,12,13],
    32:[10,11,12,13],
    33:[10,11,12,13],
    34:[10,11,12,13],
    36:[10,11,12,13],
    37:[10,11,12,13],
    38:[-1,19,20,21,22,23,24]}

nodes=[
    {"group": 0, "question": "", "name": "All", "answer_id": 0},
    {"group": 1, "question": "Is the galaxy simply smooth and rounded, with no sign of a disk?", "name": "Smooth", "answer_id": 1},
    {"group": 2, "question": "Is the galaxy simply smooth and rounded, with no sign of a disk?", "name": "Features or disk", "answer_id": 2},
    {"group": 4, "question": "Is the galaxy simply smooth and rounded, with no sign of a disk?", "name": "Star or artifact", "answer_id": 3},
    {"group": 2, "question": "Could this be a disk viewed edge-on?", "name": "Yes", "answer_id": 4},
    {"group": 3, "question": "Could this be a disk viewed edge-on?", "name": "No", "answer_id": 5},
    {"group": 3, "question": "Is there a sign of a bar feature through the centre of the galaxy?", "name": "Bar", "answer_id": 6},
    {"group": 3, "question": "Is there a sign of a bar feature through the centre of the galaxy?", "name": "No bar", "answer_id": 7},
    {"group": 3, "question": "Is there any sign of a spiral arm pattern?", "name": "Spiral", "answer_id": 8},
    {"group": 3, "question": "Is there any sign of a spiral arm pattern?", "name": "No spiral", "answer_id": 9},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "No bulge", "answer_id": 10},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "Just noticeable", "answer_id": 11},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "Obvious", "answer_id": 12},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "Dominant", "answer_id": 13},
    {"group": 5, "question": "Is there anything odd?", "name": "Yes", "answer_id": 14},
    {"group": 5, "question": "Is there anything odd?", "name": "No", "answer_id": 15},
    {"group": 1, "question": "How rounded is it?", "name": "Completely round", "answer_id": 16},
    {"group": 1, "question": "How rounded is it?", "name": "In between", "answer_id": 17},
    {"group": 1, "question": "How rounded is it?", "name": "Cigar shaped", "answer_id": 18},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Ring", "answer_id": 19},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Lens or arc", "answer_id": 20},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Disturbed", "answer_id": 21},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Irregular", "answer_id": 22},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Other", "answer_id": 23},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Merger", "answer_id": 24},
    {"group": 2, "question": "Does the galaxy have a bulge at its centre? If so, what shape?", "name": "Rounded", "answer_id": 25},
    {"group": 2, "question": "Does the galaxy have a bulge at its centre? If so, what shape?", "name": "Boxy", "answer_id": 26},
    {"group": 2, "question": "Does the galaxy have a bulge at its centre? If so, what shape?", "name": "No bulge", "answer_id": 27},
    {"group": 3, "question": "How tightly wound do the spiral arms appear?", "name": "Tight", "answer_id": 28},
    {"group": 3, "question": "How tightly wound do the spiral arms appear?", "name": "Medium", "answer_id": 29},
    {"group": 3, "question": "How tightly wound do the spiral arms appear?", "name": "Loose", "answer_id": 30},
    {"group": 3, "question": "How many spiral arms are there?", "name": "1", "answer_id": 31},
    {"group": 3, "question": "How many spiral arms are there?", "name": "2", "answer_id": 32},
    {"group": 3, "question": "How many spiral arms are there?", "name": "3", "answer_id": 33},
    {"group": 3, "question": "How many spiral arms are there?", "name": "4", "answer_id": 34},
    {"answer": "", "group": -1, "question": "", "answer_id": 35},
    {"group": 3, "question": "How many spiral arms are there?", "name": "More than 4", "answer_id": 36},
    {"group": 3, "question": "How many spiral arms are there?", "name": "Can't tell", "answer_id": 37},
    {"group": 5, "question": "Is the odd feature a ring, or is the galaxy disturbed or irregular?", "name": "Dust lane", "answer_id": 38}]