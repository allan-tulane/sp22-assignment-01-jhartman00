"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""


# no imports needed.


def foo(x):
    if x <= 1:
        return x
    else:
        return x * foo(x - 1)


def longest_run(mylist, key):
    longest = 0
    current = 0
    for i in mylist:
        if i == key:
            current += 1
            continue
        if i != key:
            if current > longest:
                longest = current
                current = 0
            else:
                current = 0
    if current > longest:
        longest = current
    return longest


class Result:
    """ done """

    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return (
                'longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
                (self.longest_size, self.left_size, self.right_size,
                 self.is_entire_range))


def longest_run_recursive(mylist, key):
  x = longest_run_recursive_runner(mylist, key).longest_size
  return x


def longest_run_recursive_runner(mylist, key):
  # base cases
  if len(mylist) == 1 and mylist[0] == key:
      return Result(1, 1, 1, True)
  elif len(mylist) == 1 and mylist[0] != key:
      return Result(0, 0, 0, False)
  elif len(mylist) == 0:
      return Result(0, 0, 0, False)
  else:
      left_list = mylist[:len(mylist) // 2]
      right_list = mylist[len(mylist) // 2:]
      left = longest_run_recursive_runner(left_list, key)
      right = longest_run_recursive_runner(right_list, key)
      combined = combine_results(left, right)
      return combined

def combine_results(left, right):

    # both sides are entirely the key
    if left.is_entire_range and right.is_entire_range:
        return Result(left.left_size + right.right_size,  left.left_size + right.right_size, left.left_size + right.right_size, True)

    # one side is the key
    elif left.is_entire_range or right.is_entire_range:

        # left is entire key and right has left key > 0
        # ex. L(1,1,1,T) + R(1,0,1,F) = 1,0,2,F
        if left.is_entire_range and right.left_size > 0:
            return Result(left.left_size + right.left_size,
                          right.right_size,
                          max(left.left_size + right.left_size, left.longest_size, right.longest_size),
                          False)

        # right is entire key and left has right key
        elif right.is_entire_range and left.right_size > 0:
            return Result(left.left_size,
                          right.right_size + left.right_size,
                          max(right.right_size + left.right_size, left.longest_size, right.longest_size),
                          False)

        # left is entire key and right doesn't have left key
        # ex. L(2,2,2,T) + R(0,1,1,F) = 2,1,2,F
        elif left.is_entire_range and right.left_size == 0:
            return Result(left.left_size,
                          right.right_size,
                          max(left.longest_size, right.longest_size),
                          False)

        # right is entire key and left doesn't have right key
        elif right.is_entire_range and left.right_size == 0:
            return Result(left.left_size,
                          right.right_size,
                          max(right.longest_size, left.longest_size),
                          False)

    # neither side is key
    else:
        # neither are fully the key, but they do have keys touching in the middle
        # ex. L(0, 1, 1, F) + R(1, 0, 1, F) = (0, 0, 2, F)
        if left.right_size > 0 and right.left_size > 0:
            return Result(left.left_size,
                          right.right_size,
                          max(left.right_size + right.left_size, left.longest_size, right.longest_size),
                          False)
        # neither are fully the key and the keys aren't touching in the middle
        # ex. L(1,0,1,F) + R(0,1,1,F) = (1, 1, 1, F)
        else:
            return Result(left.left_size,
                          right.right_size,
                          max(left.longest_size, right.longest_size),
                          False)


# Feel free to add your own tests here.
def test_longest_run():
    assert longest_run_recursive([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3
    assert longest_run_recursive([2, 12, 12, 8, 12, 12, 7, 0, 12, 1], 12) == 2
    assert longest_run_recursive([1,1,1,1,1,1,1,1,1,1], 1) == 10
    assert longest_run_recursive([1,1,1,1,1,1,1,1,1,1], 0) == 0

