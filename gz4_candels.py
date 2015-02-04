convert={
    ('candels-0','a-0'):1, ('candels-0','a-1'):2, ('candels-0','a-2'):3,
    ('candels-1','a-0'):4, ('candels-1','a-1'):5, ('candels-1','a-2'):6,
    ('candels-2','a-0'):7, ('candels-2','a-1'):8,
    ('candels-3','a-0'):9, ('candels-3','a-1'):10, ('candels-3','a-2'):11, ('candels-3','a-3'):12, ('candels-3','a-4'):13, ('candels-3','a-5'):14,
    ('candels-4','a-0'):15, ('candels-4','a-1'):16, ('candels-4','a-2'):17, ('candels-4','a-3'):18,
    ('candels-5','a-0'):19, ('candels-5','a-1'):20,
    ('candels-6','a-0'):21, ('candels-6','a-1'):22,
    ('candels-7','a-0'):23, ('candels-7','a-1'):24,
    ('candels-8','a-0'):25, ('candels-8','a-1'):26,
    ('candels-9','a-0'):27, ('candels-9','a-1'):28,
    ('candels-10','a-0'):29, ('candels-10','a-1'):30, #note: there is no 31
    ('candels-11','a-0'):32, ('candels-11','a-1'):33,
    ('candels-12','a-0'):34, ('candels-12','a-1'):35,
    ('candels-13','a-0'):36, ('candels-13','a-1'):37, ('candels-13','a-2'):38,
    ('candels-14','a-0'):39, ('candels-14','a-1'):40, ('candels-14','a-2'):41, ('candels-14','a-3'):42, ('candels-14','a-4'):43, ('candels-14','a-5'):44,
    ('candels-15','a-0'):45, ('candels-15','a-1'):46, ('candels-15','a-2'):47,
    'a-0':48, 'a-1':49, 'a-2':50, 'a-3':51,    
    ('candels-17','a-0'):-1, ('candels-17','a-1'):-1}

def valid_path(p):
    if (p[-1]!=-1) and (p[-1] not in [3,48,49,50,51]):
        return False
    l=len(p)
    valid=True
    for i in range(l-1):
        valid = (valid) and (p[i+1] in vp[p[i]])
        if not valid:
            return valid
    return valid

vp={
    -1:[-1],
    0: [1,2,3],
    1: [4,5,6],
    2: [7,8],
    3: [-1],
    4: [48,49,50,51,-1],
    5: [48,49,50,51,-1],
    6: [48,49,50,51,-1],
    7: [9,10,11,12,13,14],
    8: [27,28],
    9: [23,24],
    10: [19,20],
    11: [15,16,17,18],
    12: [15,16,17,18],
    13: [15,16,17,18],
    14: [15,16,17,18],
    15: [19,20],
    16: [19,20],
    17: [19,20],
    18: [19,20],
    19: [21,22],
    20: [23,24],
    21: [23,24],
    22: [48,49,50,51,-1],
    23: [25,26],
    24: [25,26],
    25: [48,49,50,51,-1],
    26: [48,49,50,51,-1],
    27: [29,30],
    28: [32,33],
    29: [48,49,50,51,-1],
    30: [48,49,50,51,-1],
    32: [34,35],
    33: [34,35],
    34: [36,37,38],
    35: [45,46,47],
    36: [39,40,41,42,43,44],
    37: [39,40,41,42,43,44],
    38: [39,40,41,42,43,44],
    39:[45,46,47],
    40:[45,46,47],
    41:[45,46,47],
    42:[45,46,47],
    43:[45,46,47],
    44:[45,46,47],
    45:[48,49,50,51,-1],
    46:[48,49,50,51,-1],
    47:[48,49,50,51,-1],
    48:[-1],
    49:[-1],
    50:[-1],
    51:[-1],
    52:[-1],
    53:[-1]}

