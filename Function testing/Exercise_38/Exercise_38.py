def calculate_tax(amount, age, tax=17.0):
    """The function returns the amount of income tax."""

    tax_rate = tax / 100.0

    if age <= 18:
        return int(min(amount * tax_rate, 6000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 9000))