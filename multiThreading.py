# SYED MUSAIB HUSSAIN
# 200901065
# MULTITHREADING LAB TASK

import threading

def SJF(num):
    print("\nShortest job first")
    def bubbleSort(burst_arr, arrival_arr, process_id_arr):
        n = len(arrival_arr)
       
        swapped = False

        for i in range(n - 1):

            for j in range(0, n - i - 1):


                if arrival_arr[j] > arrival_arr[j + 1]:
                    swapped = True
                    burst_arr[j], burst_arr[j + 1] = burst_arr[j + 1], burst_arr[j]
                    arrival_arr[j], arrival_arr[j + 1] = arrival_arr[j + 1], arrival_arr[j]
                    process_id_arr[j], process_id_arr[j + 1] = process_id_arr[j + 1], process_id_arr[j]

                if arrival_arr[j] == arrival_arr[j + 1]:
                    swapped = True
                    if burst_arr[j] > burst_arr[j + 1]:
                        burst_arr[j], burst_arr[j + 1] = burst_arr[j + 1], burst_arr[j]
                        arrival_arr[j], arrival_arr[j + 1] = arrival_arr[j + 1], arrival_arr[j]
                        process_id_arr[j], process_id_arr[j + 1] = process_id_arr[j + 1], process_id_arr[j]

            if not swapped:

                return

    if __name__ == '__main__':

        total_processes = 3
        process_id = [1, 2, 3]
        Arrival_time = [1, 3, 2]
        burst_time = [5, 6, 9]
        completion_time = []
        turn_around_time = []
        waiting_time = []

        bubbleSort(burst_time, Arrival_time, process_id)


        x = burst_time[0] + Arrival_time[0]
        completion_time.append(x)
        for i in range(1, total_processes):

            if Arrival_time[i] >= completion_time[i - 1]:
                y = Arrival_time[i] - completion_time[i - 1]
                z = burst_time[i] + completion_time[i - 1] + y
                completion_time.append(z)
            else:
                y = burst_time[i] + completion_time[i - 1]
                completion_time.append(y)


        for i in range(0, total_processes):
            x = completion_time[i] - Arrival_time[i]
            turn_around_time.append(x)


        for i in range(0, total_processes):
            x = turn_around_time[i] - burst_time[i]
            waiting_time.append(x)


        print("P.ID \t AT \t BT \t CT \t TAT \t WT")
        for i in range(0, total_processes):
            print("%d \t%d \t%d \t%d \t%d \t%d" % (
                process_id[i], Arrival_time[i], burst_time[i], completion_time[i], turn_around_time[i],
                waiting_time[i]))
            print()

        x = 0
        y = 0
        # Calculating average TAT and Waiting time
        for i in range(0, total_processes):
            x = x + turn_around_time[i]
            y = y + waiting_time[i]

        avgTAT = x / total_processes
        avgWT = y / total_processes

        print("\nAverage Turn around time: ", avgTAT)
        print("Waiting time: ", avgWT)


def FCFS(num):

        print("FIRST COME FIRST SERVE")
        no_process = 3
        process = [1, 2, 3]
        burst_time = [6, 2, 4]
        waiting_time = []
        turn_around_time = []

        x = 0
        waiting_time.append(x)
        for i in range(1, no_process):
            x = burst_time[i - 1] + waiting_time[i - 1]
            waiting_time.append(x)


        for i in range(0, no_process):
            x = burst_time[i] + waiting_time[i]
            turn_around_time.append(x)

        avgwt = 0
        avgtat = 0
        for i in range(0, no_process):
            avgwt = avgwt + waiting_time[i]
            avgtat = avgtat + turn_around_time[i]

        avgtat = avgtat / no_process
        avgwt = avgwt / no_process

        # printing Turn around Time and waiting
        print()
        for i in range(0, no_process):
            print("Process=", process[i])
            print("Burst Time=", burst_time[i])
            print("Waiting Time=", waiting_time[i])
            print("Turn Around Time=", turn_around_time[i])

        print()
        print("Average Waiting Time=", avgwt)
        print("Average Turn Around Time=", avgtat)


if __name__ == "__main__":

    t1 = threading.Thread(target=FCFS, args=(10,))
    t2 = threading.Thread(target=SJF, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
