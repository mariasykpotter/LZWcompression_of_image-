from arrays import Array2D


class GrayscaleImage:
    """
    Implements the GrayscaleImage ADT  for use with the Game of Life.
    """

    def __init__(self, n_rows, n_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._image = Array2D(n_rows, n_cols)

    def width(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._image.num_cols()

    def height(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._image.num_rows()

    def clear(self, value):
        """
        Clears the indicated cell by setting it to dead.
        :param value: str
        """
        for i in range(self.height()):
            for j in range(self.width()):
                if 0 <= value <= 255:
                    self._image.__setitem__((i, j), value)

    def getitem(self, row, col):
        '''
        Gets the item from 2D Array
        :param row: int
        :param col: int
        :return: None
        '''
        return self._image.__getitem__((row, col))

    def setitem(self, row, col, value):
        '''
        Sets the item in 2D Array
        :param row: int
        :param col: int
        :param value: str
        :return: None
        '''
        return self._image.__setitem__((row, col), value)
