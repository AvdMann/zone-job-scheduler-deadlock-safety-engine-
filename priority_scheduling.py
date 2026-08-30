from jobs import JOBS


def effective_priority(job, current_time, aging=False):
    if not aging:
        return job["priority"]

    waited = max(0, current_time - job["arrival_time"])
    return max(1, job["priority"] - (waited // 3))


def run_priority(aging=False):
    jobs = [dict(job) for job in JOBS]
    completed = []
    current_time = 0
    waits = {}

    while len(completed) < len(jobs):
        ready = [
            job for job in jobs
            if job not in completed and job["arrival_time"] <= current_time
        ]

        if not ready:
            current_time += 1
            continue

        ready.sort(
            key=lambda j: (
                effective_priority(j, current_time, aging),
                j["arrival_time"],
                j["job_id"]
            )
        )

        job = ready[0]

        waiting_time = current_time - job["arrival_time"]
        waits[job["job_id"]] = waiting_time

        current_time += job["burst_time"]
        completed.append(job)

    mode = "WITH AGING" if aging else "WITHOUT AGING"

    print(f"\nPRIORITY SCHEDULING {mode}")
    print("-" * 50)

    longest_job = max(waits, key=waits.get)

    for job_id, wait in waits.items():
        print(f"{job_id}: Waiting Time = {wait}")

    print(
        f"\nLongest Waiting Job: "
        f"{longest_job} ({waits[longest_job]} ticks)"
    )


if __name__ == "__main__":
    run_priority(False)
    run_priority(True)
