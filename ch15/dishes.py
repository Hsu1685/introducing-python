import multiprocessing as mp
import os
import time

def washer(dishes, output):
    for dish in dishes:
        print("Process %s says: " % os.getpid(), 'Washing', dish, 'dish')
        time.sleep(0.5)
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print("Process %s says: " % os.getpid(), 'Drying', dish, 'dish')
        input.task_done() # Indicate that a formerly enqueued task is complete.

if __name__ == '__main__':
    print("Process %s says: " % os.getpid(), "I'm the main program")
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()
    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()
