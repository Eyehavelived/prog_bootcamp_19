from borders import *

class PairUp:
    def __init__(self, a_list):
        self.list = a_list
        self.unique_list = self.get_unique()
        self.pairs = self.find_pairs()
        self.table_format = self.format()

    def get_unique(self):
        """
        For this, it does not matter if the list has 3 or more copies of the same number, as only 2 are compared at any
        point in time. Additionally, since the pair of numbers have to be one odd and one even to meet the even product,
        odd sum criterion, the pair of numbers will never be the same number.

        This means that we can reduce the run time significantly by ignoring all duplicates, and also avoid producing
        duplicate results for the user.

        :Complexity: O(1)
        :return: None
        """
        return list(set(self.list))

    def find_pairs(self):
        """
        For a pair of numbers whose produce is even and whose sum is odd, one of the numbers must be odd, and the other
        even. We can reduce the total runtime by simply checking if the pairs are even and odd. This is especially so
        when handling large numbers which may take longer to multiply, or even result in memory overflow after
        multiplying.
        :return: a list of lists containing integer pairs
        :complexity: O(N^2) where N is the length of the list.
        """
        unique_pairs = []
        for i in range(len(self.unique_list) - 1):  # because the last element has nothing else to be compared with
            i_is_odd = self.is_odd(self.unique_list[i])
            for j in range(i + 1, len(self.unique_list)):
                j_is_odd = self.is_odd(self.unique_list[j])
                if j_is_odd != i_is_odd:  # essentially XOR
                    unique_pairs.append([self.unique_list[i], self.unique_list[j]])
        return unique_pairs

    def is_odd(self, number):
        """
        Returns True or False based on whether the input integer is odd or even
        :param number: an integer
        :return: a boolean
        :complexity: O(1)
        """
        if number % 2 == 1:
            return True
        else:
            return False

    def format(self):
        n = 1
        table = [["", "Val 1", "Val 2"]]
        for pair in self.pairs:
            table.append([str(n) + "."] + pair)
            n += 1
        return table

if __name__ == "__main__":
    running = True
    while running:
        input_invalid = False
        try:
            user_list = input("Give the list of integers separated by commas.\nFor example: '1,5,3,7,2,1'\n\n")
            input_list = user_list.split(",")
            for i in range(len(input_list)):
                item = input_list[i]
                if int(item) != int(str(item)):
                    input_invalid = True
                    print(str(item) + " is not an integer.")
                input_list[i] = int(item)

        except ValueError:
            input_invalid = True
            print(str(item) + " is not an integer.")
        except TypeError:
            input_invalid = True
            print(str(item) + " is not an integer.")

        if not input_invalid:
            pairs = PairUp(input_list)
            print(Table(pairs.table_format).table)

        input("\n\nPress enter to continue.\n\n")