# Graph coloring problem.

colors = ['Blue', 'Red', 'Green', 'Yellow']

# total number of meetings
meeting = ['1', '2', '3', '4', '5', '6', '7']

# Choosing the neighbours of each meeting from the given table.
neighbors = {}
neighbors['1'] = ['2', '3', '4', '5', '7']
neighbors['2'] = ['1', '3']
neighbors['3'] = ['1', '2', '4', '5', '6']
neighbors['4'] = ['1', '3', '5', '7']
neighbors['5'] = ['1', '3', '4', '6', '7']
neighbors['6'] = ['3', '5']
neighbors['7'] = ['1', '4', '5']

# Deciding each of unique color to be assigned to the meeting.
colors_of_meeting = {}

def promising(meet, color):
    ''' This function checks for unique color for each neighbours and return boolean value.'''
    for neighbor in neighbors.get(meet): 
        color_of_neighbor = colors_of_meeting.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_meeting_color(meet):
    ''' This function returns the unique color of a meeting. '''
    for color in colors:
        if promising(meet, color):
            return color

# Assigning colors to each meeting.
for meet in meeting:
    colors_of_meeting[meet] = get_meeting_color(meet)

print ("These are the colors of each meeting: ")
print (colors_of_meeting)
print("\n")
print ("The vertices of the graph are: ")
print (meeting)
print("\n")
print ("The edges of the graph are: ")

edges = []

for i in neighbors:
    for j in neighbors[i]:
        edges.append((i,j))
print (edges)
