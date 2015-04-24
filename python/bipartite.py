def bipartite(G):
  red = []
  black = []
  first_value = G.keys()[0]
  todo = [first_value]
  red.append(first_value)
  while len(todo) > 0:
    current = todo[0]
    del todo[0]
    neighbors = G[current]
    # the current value is in which set?
    currents_set = red if current in red else black
    # and the opposite of the current set is...
    second_set = red if currents_set is black else black
    for n in neighbors:
      # If n is in the currents set, we have problems:
      if n in currents_set: return None
      # Otherwise, check if its in the others set.
      # If not, add it and insert to front of todo list.
      if n not in second_set:
        todo.insert(0, n)
        second_set.append(n)
  return set(red)

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None

test()
