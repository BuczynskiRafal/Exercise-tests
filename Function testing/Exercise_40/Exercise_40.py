def income_tax(income, first_thresh=17.0, second_thresh=32.0):
    first_rate = first_thresh / 100.0
    second_rate = second_thresh / 100.0
    threshold = 85528
    if income < threshold:
        return income * first_rate
    else:
        return threshold * first_rate + (income - threshold) * second_rate