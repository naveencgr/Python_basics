import queue

my_queue = queue.LifoQueue(maxsize=10)
for i in range(0,10):
    my_queue.put(i)

print(f"queue size{my_queue.qsize}")    
