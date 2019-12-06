def fitst_x_numbers_greater_or_equal_than_y_divided_by_z_and_not_divided_by_q(x, y, z, q):

    if x < 0:
        raise ValueError("Number count parameter must be greater than zero")

    list_of_numbers = []
    while len(list_of_numbers) != x:
        if y % z == 0 and y % q != 0:
            list_of_numbers.append(y)
        y += 1
    return list_of_numbers


print(fitst_x_numbers_greater_or_equal_than_y_divided_by_z_and_not_divided_by_q(-1, 100, 3, 2))
