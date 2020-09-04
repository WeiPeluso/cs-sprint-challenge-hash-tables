#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket_table = {}
    route = []

    for ticket in tickets:
        ticket_table[ticket.source] = ticket.destination

    index = 0
    curr_dest = "NONE"
    while index < length:
        curr_dest = ticket_table.get(curr_dest)
        route.append(curr_dest)
        index += 1

    return route
