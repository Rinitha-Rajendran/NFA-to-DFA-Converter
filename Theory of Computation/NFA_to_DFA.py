import pandas as pd
from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt

nfa = {}
n = int(input("No. of states : "))
t = int(input("No. of transitions : "))
for i in range(n):
    state = input("state name : ")
    nfa[state] = {}
    for j in range(t):
        path = input("path : ")
        
        print(f"Enter end state from state {state} travelling through path {path}: ")
        reaching_state = [x for x in input().split()]
        nfa[state][path] = reaching_state

print("\nNFA :- \n")
print(nfa)

nfa_table = pd.DataFrame(nfa)
print("\nPrinting NFA table :- ")
print(tabulate(nfa_table, headers='keys', tablefmt='fancy_grid'))

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]

new_states_list = []

# -------------------------------------------------

dfa = {}
keys_list = [list(nfa.keys())[0]]
path_list = list(nfa[keys_list[0]].keys())

dfa[keys_list[0]] = {}
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])
    dfa[keys_list[0]][path_list[y]] = var
    if var not in keys_list:
        new_states_list.append(var)
        keys_list.append(var)

while len(new_states_list) != 0:
    dfa[new_states_list[0]] = {}
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]
            s = "".join(sorted(set(temp)))
            if s not in keys_list:
                new_states_list.append(s)
                keys_list.append(s)
            dfa[new_states_list[0]][path_list[i]] = s

    new_states_list.remove(new_states_list[0])

print("\nDFA :- \n")
print(dfa)

dfa_table = pd.DataFrame(dfa)
print("\nPrinting DFA table :- ")
print(tabulate(dfa_table, headers='keys', tablefmt='fancy_grid'))

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)
def draw_dfa(dfa, final_states):
    G = nx.DiGraph()

    # Add nodes
    for state in dfa:
        if state in final_states:
            G.add_node(state, color='green')  # Set color for final states
        else:
            G.add_node(state)

    # Add edges
    for state, transitions in dfa.items():
        for symbol, next_state in transitions.items():
            if state == next_state:
                # Handling self-loops
                G.add_edge(state, next_state, label=symbol + "self-loop")
            else:
                G.add_edge(state, next_state, label=symbol)

    # Remove isolated nodes (states without transitions)
    isolated_nodes = [node for node in G.nodes if len(G.out_edges(node)) == 0]
    G.remove_nodes_from(isolated_nodes)

    # Draw graph if there are nodes left
    if G.number_of_nodes() > 0:
        pos = nx.spring_layout(G)

        # Draw edges with labels
        edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        # Draw nodes with colors
        node_colors = [node[1]['color'] if 'color' in node[1] else 'skyblue' for node in G.nodes(data=True)]
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color=node_colors, font_size=15, font_weight="bold", arrows=True)

        # Add arrow for the initial state
        initial_state = list(dfa.keys())[0]  # Assuming the first state is the initial state
        plt.annotate("", xy=pos[initial_state], xytext=(-20, 0),
                     textcoords='offset points', arrowprops=dict(arrowstyle="->", color='blue'))

        plt.title("DFA Graph")
        plt.show()
    else:
        print("No states with transitions found, unable to draw graph.")

# Example usage:
draw_dfa(dfa, dfa_final_states)
