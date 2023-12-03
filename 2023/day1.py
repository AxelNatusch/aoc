def get_input():
    with open("data/day1.txt") as f:
        return f.read().splitlines()


def part1():
    num_list = []
    for word in get_input():
        first_num = last_num = None
        for char in word:
            if char.isdigit():
                num = int(char)
                if first_num is None:
                    first_num = num
                last_num = num

        if first_num is not None and last_num is not None:
            num_list.append(int(f"{first_num}{last_num}"))

    return sum(num_list)


def part2():
    num_list = []
    replace_list = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for word in get_input():
        for spelled, digit in replace_list.items():
            word = word.replace(spelled, digit)

        first_num = last_num = None
        for char in word:
            if char.isdigit():
                if first_num is None:
                    first_num = char
                last_num = char

        if first_num is not None and last_num is not None:
            num_list.append(int(f"{first_num}{last_num}"))

    return sum(num_list)


def part2_copied():
    with open("data/day1.txt") as file:
        lines = file.read().strip().split("\n")

    total_value = 0
    spelled_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for line in lines:
        for i in range(len(spelled_numbers)):
            if spelled_numbers[i] in line:
                line = line.replace(
                    spelled_numbers[i],
                    spelled_numbers[i][0] + str(i + 1) + spelled_numbers[i][-1],
                )
        calibration_value = ""
        for i in range(len(line)):
            if line[i].isdigit():
                calibration_value += line[i]
                break
        for i in range(len(line)):
            if line[len(line) - i - 1].isdigit():
                calibration_value += line[len(line) - i - 1]
                break
        total_value += int(calibration_value)
    print(total_value)


if __name__ == "__main__":
    print(part1())
    print(part2())
    print(part2_copied())
