def fractional_knapsack(weights, values, capacity):
    # Create list of (value/weight ratio, weight, value)
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort by ratio in descending order
    items.sort(reverse=True)

    total_value = 0

    for ratio, weight, value in items:

        # Take whole item
        if capacity >= weight:
            total_value += value
            capacity -= weight

        # Take fraction of item
        else:
            total_value += ratio * capacity
            break

    return total_value


# Example
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print(fractional_knapsack(weights, values, capacity))