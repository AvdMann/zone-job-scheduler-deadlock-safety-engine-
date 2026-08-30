PAGE_SIZE = 1024

PAGE_TABLE = {
    0: 5,
    1: 2,
    2: 9,
    3: 1
}

SEGMENT_TABLE = {
    0: (1000, 400),
    1: (2200, 300),
    2: (500, 150)
}


def translate_paged(address):
    page = address // PAGE_SIZE
    offset = address % PAGE_SIZE

    if page not in PAGE_TABLE:
        print(f"{address} -> PAGE FAULT")
        return

    frame = PAGE_TABLE[page]
    physical = frame * PAGE_SIZE + offset

    print(f"{address} -> {physical}")


def translate_segmented(segment, offset):
    if segment not in SEGMENT_TABLE:
        print(f"({segment},{offset}) -> SEGMENT FAULT")
        return

    base, limit = SEGMENT_TABLE[segment]

    if offset >= limit:
        print(f"({segment},{offset}) -> SEGMENTATION FAULT")
        return

    physical = base + offset

    print(f"({segment},{offset}) -> {physical}")


print("PAGING")

translate_paged(260)
translate_paged(1500)
translate_paged(3000)
translate_paged(5000)

print("\nSEGMENTATION")

translate_segmented(0, 150)
translate_segmented(1, 350)
translate_segmented(2, 100)
