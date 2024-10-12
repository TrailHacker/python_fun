class ItemList:
    items: []
    index: 0

    def __init__(self, items):
        self.index = 0
        self.items = items

    def next(self):
        result = self.items[self.index]
        self.index += 1
        return result

# APP STARTS HERE!
# ---------------

# define the triangle sides of the following:
#         1
#       2   3
#     4   5   6
#   7   8   9   10
# 11  12  13  14  15
rack_sides = [] # top left / bottom / top-right
rack_sides.append(ItemList([1, 2, 4, 7, 8]))
rack_sides.append(ItemList([11, 12, 13, 14, 9]))
rack_sides.append(ItemList([15, 10, 6, 3, 5]))

# define the different player's range of balls:
# player 1 has balls 1 - 5
# player 2 has balls 6 - 10
# player 3 has balls 11 - 15
ball_groups = [] # 1-5, 6-10, 11-15
ball_groups.append(ItemList([1, 2, 3, 4, 5]))
ball_groups.append(ItemList([6, 7, 8, 9, 10]))
ball_groups.append(ItemList([11, 12, 13, 14, 15]))

# setup counters for algorithm 
corners = len(rack_sides)
rack_side_index = 0
ball_group_index = 0
counter = 0
result = {}

# go through each ball 1 - 15 and place it 
# somewhere in the triangle indexed by the
# `rack_sides` definition above...
for i in range(15):

    # get the next ball number and next rack-side index
    ball = ball_groups[ball_group_index].next()
    index = rack_sides[rack_side_index].next()

    # position the ball inside the triangle
    result[index] = ball # e.g. ball #6 @ position 11 (see above triangle graph)

    # prepare for the next iteration
    rack_side_index += 1
    ball_group_index += 1
    counter += 1

    # if we just did a full iteration, skip a side to mix things up (sloat's idea)
    if counter % corners == 0:
        rack_side_index += 1
        counter = 0

    # get the rack-side index of 0, 1, or 2 (e.g. "4 % 3 = 1")
    rack_side_index = rack_side_index % corners
    ball_group_index = ball_group_index % corners

# print the results to the terminal
# should be: 
#         1 
#       12  14 
#     8   10   3
#   4   15   5   7  
# 6   2   13   9   11
for index in range(len(result.keys())):
    key = index + 1 # 1 based dictionary
    print("Ball #" + str(key) + ": " + str(result[key]))