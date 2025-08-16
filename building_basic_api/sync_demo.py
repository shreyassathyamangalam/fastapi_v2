import time
from timeit import default_timer as timer

def run_task(name, duration):
    print(f"Task {name} started at {timer()}")
    time.sleep(duration)
    print(f"Task {name} completed at {timer()}")
    
start = timer()
run_task("Task 1", 2)
run_task("Task 2", 1)
run_task("Task 3", 3)
print(f"\nAll tasks completed in {timer() - start:.2f} seconds")

    
    
    