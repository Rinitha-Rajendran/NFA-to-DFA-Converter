# NFA to DFA Converter

This Python tool converts a Non-deterministic Finite Automaton (NFA) into a Deterministic Finite Automaton (DFA). It includes interactive input for NFA details, displays transition tables using pandas and tabulate, and visualizes the resulting DFA graphically with NetworkX and Matplotlib.

## Installation

Clone the repository and navigate to the `theory_of_computation` folder:

```bash
git clone https://github.com/Rinitha-Rajendran/Theory of Computation.git
cd Theory of Computation
```

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Run the `NFA_to_DFA.py` script to start the tool. Follow the prompts to input the number of states, transitions, state names, paths, and end states for each path. The script will output the NFA and DFA transition tables, identify final states of the DFA, and display a graphical representation of the DFA.

Example usage:

```bash
python NFA_to_DFA.py
```

## File Structure

- `NFA_to_DFA.py`: Main script for NFA to DFA conversion and visualization.
- `requirements.txt`: List of dependencies.
- `README.md`: This file, containing instructions and information about the project.


## Additional Information

For more details on the conversion process, examples of input and output, and how to contribute to the project, please refer to the `README.md` and `nfa_to_dfa.py` files within the `theory_of_computation` folder.

###Example Input:

No. of states : 2
No. of transitions : 2
state name : A
path : a
Enter end state from state A travelling through path a:
B
path : b
Enter end state from state A travelling through path b:
A
state name : B
path : a
Enter end state from state B travelling through path a:
A B
path : b
Enter end state from state B travelling through path b:
B
Enter final state of NFA :
B

#Example Output:

NFA :-
{'A': {'a': ['B'], 'b': ['A']}, 'B': {'a': ['A', 'B'], 'b': ['B']}}

Printing NFA table :-
╒═════╤════════╤════════╕
│     │ a      │ b      │
╞═════╪════════╪════════╡
│ A   │ ['B']  │ ['A']  │
├─────┼────────┼────────┤
│ B   │ ['A', 'B'] │ ['B']  │
╘═════╧════════╧════════╛

DFA :-
{'A': {'a': 'B', 'b': 'A'}, 'B': {'a': 'AB', 'b': 'B'}, 'AB': {'a': 'AB', 'b': 'AB'}}

Printing DFA table :-
╒══════╤════════╤════════╕
│      │ a      │ b      │
╞══════╪════════╪════════╡
│ A    │ B      │ A      │
├──────┼────────┼────────┤
│ B    │ AB     │ B      │
├──────┼────────┼────────┤
│ AB   │ AB     │ AB     │
╘══════╧════════╧════════╛

Final states of the DFA are :  ['B', 'AB']

