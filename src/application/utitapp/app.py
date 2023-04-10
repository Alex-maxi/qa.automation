class Apps:

    def revarray(self, arr):
        return arr[::-1]
    
    def get_sum_of_digits(self, num):
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum

