import random

num_size = 8
random_list = []

for i in range(num_size):
    random_list.append(random.randint(-100, 100))

try:

    while True:

        print(
            "Choose in action:"
            "\n1. Calculate the sum of negative numbers:"
            "\n2. Calculate the sum of neven numbers:"
            "\n3. Calculate the sum of odd numbers:"
            "\n4. Calculate the product of element divisible by 3:"
            "\n5. Calculate the product of elements between the minimum and maximum elements:"
            "\n6. Calculate the sum of elements between the first and last positive elements:"
            "\n7. Exit."
        )

        action = int(input("Enter action number: "))

        if action == 1:
            negative = 0
            for num_one in random_list:
                if num_one < 0:
                    negative += num_one
            print(f"Sum of negative: {negative}")

        elif action == 2:
            double_numbers = 0
            for num_two in random_list:
                if num_two % 2 == 0:
                    double_numbers += num_two
            print(f"Sum of even: {double_numbers}")

        elif action == 3:
            unpaired_numbers = 0
            for num_three in random_list:
                if num_three % 2 != 0:
                    unpaired_numbers += num_three
            print(f"Sum of unpaired: {unpaired_numbers}")

        elif action == 4:
            elements_with_indices = 1
            for four in range(len(random_list)):
                if four % 3 == 0:
                    elements_with_indices *= random_list[four]
            print(f"Product of element divisible by 3: {elements_with_indices}")

        elif action == 5:

            min_element = min(random_list)
            max_element = max(random_list)

            element_min_max = 1
            for five in random_list:
                if element_min_max <= five <= max_element:
                    element_min_max *= five
            print(
                f"Product of elements between the minimum and maximum elements: {element_min_max}"
            )

        elif action == 6:

            first_positive_element = None
            last_positive_element = None

            for first_element in range(len(random_list)):
                if random_list[first_element] < 0:
                    first_positive_element = first_element
                    break

            for last_element in range(len(random_list) - 1, -1, -1):
                if random_list[last_element] > 0:
                    last_positive_element = last_element
                    break

            if (
                first_positive_element is not None
                and last_positive_element is not None
                and first_positive_element < last_positive_element
            ):
                sum_positive = 0
                for six in range(first_positive_element + 1, last_positive_element):
                    sum_positive += random_list[six]
                print(f"Sum element: {sum_positive}")
            else:
                print("No positive element found!")

        elif action == 7:
            print("Exit.")
            break

except Exception as e:
    print(e)
