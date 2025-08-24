from collections import deque

queue = deque()

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

queue += graph["you"]


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue
        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return person
        search_queue += graph[person]
        searched.append(person)
    return None


search("you")
