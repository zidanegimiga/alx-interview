# Lockboxes

You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n-1 and each box contains keys to the other boxes.
1. A key with the same number as the box opens that box.
2. There can be keys that do not have boxes.
3. A box may be empty i.e., not have any keys at all.

The first box is already unlocked.
Given a certain set of boxes, write a function that determines if all the boxes can be opened.
Function Prototype:
` def canUnlockAll(boxes)`

where boxes is a list of lists
