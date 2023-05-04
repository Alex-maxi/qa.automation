class Apps:
    """Class test simple functions"""

    def revarray(self, arr: list) -> list:
        """
        Reverses the order of elements in the input array.
        Args:
            arr (list): A list of elements to be reversed.

        Returns:
            list: A list of elements in reverse order.
        """
        return arr[::-1]

    def get_sum_of_digits(self, num:int) -> int:
        """
        Sum of entered numbers.
        Args:
            num (int): Input numbers.  

        Returns:
            int: Sum of inputed numbers.
        """
        sum_ = 0
        for digit in str(num):
            sum_ += int(digit)
        return sum_