nodes=[
    {"group": 0, "question": "", "name": "All", "answer_id": 0},
    {"group": 1, "question": "Is the galaxy simply smooth and rounded, with no sign of a disk?", "name": "Smooth", "answer_id": 1},
    {"group": 2, "question": "Is the galaxy simply smooth and rounded, with no sign of a disk?", "name": "Features or disk", "answer_id": 2},
    {"group": 5, "question": "Is the galaxy simply smooth and rounded, with no sign of a disk?", "name": "Star or artifact", "answer_id": 3},
    {"group": 1, "question": "How rounded is it?", "name": "Completely round", "answer_id": 4},
    {"group": 1, "question": "How rounded is it?", "name": "In between", "answer_id": 5},
    {"group": 1, "question": "How rounded is it?", "name": "Cigar shaped", "answer_id": 6},
    {"group": 4, "question": "Does the galaxy have a mostly clumpy appearance?", "name": "Yes", "answer_id": 7},
    {"group": 2, "question": "Does the galaxy have a mostly clumpy appearance?", "name": "No", "answer_id": 8},
    {"group": 4, "question": "How many clumps are there?", "name": "1", "answer_id": 9},
    {"group": 4, "question": "How many clumps are there?", "name": "2", "answer_id": 10},
    {"group": 4, "question": "How many clumps are there?", "name": "3", "answer_id": 11},
    {"group": 4, "question": "How many clumps are there?", "name": "4", "answer_id": 12},
    {"group": 4, "question": "How many clumps are there?", "name": "More than 4", "answer_id": 13},
    {"group": 4, "question": "How many clumps are there?", "name": "Can't tell", "answer_id": 14},
    {"group": 4, "question": "Do the clumps appear in a straight line, a chain, or a cluster?", "name": "Straight Line", "answer_id": 15},
    {"group": 4, "question": "Do the clumps appear in a straight line, a chain, or a cluster?", "name": "Chain", "answer_id": 16},
    {"group": 4, "question": "Do the clumps appear in a straight line, a chain, or a cluster?", "name": "Cluster", "answer_id": 17},
    {"group": 4, "question": "Do the clumps appear in a straight line, a chain, or a cluster?", "name": "Spiral", "answer_id": 18},
    {"group": 4, "question": "Is there one clump which is clearly brighter than the others?", "name": "Yes", "answer_id": 19},
    {"group": 4, "question": "Is there one clump which is clearly brighter than the others?", "name": "No", "answer_id": 20},
    {"group": 4, "question": "Is the brightest clump central to the galaxy?", "name": "Yes", "answer_id": 21},
    {"group": 4, "question": "Is the brightest clump central to the galaxy?", "name": "No", "answer_id": 22},
    {"group": 4, "question": "Does the galaxy appear symmetrical?", "name": "Yes", "answer_id": 23},
    {"group": 4, "question": "Does the galaxy appear symmetrical?", "name": "No", "answer_id": 24},
    {"group": 4, "question": "Do the clumps appear to be embedded within a larger object?", "name": "Yes", "answer_id": 25},
    {"group": 4, "question": "Do the clumps appear to be embedded within a larger object?", "name": "No", "answer_id": 26},
    {"group": 2, "question": "Could this be a disk viewed edge-on?", "name": "Yes", "answer_id": 27},
    {"group": 3, "question": "Could this be a disk viewed edge-on?", "name": "No", "answer_id": 28},
    {"group": 2, "question": "Does the galaxy have a bulge at its centre? If so, what shape?", "name": "Bulge", "answer_id": 29},
    {"group": 2, "question": "Does the galaxy have a bulge at its centre? If so, what shape?", "name": "No bulge", "answer_id": 30},
    {"group": 2, "question": "", "name": "", "answer_id": 31},    
    {"group": 3, "question": "Is there a sign of a bar feature through the centre of the galaxy?", "name": "Bar", "answer_id": 32},
    {"group": 3, "question": "Is there a sign of a bar feature through the centre of the galaxy?", "name": "No bar", "answer_id": 33},
    {"group": 3, "question": "Is there any sign of a spiral arm pattern?", "name": "Spiral", "answer_id": 34},
    {"group": 3, "question": "Is there any sign of a spiral arm pattern?", "name": "No spiral", "answer_id": 35},
    {"group": 3, "question": "How tightly wound do the spiral arms appear?", "name": "Tight", "answer_id": 36},
    {"group": 3, "question": "How tightly wound do the spiral arms appear?", "name": "Medium", "answer_id": 37},
    {"group": 3, "question": "How tightly wound do the spiral arms appear?", "name": "Loose", "answer_id": 38},
    {"group": 3, "question": "How many spiral arms are there?", "name": "1", "answer_id": 39},
    {"group": 3, "question": "How many spiral arms are there?", "name": "2", "answer_id": 40},
    {"group": 3, "question": "How many spiral arms are there?", "name": "3", "answer_id": 41},
    {"group": 3, "question": "How many spiral arms are there?", "name": "4", "answer_id": 42},
    {"group": 3, "question": "How many spiral arms are there?", "name": "More than 4", "answer_id": 43},
    {"group": 3, "question": "How many spiral arms are there?", "name": "Can't tell", "answer_id": 44},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "No bulge", "answer_id": 45},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "Obvious", "answer_id": 46},
    {"group": 3, "question": "How prominent is the central bulge, compared with the rest of the galaxy?", "name": "Dominant", "answer_id": 47},
    {"group": 6, "question": "Is the galaxy currently merging or is there any sign of tidal debris?", "name": "Merging", "answer_id": 48},
    {"group": 6, "question": "Is the galaxy currently merging or is there any sign of tidal debris?", "name": "Tidal debris", "answer_id": 49},
    {"group": 6, "question": "Is the galaxy currently merging or is there any sign of tidal debris?", "name": "Merging and debris", "answer_id": 50},
    {"group": 6, "question": "Is the galaxy currently merging or is there any sign of tidal debris?", "name": "Not merging and no debris", "answer_id": 51},
    {"group": 6, "question": "Would you like to discuss this object?", "name": "Yes", "answer_id": 52},
    {"group": 6, "question": "Would you like to discuss this object?", "name": "No", "answer_id": 53}]
