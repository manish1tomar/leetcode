def heapify(items=[]):
    def bubbleDown(idx):
        nonlocal items

        left = (idx*2) + 1
        right = left + 1

        if left < len(items) and items[left] > items[idx]:
            items[left], items[idx] = items[idx], items[left]
            if left < len(items):
                bubbleDown(left)

        if right < len(items) and items[right] > items[idx]:
            items[right], items[idx] = items[idx], items[right]
            if right < len(items):
                bubbleDown(right)

    idx_first_parent = len(items) // 2

    while idx_first_parent >= 0:
        left = idx_first_parent * 2 + 1
        right = left + 1

        if left < len(items) and items[left] > items[idx_first_parent]:
            items[left], items[idx_first_parent] = items[idx_first_parent], items[left]
            bubbleDown(left)
        if right < len(items) and items[right] > items[idx_first_parent]:
            items[right], items[idx_first_parent] = items[idx_first_parent], items[right]
            bubbleDown(right)
        idx_first_parent -= 1

    return items

def HeapSort(items=[]):
    def bubbleDown(idx):
        nonlocal items

        left = (idx*2) + 1
        right = left + 1

        if left < len(items) and items[left] > items[idx]:
            items[left], items[idx] = items[idx], items[left]
            if left < len(items):
                bubbleDown(left)

        if right < len(items) and items[right] > items[idx]:
            items[right], items[idx] = items[idx], items[right]
            if right < len(items):
                bubbleDown(right)

    while len(items) > 0:
        items[0], items[len(items) - 1] = items[len(items) - 1], items[0]
        max = items.pop()
        print(max)
        bubbleDown(0)


print(heapify([10,20,15,12,40,25,18]))
items = heapify([10,20,15,12,40,25,18])
HeapSort(items)
