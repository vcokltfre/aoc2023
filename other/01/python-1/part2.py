from pathlib import Path

lines = Path("other/01/python-1/input.txt").read_text().splitlines()

num_map = {
    "one": 1,
    "two": 2,
    "six": 6,
    "four": 4,
    "five": 5,
    "nine": 9,
    "three": 3,
    "seven": 7,
    "eight": 8,
    **{str(i): i for i in range(1,10)},
}

total = 0

for line in lines:
    nums: list[int] = []

    for i in range(len(line)):
        for num_str, num in num_map.items():
            if line[i:i+len(num_str)] == num_str:
                nums.append(num)
                break

    total += (10 * nums[0]) + nums[-1]

print(total)
