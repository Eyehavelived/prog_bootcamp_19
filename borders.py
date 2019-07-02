class Table:
    """
    Written by JJ. Because awesome stuff are borne from laziness.
    This class object serves to print decent bordered tables from lists of lists.
    """
    def __init__(self, list_of_lists, wrapping=False, alignment="default", padding=1):
        # TODO: Write in function to accommodate text-wrap
        self.list_of_lists = list_of_lists
        self.number_of_columns = self.get_total_number_of_columns(list_of_lists)
        if alignment == "default":
            self.alignments = self.get_default_alignment()
        else:
            self.alignments = alignment
        self.column_sizes = self.get_column_sizes(padding)
        self.borders = self.get_borders_dict()
        self.top = self.build_bar("top")
        self.bottom = self.build_bar("bottom")
        self.middle = self.build_bar("middle")
        self.table = self.build_table(padding)

    def get_borders_dict(self):
        dictionary = {
            "top_left_corner": "\u2554",        # ╔
            "horizontal": "\u2550",             # ═
            "top_right_corner": "\u2557",       # ╗
            "vertical": "\u2551",               # ║
            "left_middle": "\u255F",            # ╟
            "right_middle": "\u2562",           # ╢
            "bottom_left_corner": "\u255A",     # ╚
            "top_middle": "\u2564",             # ╤
            "bottom_middle": "\u2567",          # ╧
            "bottom_right_corner": "\u255D",    # ╝
            "single_horizontal": "\u2500",      # ─
            "single_vertical": "\u2502",        # │
            "single_cross": "\u253C"            # ┼
        }
        return dictionary

    def get_total_number_of_columns(self, list_of_lists):
        number_of_columns = 0
        for each_list in list_of_lists:
            if len(each_list) > number_of_columns:
                number_of_columns = len(each_list)
        return number_of_columns

    def get_column_sizes(self, padding):
        column_sizes = [1] * self.number_of_columns
        for each_list in self.list_of_lists:
            i = 0
            while i < self.number_of_columns:
                try:
                    length_of_current_column = len(str(each_list[i]))
                    if length_of_current_column > column_sizes[i]:
                        column_sizes[i] = length_of_current_column
                except IndexError:
                    pass
                i += 1
        for i in range(len(column_sizes)):
            column_sizes[i] += 2 * padding                # to give 1 space padding for each border
        return column_sizes

    def build_bar(self, side):
        """
        consider the format cl-h-h-h-h-h-h-h-m-h-h-h-h-h-m-h-h-h-cr. This will be consistent throughout the table
        hence, it is reused to generate the top, middle and bottom border
        :param borders: a dictionary with all unicode borders
        :param column_sizes: integers
        :param side: a string for "top", "middle" or "bottom"
        :return: a string that is the border side
        """
        if side == "middle":
            h = self.borders.get("single_horizontal")
            cl = self.borders.get("left_middle")
            m = self.borders.get("single_cross")
            cr = self.borders.get("right_middle")
        else:
            h = self.borders.get("horizontal")
            if side == "top":
                cl = self.borders.get("top_left_corner")
                m = self.borders.get("top_middle")
                cr = self.borders.get("top_right_corner")
            elif side == "bottom":
                cl = self.borders.get("bottom_left_corner")
                m = self.borders.get("bottom_middle")
                cr = self.borders.get("bottom_right_corner")

        output = cl
        for i in range(len(self.column_sizes)):
            column_length = self.column_sizes[i]
            output += (h * column_length)
            if i != len(self.column_sizes) - 1:               # if this is not the last column, put the middle border
                output += m
            else:
                output += cr
        return output

    def get_default_alignment(self):
        alignment = ["center"] + (self.number_of_columns - 1) * ["left"]
        return alignment

    def build_content_row(self, row, borders, column_sizes, alignments, padding, number_of_columns):
        sides = borders.get("vertical")
        middle = borders.get("single_vertical")
        output = sides

        for i in range(number_of_columns):
            content = self.fill_white_space(alignments[i], row[i], padding, column_sizes[i])
            output += content
            if i != number_of_columns - 1:
                output += middle
            else:
                output += sides
        return output

    def fill_white_space(self, alignment, content, padding, column_size):
        """
        This function returns the string to be put in each column
        :param alignment: string for "left", "middle", "right"
        :param content: string to be printed
        :param padding: integer for the number of white spaces
        :param column_size: integer
        :return: string
        precondition: padding + content_length <= column_size
        """
        length_of_content = len(str(content))
        white_spaces = column_size - length_of_content
        if alignment == "left":
            left_padding = " " * padding
            value = str(content)
            right_padding = " " * (white_spaces - padding)
        elif alignment == "right":
            right_padding = " " * padding
            value = str(content)
            left_padding = " " * (white_spaces - padding)
        elif alignment == "center":
            left_padding = " " * (white_spaces//2)
            value = str(content)
            right_padding = " " * (white_spaces - white_spaces//2)

        output = left_padding + value + right_padding

        return output

    def build_table(self, padding):
        output = self.top
        number_of_rows = len(self.list_of_lists)
        for i in range(number_of_rows):
            row = self.list_of_lists[i]
            row_string = self.build_content_row(row, self.borders, self.column_sizes, self.alignments, padding,
                                                self.number_of_columns)
            output += "\n" + row_string
            if i < number_of_rows - 1:  # if current row is not the last row
                output += "\n" + self.middle
            else:
                output += "\n" + self.bottom

        return output

