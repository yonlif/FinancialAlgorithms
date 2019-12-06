from typing import List

"""
Implementing algorithm A (Greedy) - pick the highest value until full.
"""

weights = [100] + [2] * 50
max_weight = 100


def choices(values: List[float]) -> List[bool]:
    weight_sum = 0
    pick_list = []
    # Sorting the items by value
    sorted_values_weights = sorted(zip(values, weights), key=lambda x: x[0], reverse=True)
    # For each item - if it fits in the knapsack take it
    for v, w in sorted_values_weights:
        if weight_sum + w <= max_weight:
            weight_sum += w
            pick_list.append(True)
        else:
            pick_list.append(False)
    return pick_list


def payments(values: List[float]) -> List[float]:
    # Find who are the one's that should pay
    org_choices = choices(values)
    payments_list = []
    for i, item in enumerate(org_choices):
        if not item:
            # If item was not picked - we do not need to pay
            payments_list.append(0)
        else:
            # Find the threshold value by iterating down the item until it is not picked
            ended = False
            for new_index in range(i + 1, len(values)):
                new_values = values
                new_values[i] = values[new_index]
                new_choices = choices(new_values)
                if new_choices[i] == 0:
                    ended = True
                    payments_list.append(values[new_index])
                    break
            if not ended:
                payments_list.append(values[-1])
    return payments_list


if __name__ == '__main__':
    print(payments([100] + [20] * 50))
