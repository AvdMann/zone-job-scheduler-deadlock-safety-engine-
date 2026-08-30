from jobs import JOBS


def print_results(name, results):
    print(f"\n{name}")
    print("-" * 70)
    print("Job ID\tWaiting Time\tTurnaround Time")

    total_wait = 0
    total_turnaround = 0

    for job_id, wait, turnaround in results:
        print(f"{job_id}\t{wait}\t\t{turnaround}")
        total_wait += wait
        total_turnaround += turnaround

    avg_wait = total_wait / len(results)
    avg_turnaround = total_turnaround / len(results)

    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")


def fcfs():
    jobs = sorted(JOBS, key=lambda x: (x["arrival_time"], x["job_id"]))

    current_time = 0
    results = []

    for job in jobs:
        if current_time < job["arrival_time"]:
            current_time = job["arrival_time"]

        waiting_time = current_time - job["arrival_time"]
        current_time += job["burst_time"]
        turnaround_time = current_time - job["arrival_time"]

        results.append(
            (job["job_id"], waiting_time, turnaround_time)
        )

    print_results("FCFS Scheduling", results)


def sjf_non_preemptive():
    jobs = [dict(job) for job in JOBS]

    completed = []
    current_time = 0

    while len(completed) < len(jobs):
        ready = [
            job for job in jobs
            if job not in completed and job["arrival_time"] <= current_time
        ]

        if not ready:
            current_time += 1
            continue

        ready.sort(
            key=lambda x: (
                x["burst_time"],
                x["arrival_time"],
                x["job_id"]
            )
        )

        job = ready[0]

        waiting_time = current_time - job["arrival_time"]
        current_time += job["burst_time"]
        turnaround_time = current_time - job["arrival_time"]

        completed.append(job)

        job["waiting_time"] = waiting_time
        job["turnaround_time"] = turnaround_time

    results = [
        (
            job["job_id"],
            job["waiting_time"],
            job["turnaround_time"]
        )
        for job in completed
    ]

    print_results("SJF Non-Preemptive", results)


def srtf():
    jobs = [dict(job) for job in JOBS]

    remaining = {
        job["job_id"]: job["burst_time"]
        for job in jobs
    }

    completion = {}

    time = 0

    while len(completion) < len(jobs):
        ready = [
            job for job in jobs
            if job["arrival_time"] <= time
            and remaining[job["job_id"]] > 0
        ]

        if not ready:
            time += 1
            continue

        ready.sort(
            key=lambda x: (
                remaining[x["job_id"]],
                x["arrival_time"],
                x["job_id"]
            )
        )

        current = ready[0]

        remaining[current["job_id"]] -= 1
        time += 1

        if remaining[current["job_id"]] == 0:
            completion[current["job_id"]] = time

    results = []

    for job in jobs:
        turnaround = completion[job["job_id"]] - job["arrival_time"]
        waiting = turnaround - job["burst_time"]

        results.append(
            (
                job["job_id"],
                waiting,
                turnaround
            )
        )

    print_results("SRTF Scheduling", results)


if __name__ == "__main__":
    print(
        "Tie-breaking rule: "
        "earlier arrival_time, then lower job_id."
    )

    fcfs()
    sjf_non_preemptive()
    srtf()
