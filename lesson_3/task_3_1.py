def div_func(div_1, div_2):
    try:
        result = int(div_1) / int(div_2)
    except ValueError:
        return 'Please use a number!'
    except ZeroDivisionError:
        return "You can't use zero as a divisor!"

    return result


print("Result = ", div_func(input('Enter divisible: '), input('Enter divisor : ')))
