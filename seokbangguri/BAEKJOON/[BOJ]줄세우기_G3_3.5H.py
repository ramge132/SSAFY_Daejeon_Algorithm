from pprint import pprint

from collections import deque

N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]
students = set([str(i) for i in range(1, N+1)])
priority = deque([])

graph = {}

for a, b in conditions:
    if graph.get(a):
        graph[a]['back'].add(b)
        graph[a]['back_length'] += 1
    
    else:
        graph[a] = {
            'front' : set(),
            'back' : set(),
            'front_length' : 0,
            'back_length' : 1
        }
        graph[a]['back'].add(b)

    
    if graph.get(b):
        graph[b]['front'].add(a)
        graph[b]['front_length'] += 1

    else:
        graph[b] = {
            'front' : set(),
            'back' : set(),
            'front_length' : 1,
            'back_length' : 0
        }
        graph[b]['front'].add(a)

while graph:
    temp_removed_key = []
    for key, node in graph.items():

        if node['front_length'] == 0:
            students.remove(str(key))
            priority.append(str(key))

            for back in node['back']:
                graph[back]['front'].remove(key)
                graph[back]['front_length'] -= 1

            temp_removed_key.append(key)
    
    for key in temp_removed_key:
        del graph[key]
        
print(" ".join(list(priority)) + " " + " ".join(list(students)))