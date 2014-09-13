import curses

class Point:
    x = None
    y = None
    value = None
    path_length_from_start = None;
    came_from = None;
    estimate_path_length = None;
    estimate_full_path_length = None;

    def __init__(self, position, value):
        self.x = position[0]
        self.y = position[1]
        self.value = value

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def get_estimate_full_path_length(self):
        return self.path_length_from_start + self.estimate_path_length

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
        #self.start_point = start_point
        self.set_start_point(start_point)
        #self.end_point = end_point
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


#--------------program starts here---------------------
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

start_point = Point([8,1], 'S')

start_point.path_length_from_start = 0
start_point.came_from = 0

end_point = Point([4,34], 'E')

graph = Graph(start_point, end_point)
graph.display(stdscr)
closed_set = []
open_set = []

open_set.append(graph.start_point);
while len(open_set) > 0:
    pass

