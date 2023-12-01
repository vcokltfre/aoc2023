from pathlib import Path

lines = Path("other/01/python-1/input.txt").read_text().splitlines()

print(sum(map(lambda line:[nums:=list(filter(str.isnumeric, line)),int(nums[0]+nums[-1])][-1],lines)))  # type: ignore
