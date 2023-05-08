#!/usr/bin/python3
""" Unlock boxes algorithm """


def canUnlockAll(boxes):
    """ A method to determine if all the boxes can be opened """
    num_boxes = len(boxes)
    available_keys = set([0])
    no_keys = set()
    count = 0

    if len(boxes) == 1:
        return True
    if len(boxes[0]) == 0:
        return False
    for key in boxes[0]:
        available_keys.add(key)

    for box_id, box in enumerate(boxes):
        if box_id in available_keys:
            count = count + 1
            [available_keys.add(key) for key in box]
        else:
            no_keys.add(box_id)
    for box_id in no_keys:
        if box_id in available_keys:
            [available_keys.add(key) for key in boxes[box_id]]
            count = count + 1
    if count == len(boxes):
        return True
    else:
        return False

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# canUnlockAll(boxes)
