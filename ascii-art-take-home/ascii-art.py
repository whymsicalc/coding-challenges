 class Canvas:
    def __init__(self):
        """Create instance of a Canvas."""

        self.canvas = []
        self.shapes = []
        for i in range(10):
            self.canvas.append([' '] * 10)

    def print_canvas(self):
        """Print canvas with indices."""
                
        # Add rectangles to canvas
        for shape in self.shapes:
          for x in range(shape.start_x, shape.end_x + 1):
            for y in range(shape.start_y, shape.end_y + 1):
                self.canvas[x][y] = shape.fill_char
        
        print('  0123456789')
        for i, row in enumerate(self.canvas):
            line = str(i) + ' '
            for item in row:
                line += item
            print(line)

    def add_shape(self, shape):
        """Add a shape to the canvas."""
        self.shapes.append(shape)

    def clear_shape(self, shape):
        """Remove a shape from the canvas."""
        self.shapes.remove(shape)


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
        self.fill_char = char
        
    def move_shape(self, shape, axis, num):
        """Update start and end point of shape."""
        if axis = 'x':
            shape.start_x += num
            shape.end_x += num
        elif axis = 'y':
            shape.start_y += num
            shape.end_y += num

