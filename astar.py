import curses
class OpenSet:
    open_set = []

    def append(self, value):
        self.open_set.append(value)

    def get_lowest_f(self):
        min = self[0]
        for point in self:
            if point.f < min.f:
                min = point

    def __getitem__(self, index):
        return self[index]

    def __len__(self):
        return len(self.open_set)

    def remove(self, point_to_remove):
        self.open_set.remove(point_to_remove)



class Point:
    x = None
    y = None
    value = None
    path_length_from_start = None;
    came_from = None;
    estimate_path_length = None;
    estimate_full_path_length = None;
    g = None # cost form start
    h = None # heuristic cost to goal
    f = None

    def __init__(self, position, value):
        self.x = position[0]
        self.y = position[1]
        self.value = value

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def get_estimate_full_path_length(self):
        return self.path_length_from_start + self.estimate_path_length

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

class Graph:
    start_point = None
    end_point = None

    data = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    def __init__(self, start_point, end_point):
        self.set_start_point(start_point)
        self.set_end_point(end_point)
        self.update_graphs_data()

    def set_start_point(self, point):
        self.data[point.x][point.y] = point.value

    def set_end_point(self, point):
        self.data[point.x][point.y] = point.value

    def update_graphs_data(self):
        line_number = 0
        for line in self.data:
            item_number = 0
            for item in line:
                if item == 0:
                    self.data[line_number][item_number] = Point([line_number, item_number], 0)
                elif item == 1:
                    self.data[line_number][item_number] = Point([line_number, item_number], 1)
                elif item == 'S':
                    self.data[line_number][item_number] = Point([line_number, item_number], 'S')
                elif item == 'E':
                    self.data[line_number][item_number] = Point([line_number, item_number], 'E')
                item_number = item_number+1
            line_number = line_number+1
    
    def display(self, curses_window):
        line_number = 0
        for line in self.data:
            item_number = 0
            for item in line:
                if self.data[line_number][item_number].value == 1:
                    curses_window.addstr(line_number, item_number, '0')
                    curses_window.refresh()
                elif self.data[line_number][item_number].value == 0:
                    curses_window.addstr(line_number, item_number, '.')
                    curses_window.refresh()
                elif self.data[line_number][item_number].value == 'S':
                    curses_window.addstr(line_number, item_number, 'S')
                    curses_window.refresh()
                elif self.data[line_number][item_number].value == 'E':
                    curses_window.addstr(line_number, item_number, 'E')
                    curses_window.refresh()
                item_number = item_number+1
            line_number = line_number+1
    def get_heuristic_path_length(self, from_point, to_point):
        return int(from_point.x - to_point.x) + int(from_point.y - to_point.y)
    def __eq__(self, other):
        first = self.x == other.x
        last = self.y == other.y
        return first == last


#--------------program starts here---------------------
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

start_point = Point([8,1], 'S')
end_point = Point([4,34], 'E')

graph = Graph(start_point, end_point)
graph.display(stdscr)

closed_set = []
open_set = OpenSet()

open_set.append(graph.start_point);
print type(graph.start_point)
exit()
graph.start_point.g = 0 # there is zero hops from start point to start point ;)
graph.start_point.h = graph.get_heuristic_path_length(start_point, end_point); # gets heuristic path to goal
graph.start_point.f = start_point.g + start_point.h  

while len(open_set) > 0:
    low_f_point = open_set.get_lowest_f()
    if low_f_point == end_point:
        print "FOUND!!!!" # need to replace it with real function
        exit()

    open_set.remove(low_f_point)
    closed_set.append(low_f_point)

    for point in low_f_point.get_neighbors(): # CONTINUE HERE
        pass


    


