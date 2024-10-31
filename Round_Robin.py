# Round Robin Scheduling Algorithm in Python

def round_robin(processes, burst_times, time_quantum):
    """
    Simulates the Round Robin CPU scheduling algorithm.
    
    Parameters:
    processes (list): List of process IDs.
    burst_times (list): List of burst times corresponding to each process.
    time_quantum (int): Time quantum for each process.
    
    Returns:
    None: Prints process completion times and turnaround times.
    """
    
    n = len(processes)  # Number of processes
    remaining_times = burst_times[:]  # Copy burst times for processing
    waiting_times = [0] * n  # Waiting time for each process
    turnaround_times = [0] * n  # Turnaround time for each process
    current_time = 0  # Track the elapsed time
    
    # While there are unfinished processes
    while any(remaining_times):
        for i in range(n):
            if remaining_times[i] > 0:
                # Process can only run up to the time quantum or less if it finishes
                processing_time = min(time_quantum, remaining_times[i])
                current_time += processing_time
                remaining_times[i] -= processing_time
                
                # Process completion
                if remaining_times[i] == 0:
                    turnaround_times[i] = current_time
                    waiting_times[i] = turnaround_times[i] - burst_times[i]

    # Output results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
    
    # Average waiting and turnaround times
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


# Example usage
processes = [1, 2, 3, 4]
burst_times = [10, 5, 8, 6]
time_quantum = 3

round_robin(processes, burst_times, time_quantum)
