#   In The Name of ALLAH


def max_objects(n, m, k, object_sizes):

    if m == 0:
        return 0

    boxes = m
    max_value = 0
    packed_objects = 0
    for object_size in object_sizes[::-1]:

        if object_size > k:
            return packed_objects

        if object_size + max_value <= k:
            max_value += object_size
            packed_objects += 1
            continue

        boxes -= 1
        max_value = object_size
        if boxes == 0 and max_value > 0:
            return packed_objects
        packed_objects += 1

    return n


n, m, k = map(int, input().split())
object_sizes = list(map(int, input().split()))

print(max_objects(n, m, k, object_sizes))

