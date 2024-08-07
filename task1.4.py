customers = [[5,2],[5,4],[10,3],[20,1]]

def avg_waiting_time(customers):
    time=0
    total_waiting_time=0

    for  arriving_time, preparing_time in customers:
        if time< arriving_time:
            time = arriving_time
        waiting_time = time- arriving_time +preparing_time
        total_waiting_time += waiting_time
        time +=preparing_time

    average_waiting_time = total_waiting_time/len(customers)
    return average_waiting_time       

average_waiting_time = avg_waiting_time(customers)
print(f'The average waiting time is: {average_waiting_time:.2f}')