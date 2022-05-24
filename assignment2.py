'''Assignment 2

This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line
username1 = input("Kindly select a username from the list, @bongolpoc, @joaquin, @chums, @jobenilagan, @joeilagan, @eeebeee")
username2 = input("Kindly select another username from the list, @bongolpoc, @joaquin, @chums, @jobenilagan, @joeilagan, @eeebeee")

if (from_member in social_graph[to_member]["following"]) and (to_member in social_graph[from_member]["following"]):
    return "friends"
elif to_member in social_graph[from_member]["following"]:
    return "follower"
elif from_member in social_graph[to_member]["following"]:
    return "followed by"
else:
    return "no relationship"

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    }
}
print(relationship_status("@chums","@jobenilagan",social_graph))

def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-2-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line
symbol = '';

for row in range(0,len(board)-1):
    for col in range(0,len(board[row])-2):
        if board[row][col] == board[row][col+1] and board[row][col] == board[row][col+2]:
            symbol = board[row][col]


for col in range(0,len(board)-1):
    for row in range(0,len(board[col])-2):
        if board[row][col] == board[row+1][col] and board[row][col] == board[row+2][col]:
            symbol =  board[row][col]


for row in range(0,len(board)-2):
    for col in range(0,len(board[row])-2):
        if board[row][col] == board[row+1][col+1] and board[row][col] == board[row+2][col+2]:
            symbol = board[row][col]


for row in range(len(board)-1,-1,-1):
    for col in range(0,len(board[row])-2):
        if board[row][col] == board[row-1][col+1] and board[row][col] == board[row-2][col+2]:
            symbol = board[row][col]

if symbol == '':
    return "NO WINNER"
else:
    return symbol


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

print(tic_tac_toe(board6))
    '''
    Item 3.
    ETA. 10 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line
if (first_stop == "admu" and second_stop == "upd") or (first_stop == "upd" and second_stop == "admu"):
    value = (route_map["upd","admu"]["travel_time_mins"])
    return value

elif (first_stop == "admu" and second_stop == "dlsu") or (first_stop == "dlsu" and second_stop == "admu"):
    value = (route_map["admu","dlsu"]["travel_time_mins"])
    return value

elif (first_stop == "dlsu" and second_stop == "upd") or (first_stop == "upd" and second_stop == "dlsu"):
    value = (route_map["dlsu","upd"]["travel_time_mins"])
    return value
else:
    return ("Invalid Input")

legs = {
("upd","admu"):{
    "travel_time_mins":10
},
("admu","dlsu"):{
    "travel_time_mins":35
},
("dlsu","upd"):{
    "travel_time_mins":55
}
}

print("estimated time of arrival: " + str(eta("dlsu", "admu", legs)) + "minutes")
