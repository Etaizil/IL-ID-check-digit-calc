from typing import Union


class IDCalculator:
    def calculate(self, id_number: Union[str, int]) -> int:
        id_number = str(id_number)
        if not id_number.isdigit():
            raise TypeError("Should contain digits only")
        if len(id_number) != 8 and len(id_number) != 9:
            raise TypeError("ID number must be 8 or 9 digits long")
        if len(id_number) == 9:
            id_number = id_number[:-1]
        check_digit = 0
        odd = 0
        digits_list = [int(digit) for digit in id_number]
        # original_check_number = digits_list[len(digits_list) - 1]
        digits_sum = 0
        for i in range(len(digits_list)):
            prod = (1 + odd) * digits_list[i]
            if prod > 9:
                prod -= 9
            digits_sum += prod
            odd ^= 1
        check_digit = (10 - (digits_sum % 10)) % 10
        return check_digit
