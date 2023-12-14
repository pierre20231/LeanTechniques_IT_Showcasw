def calculate_currency(amount):
    currency_units = [10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    result = {unit: 0 for unit in currency_units}
    for unit in currency_units:
        count = int(amount / unit)
        result[unit] = count
        amount -= count * unit

    return result


def display_result(result):
    print("Result:")
    for unit, count in result.items():
        if count > 0:
            print(f"{count} - ${unit:.2f} bill/coin")


def main():
    try:
        amount = float(input("Enter the amount: $"))
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
        return
    if amount < 0:
        print("Invalid input. Please enter a non-negative amount.")
        return
    result = calculate_currency(amount)
    display_result(result)


main()
