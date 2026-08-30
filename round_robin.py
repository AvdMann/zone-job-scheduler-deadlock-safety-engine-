from collections import deque
from jobs import JOBS


def round_robin(quantum):
    jobs = sorted(JOBS, key=lambda x: x["arrival_time"])

    remaining = {
        job["job_id"]: job["burst_time"]
        for job in jobs
    }

    completion = {}
    ready = deque()

    time = 0
    index = 0

    dispatch_slices = 0
    context_switches = -1

    while len(completion) < len(jobs):

        while index < len(jobs) and jobs[index]["arrival_time"] <= time:
            ready.append(jobs[index])
            index += 1

        if not ready:
            time += 1
            continue

        current = ready.popleft()

        dispatch_slices += 1
        context_switches += 1

        run_time = min(
            quantum,
            remaining[current["job_id"]]
        )

        start = time
        end = time + run_time

        remaining[current["job_id"]] -= run_time
        time = end

        while index < len(jobs) and jobs[index]["arrival_time"] <= time:
            ready.append(jobs[index])
            index += 1

        if remaining[current["job_id"]] > 0:
            ready.append(current)
        else:
            completion[current["job_id"]] = time

    total_wait = 0
    total_turnaround = 0

    print(f"\nROUND ROBIN (Quantum = {quantum})")
    print("-" * 60)
    print("Job ID\tWaiting\tTurnaround")

    for job in jobs:
        turnaround = (
            completion[job["job_id"]]
            - job["arrival_time"]
        )

        waiting = turnaround - job["burst_time"]

        total_wait += waiting
        total_turnaround += turnaround

        print(
            f"{job['job_id']}\t{waiting}\t{turnaround}"
        )

    print(
        f"\nAverage Waiting Time: "
        f"{total_wait / len(jobs):.2f}"
    )

    print(
        f"Average Turnaround Time: "
        f"{total_turnaround / len(jobs):.2f}"
    )

    print(f"Dispatch Slices: {dispatch_slices}")
    print(f"Context Switches: {context_switches}")


if __name__ == "__main__":
    round_robin(3)
    round_robin(6)

    print(
        "\nTheory: Quantum 3 causes more overhead "
        "than Quantum 6 because more context "
        "switches occur."
    )
