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
    # TODO Uncomment this input
    #source = person_id_for_name(input("Name: "))
    source = person_id_for_name("Kevin Bacon")
    print(source)
    # source = person_id_for_name("source_")
    if source is None:
        # TODO Uncomment this hard coding and put back sysexit
        # source = "Kevin Bacon"
        sys.exit("Person not found.")
    # TODO Uncomment this input
    # target = person_id_for_name(input("Name: "))
    target = person_id_for_name("Demi Moore")
    print(target)
    if target is None:
        # TODO Uncomment this hard coding and put back sysexit
        # target = "Demi Moore"
        # target = "Bill Paxton"
        # target = "Sally Field"
        # target = "Will DaRosa"
        # target = "Cary Elwes"
        sys.exit("Person not found.")
    path = shortest_path(source, target)
    # print("And finally, path is: " + path)
    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        # This statement sets up the path, with no movie, but the orig actor.
        path = [(None, source)] + path
        print(path)
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
    source_id = source
    target_id = target
    solution = []
    # Create a node from where we are (the source_list[0] id)
    start = Node(state=source_id, parent=None, action=None)
    # Start with a frontier that contains the initial state:
    frontier = StackFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = set()

    # Set the goal as the target's id
    goal = target_id
    print("Goal is: " + goal)
    # Now for the search loop

    while True:
        # print("shortest_path loop called.")
        # print("Start Frontier length: " + str((len(frontier))))
        # If frontier is empty, then no solution:
        if frontier.empty():
            raise Exception("no solution")

        # Remove a node from the frontier.
        node = frontier.remove()
        # print("End Frontier length: " + str((len(frontier))))
        num_explored += 1

        # If node contains goal state, return the solution:
        if node.state == goal:
            # TODO This needs to be changed to put the movie and the
            # actor together.
            # Old versions:
            # actions = []
            # movies_tog = []
            actor = []
            while node.parent is not None:
                # actions.append(node.action)
                # movies_tog.append(node.state)
                solution = (node.action, node.state)
                actor.append(solution)
                node = node.parent
            # actions.reverse()
            # movies_tog.reverse()

            # solution_details = (actions, movies_tog)
            # solution.append(solution_details)
            print("We're returning the solution: " + str(solution))
            return actor

        # Mark node as explored
        # print("Node added to explored: " + node.state)
        explored.add(node.state)

        # TODO expand the node
        # Expand node, add resulting nodes to the frontier.
        # This means looking at all the neighbours of the node.
        # print("Num Exp: " + str(num_explored))
        # print(neighbors_for_person(node.state))
        # print(" Node ID: " + str(node.state))
        # print(neighbors_for_person(node.state))
        # print("Explored: "+ str(explored))
        for costar_movie, state, in neighbors_for_person(node.state):
            # print("Expanding node loop called. ")
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=costar_movie)
                # print("Child created.")
                frontier.add(child)
                # print("Node: " + node.state + " added to frontier.")

    # TODO
    # raise NotImplementedError


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
    initial_actor = person_id
    movie_ids = people[person_id]["movies"]
    # print("movie_ids: "+ str(movie_ids))
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            # TODO I need to omit the person who started this function
            if person_id != initial_actor:
                neighbors.add((movie_id, person_id))
    # print("Neighbors: " + str(neighbors))

    return neighbors


if __name__ == "__main__":
    main()
