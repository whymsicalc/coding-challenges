 class Canvas:
    def __init__(self):
        """Create instance of a Canvas."""

        self.canvas = []
        for i in range(10):
            self.canvas.append([' '] * 10)

    def print_canvas(self):
        """Print canvas with indices."""

        print('  0123456789')
        for i, row in enumerate(self.canvas):
            line = str(i) + ' '
            for item in row:
                line += item
            print(line)

    def add_shape(self, shape):
        """Add a shape to the canvas."""
        # Somehow loop through each line from start_x, start_y until end_x, end_y
        # At position update value to shape.fill_char
        canvas[shape.start_x][start_y] = shape.fill_char

    def clear_shape(self, shape):
        """Remove a shape from the canvas."""
        # Somehow loop through each line from start_x, start_y until end_x, end_y
        # At position update value to ' '
        canvas[shape.start_x][start_y] = ' '

    def move_shape(self, shape, axis, num):
        """Move a shape on the canvas."""
        if axis = 'x':
            shape.start_x += num
            shape.end_x += num
        elif axis = 'y':
            shape.start_y += num
            shape.end_y += num
        clear_shape(shape)
        add_shape(shape)


class Rectangle:
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Create instance of a Rectangle."""
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def change_fill(self, char):
        """Change the fill character of the Rectangle."""
        # Not sure what to do if shape is already on canvas?
        self.fill_char = char


