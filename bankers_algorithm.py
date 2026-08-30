AVAILABLE = [3, 3, 2]

MAX_NEED = {
    "P0": [7, 5, 3],
    "P1": [3, 2, 2],
    "P2": [9, 0, 2],
    "P3": [2, 2, 2]
}

ALLOCATION = {
    "P0": [0, 1, 0],
    "P1": [2, 0, 0],
    "P2": [3, 0, 2],
    "P3": [2, 1, 1]
}


def calculate_need():
    need = {}

    for p in MAX_NEED:
        need[p] = [
            MAX_NEED[p][i] - ALLOCATION[p][i]
            for i in range(3)
        ]

    return need


def is_safe(avail, alloc, need):
    work = avail[:]
    finish = {p: False for p in alloc}
    sequence = []

    changed = True

    while changed:
        changed = False

        for p in alloc:
            if not finish[p]all(
                    need[p][i] <= work[i]
                    for i in range(3)
                ):
                    for i in range(3):
                        work[i] += alloc[p][i]

                    finish[p] = True
                    sequence.append(p)
                    changed = True

    return all(finish.values()), sequence


def request_resources(process, request):
    avail = AVAILABLE[:]

    alloc = {
        p: ALLOCATION[p][:]
        for p in ALLOCATION
    }

    need = calculate_need()

    if any(request[i] > need[process][i] for i in range(3)):
        return False

    if any(request[i] > avail[i] for i in range(3)):
        return False

    for i in range(3):
        avail[i] -= request[i]
        alloc[process][i] += request[i]
        need[process][i] -= request[i]

    safe, seq = is_safe(avail, alloc, need)

    return safe


need = calculate_need()

print("NEED MATRIX")
for p in need:
    print(p, need[p])

safe, sequence = is_safe(
    AVAILABLE,
    ALLOCATION,
    need
)

print("\nSAFE STATE:", safe)
print("SAFE SEQUENCE:", sequence)

print(
    "\nP1 Request [1,0,2]:",
    "GRANTED" if request_resources(
        "P1",
        [1, 0, 2]
    ) else "DENIED"
)

print(
    "P0 Request [2,0,2]:",
    "GRANTED" if request_resources(
        "P0",
        [2, 0, 2]
    ) else "DENIED"
)
