import math
import time

TREATS_PER_CELL = 7 # used to estimate the needed number of cells
filename = "input.txt"
def run(filename):
    start_time = time.time()
    with open(filename) as file:
        n_treats = int(file.readline()) # Number of treats.
        coords = [[float(xy) for xy in line.split()] for line in file]

    # Number of cells per side of the square:
    side_length = math.ceil(math.sqrt(max(1, n_treats / TREATS_PER_CELL)))

    # Build the cell dict and fill it:
    cell_dict = {}
    for x in range(side_length):
        for y in range(side_length):
            cell_dict[(x,y)] = []

    for pos in coords:
        x = int(side_length * pos[0])
        y = int(side_length * pos[1])
        cell_dict[(x,y)].append(pos)

    # Calculate the total distance
    total_distance = 0
    current_pos = [0.5, 0.5]
    current_cell = (int(side_length * 0.5), int(side_length * 0.5))
    for n in range(n_treats):
        interesting_cells = []
        radius = 0 # The search radius around the current cell
        max_radius = side_length
        found = False # No treats have yet been found
        while radius <= side_length:
            for x in range(-radius, radius + 1):
                x_pos = current_cell[0] + x
                if x_ps not in range(0, side_length):
                    continue
                for y in range(-radius, radius+1):
                    y_pos = current_cell[1] + y
                    if y_pos not in range(0, side_length):
                        continue

                    cell = (x_pos, y_pos)
                    if cell in interesting_cells:
                        continue

                    if cell in cell_dict:
                        if cell_dict[cell]:
                            interesting_cells.append(cell)
                            if not found:
                                found = True
                                max_radius = max(math.ceil(radius*math.sqrt(2)),
                                                 radius + 2)
                            else:
                                del cell_dict[cell]

            radius += 1
        next_pos = None

        min_distance = 3 # Some random big number.
        for cell in interesting_cells:
            for pos in cell_dict[cell]:
                distance = math.hypot(pos[0] - current_pos[0],
                                      pos[1] - current_pos[1])
                if distance < min_distance:
                    min_distance = distance
                    next_pos = pos
                    current_cell = cell
        total_distance += min_distance
        current_pos = next_pos
        cell_dict[current_cell].remove(current_pos)

    print("distance: ", total_distance)
    print("Time: ", time.time() - start_time)