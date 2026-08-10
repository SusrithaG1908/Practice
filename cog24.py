def coin_combinations(coins, target):

    result = []

    def backtrack(index, remaining, current):

        # Target reached
        if remaining == 0:
            result.append(current.copy())
            return

        # No coins left or remaining became negative
        if index == len(coins) or remaining < 0:
            return

        # Choice 1: Include current coin
        current.append(coins[index])

        # Stay at same index because coin can be reused
        backtrack(
            index,
            remaining - coins[index],
            current
        )

        current.pop()

        # Choice 2: Don't include current coin
        backtrack(
            index + 1,
            remaining,
            current
        )

    backtrack(0, target, [])

    return result


print(coin_combinations([2, 3, 5], 7))