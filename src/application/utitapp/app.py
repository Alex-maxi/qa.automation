class Apps:

    def revarray(self, arr):
        """
        Reverses the order of elements in the input array.

        Args:
        input_array (list): A list of elements to be reversed.

        Returns:
        list: A list of elements in reverse order.
        """
        return arr[::-1]
    
    def get_sum_of_digits(self, num):
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum

