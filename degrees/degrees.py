import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")
    # TODO Delete the plain source and target hard codings
    source = None
    target = None
    # TODO Uncomment this input
    # source = person_id_for_name(input("Name: "))
    if source is None:
        # TODO Uncomment this hard coding and put back sysexit
        source = "Kevin Bacon"
        # sys.exit("Person not found.")
    # TODO Uncomment this input
    # target = person_id_for_name(input("Name: "))
    if target is None:
        # TODO Uncomment this hard coding and put back sysexit
        target = "Demi Moore"
        # sys.exit("Person not found.")
    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")



def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    num_explored = 0
    source_dict = person_id_for_name(source)
    target_dict = person_id_for_name(target)
    print(source_dict, target_dict)
    # Create a node from where we are (the source_list[0] id)
    start = Node(state=source_dict, parent=None, action=None)
    # Start with a frontier that contains the initial state:
    frontier = StackFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = set()

    # Set the goal as the target's id
    goal = target_dict[0]
    # Now for the search loop

    while True:
        # If frontier is empty, then no solution:
        if frontier.empty():
            raise Exception("no solution")

        # Remove a node from the frontier.
        node = frontier.remove()

        num_explored += 1

        # If node contains goal state, return the solution:
        if node.state == goal:
            actions = []
            movies = []
            while node.parent is not None:
                actions.append(node.action)
                movies.append(node.state)
                node = node.parent
            actions.reverse()
            movies.reverse()
            solution = (actions, movies)
            return

        # Mark node as explored
        explored.add(node.state)

        # TODO expand the node
        # Expand node, add resulting nodes to the frontier.
        # This means looking at all the neighbours of the node.
        print(neighbors_for_person(node.state))

        for action, state in neighbors_for_person(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)

    # TODO
    # raise NotImplementedError

    # TODO Just return the path between stars
    return path

# def neighbors(state):
#     """
#     Accepts a node state as an argument. The node state refers to the
#     actor that we are at for that node.
#     This will return actors who have been in the same films as source.
#     Returns neighbour as actor id.
#     """
#     neighbours = []
#
#     return neighbours


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
