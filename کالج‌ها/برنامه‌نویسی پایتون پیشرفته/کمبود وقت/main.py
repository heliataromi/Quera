from threading import Thread
import time


def grow_plants(duration):
    time.sleep(duration)
    print("The plants are grown!")


def listen_to_music(duration):
    time.sleep(duration)
    print("The music is played!")


def cook_meal(duration):
    time.sleep(duration)
    print("The meal is cooked!")


def run_sequential(durations):
    start_time = time.time()

    grow_plants(durations[0])
    listen_to_music(durations[1])
    cook_meal(durations[2])

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Sequential execution time: {elapsed_time:.1f} seconds")


def run_threaded(durations):
    start_time = time.time()

    t1 = Thread(target=grow_plants, args=(durations[0],))
    t2 = Thread(target=listen_to_music, args=(durations[1],))
    t3 = Thread(target=cook_meal, args=(durations[2],))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Threaded execution time: {elapsed_time:.1f} seconds")


durations = list(map(float, input().split()))
run_sequential(durations)
run_threaded(durations)

