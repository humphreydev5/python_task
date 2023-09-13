from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)           # Terry arrives
queue.append("Graham") 
print('the new:', queue)       # Graham arrives
queue.popleft()                 # The first to arrive now leaves
#'Eric'
queue.popleft()                 # The second to arrive now leaves
#'John'
#queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
print(queue)