# AI Practical Exam Viva Guide

This guide is prepared from the codes in this folder for final practical exam preparation.
It covers:
- What each practical does
- Key theory behind it
- **Theory & usefulness** for each code file (definitions, role in AI, real-world value)
- Likely viva questions and strong answers
- Common debugging/improvement points examiners ask

---

## Practical 1: `Assignment-A1.py` (DFS and BFS on Graph)

### What this practical is
This program builds an **undirected graph** using adjacency lists and performs:
- **DFS (Depth First Search)** using recursion
- **BFS (Breadth First Search)** using queue (`collections.deque`)

You enter edges and a start node, and it prints traversal order.

### Core concepts
- Graph representation: dictionary of lists
- Traversal strategies:
  - DFS: go deep first, then backtrack
  - BFS: visit level by level
- Visited set prevents infinite loops in cyclic graphs

### Theory & usefulness (`Assignment-A1.py`)
- **What the underlying theory is:** A graph is a pair \((V, E)\) of vertices and edges. **DFS** formalizes *depth-priority* exploration of a **search tree** implicit in the graph; **BFS** formalizes *breadth-priority* exploration. Both are **uninformed** (blind) search strategies: they only use connectivity, not a goal estimate. The **visited** set implements the closed list idea so you do not expand the same state twice—essential when the graph has cycles.
- **Why it matters in AI:** Almost every discrete AI problem (maze, planning, game tree, web crawl, dependency graph) eventually reduces to “move on a graph.” DFS and BFS are the two canonical ways to enumerate reachable states before you add heuristics or costs. Understanding their order of expansion is prerequisite for A*, IDA*, and many planners.
- **How useful it is in practice:** **BFS** is used when you need **shortest hop count** in unweighted graphs (social degrees, network routing layers, level-order processing). **DFS** is used for **topological intuition**, cycle detection, connected components, and when memory for a wide frontier is costly. For viva: tie the code to “state space” and “complete vs optimal” (BFS is complete for finite branching; on unweighted graphs it is optimal for shortest path in edges).

### Likely viva Q&A
1. **Q: Difference between DFS and BFS?**  
   **A:** DFS uses stack/recursion and explores one branch deeply before backtracking. BFS uses queue and explores nodes level by level. BFS gives shortest path in unweighted graph; DFS does not guarantee shortest.

2. **Q: Why use a visited set?**  
   **A:** To avoid revisiting nodes and infinite loops in cyclic graphs.

3. **Q: Time complexity of DFS and BFS?**  
   **A:** Both are `O(V + E)` where `V` is vertices and `E` is edges.

4. **Q: Why is `deque` used in BFS?**  
   **A:** `deque.popleft()` is efficient `O(1)`, unlike list pop from front.

5. **Q: Is this graph directed or undirected?**  
   **A:** Undirected, because each edge is added in both directions (`u->v` and `v->u`).

### Important correction examiner may ask
- `dfs(node, visited=set())` uses mutable default argument. Better style:
  - use `visited=None`, then create set inside function.

---

## Practical 2: `Assignment-A2.py` (A* for 8-Puzzle)

### What this practical is
This solves the **8-puzzle** using **A\*** search.
- Goal state is fixed as:
  - `[[1,2,3],[4,5,6],[7,8,0]]`
- Heuristic `h(n)` = number of misplaced tiles (excluding blank `0`)
- `f(n) = g(n) + h(n)` where:
  - `g(n)` = cost from start to current state
  - `h(n)` = estimated cost to goal

### Core concepts
- Informed search (heuristic-based)
- Priority queue (`heapq`) selects node with minimum `f`
- State conversion to tuple for hashing in visited set
- Neighbor generation by moving blank tile in 4 directions

### Theory & usefulness (`Assignment-A2.py`)
- **What the underlying theory is:** The 8-puzzle is a **state-space search** problem: nodes are board configurations, edges are legal moves. **A\*** evaluates nodes by \(f(n) = g(n) + h(n)\): **\(g\)** is exact cost from the start, **\(h\)** is an **heuristic estimate** of remaining cost to the goal. With a **min-heap**, you always expand the currently most promising partial solution. If **\(h\)** is **admissible** (never overestimates), A\* remains **optimal** for tree search; with consistent heuristics and graph search variants, optimality is preserved under standard conditions you can mention briefly in viva.
- **Why it matters in AI:** A\* is the standard teaching bridge from blind search (BFS/DFS) to **heuristic planning** used in games, robotics, and puzzle solvers. It shows how **domain knowledge** (misplaced tiles) reduces search compared to uninformed methods.
- **How useful it is in practice:** Same ideas scale to **pathfinding** (maps, games), **motion planning** (with different state spaces), and **scheduling** as graph search. Misplaced-tile count is simple and admissible but weak; **Manhattan distance** is still admissible for the 8-puzzle and usually expands far fewer nodes—good improvement talking point.

### Likely viva Q&A
1. **Q: Why A\* instead of BFS for 8-puzzle?**  
   **A:** BFS is uninformed and explores many states. A\* uses heuristic to reach goal faster.

2. **Q: What is heuristic in this code?**  
   **A:** Misplaced tiles count.

3. **Q: Is misplaced tile heuristic admissible?**  
   **A:** Yes, it never overestimates true remaining moves.

4. **Q: What data structure is used for open list?**  
   **A:** Min-heap priority queue from `heapq`.

5. **Q: Why convert list state to tuple?**  
   **A:** Lists are mutable and unhashable; tuples are hashable for set membership.

6. **Q: If no solution exists, what happens?**  
   **A:** Function returns `None`, and program prints "No solution found."

### Improvement points
- Add solvability check using inversion count before running A\*.
- Better heuristic: Manhattan distance gives stronger guidance than misplaced tiles.

---

## Practical 3: `Assignment-A3.py` (Selection Sort and Prim's MST)

### What this practical is
Menu-driven program implementing:
1. **Selection Sort** on user-entered numbers
2. **Prim's algorithm** to find Minimum Spanning Tree (MST) from adjacency matrix

### Core concepts
- Selection sort repeatedly picks minimum from unsorted part
- Prim grows MST by adding minimum weight edge from visited to unvisited node
- Weighted connected undirected graph for MST

### Theory & usefulness (`Assignment-A3.py`)
- **Selection sort — theory:** A **comparison sort** that maintains an invariant: after pass \(i\), the first \(i\) positions hold the \(i\) smallest elements in final order. It minimizes **writes** to memory (at most one swap per pass) but always does about \(\Theta(n^2)\) comparisons—so it is **not** used for large production datasets; it is pedagogical and sometimes acceptable for tiny \(n\) or very simple hardware.
- **Prim’s MST — theory:** An MST is a **spanning tree** (connects all vertices, acyclic) with **minimum total edge weight**. **Prim’s** is a **greedy** algorithm: at each step, add the **cheapest edge** that connects the already chosen set to a new vertex. On connected graphs with nonnegative weights, this greedy choice is globally correct for MST.
- **How useful:** Sorting is foundational everywhere (indexes, ranking). **MST** models **minimum-cost connectivity**: network design (fiber, power), **clustering** (single-linkage ideas), **approximation** for TSP heuristics, and **spanning** subgraphs in graph ML pipelines. For viva: Prim is “grow a tree from one root”; Kruskal is “sort edges globally”—same problem, different greedy view.

### Likely viva Q&A
1. **Q: How selection sort works?**  
   **A:** For each index `i`, find minimum element from `i...end` and swap with `arr[i]`.

2. **Q: Time complexity of selection sort?**  
   **A:** `O(n^2)` in best, average, and worst case.

3. **Q: What is MST?**  
   **A:** A spanning tree connecting all vertices with minimum total edge weight and no cycles.

4. **Q: Prim vs Kruskal?**  
   **A:** Prim grows from a start vertex using local minimum connecting edge. Kruskal sorts all edges globally and adds edges avoiding cycles.

5. **Q: Complexity of Prim in this code?**  
   **A:** About `O(V^2)` due to adjacency matrix scanning.

6. **Q: Why 0 means no edge here?**  
   **A:** In this representation, non-diagonal zero indicates absence of edge.

### Improvement points
- Handle disconnected graph case explicitly.
- Replace `minimum = 999` with `float("inf")`.

---

## Practical 4: `Assignment-B4.py` (N-Queen using Backtracking)

### What this practical is
Solves N-Queen problem using recursion and backtracking.
- Places one queen per row
- Tracks unsafe columns and diagonals
- Prints one valid board configuration using `Q` and `.`

### Core concepts
- Constraint Satisfaction Problem (CSP)
- Backtracking:
  - choose position
  - recurse
  - undo choice if dead end
- Diagonal indexing:
  - right diagonal index = `i + j`
  - left diagonal index = `i - j + n - 1`

### Theory & usefulness (`Assignment-B4.py`)
- **What the underlying theory is:** N-Queens is a classic **CSP**: variables are row positions (or column placements), domains are columns, **constraints** are “no two queens attack” (column + two diagonal relations). **Backtracking** is **depth-first search** over partial assignments: assign a variable, recurse; if a constraint fails, **undo** (backtrack) and try another value. It is systematic **trial and error** with pruning—far better than generating all \(n^n\)-style blind placements.
- **Why it matters in AI:** CSP + backtracking is the backbone of **scheduling**, **timetabling**, **sudoku/solvers**, **configuration**, and many **logic puzzles**. It teaches **constraint propagation** intuition (even if this small code only uses implicit checking).
- **How useful it is:** Real systems add **forward checking**, **arc consistency (AC-3)**, and **variable ordering** (MRV) to cut search drastically. For viva: say N-Queens is a toy model of “assign resources under mutual exclusion rules.”

### Likely viva Q&A
1. **Q: Why backtracking is used in N-Queen?**  
   **A:** It systematically explores valid placements and backtracks when constraints fail.

2. **Q: What constraints are checked?**  
   **A:** Same column, same left diagonal, same right diagonal.

3. **Q: Why arrays of size `2*n` for diagonals?**  
   **A:** Total possible diagonal indices are up to `2n-1`; size `2*n` safely covers indexing.

4. **Q: Does this code print all solutions?**  
   **A:** No, it returns after first valid solution (`return True`).

5. **Q: Worst-case time complexity?**  
   **A:** Exponential, roughly `O(n!)` for brute-force style backtracking.

### Improvement points
- Modify to collect and print all solutions.
- Validate `n` input (`n >= 1`).

---

## Practical 5: `Assignment-B5.py` (Rule-based Chatbot using NLTK)

### What this practical is
A simple customer-support chatbot using:
- `nltk.chat.util.Chat`
- Pattern-response pairs (regex + fixed replies)
- Interactive conversation loop (`chatbot.converse()`)

### Core concepts
- Pattern matching with regular expressions
- Rule-based NLP (not ML-based learning)
- Reflections support pronoun conversion (from NLTK utility)

### Theory & usefulness (`Assignment-B5.py`)
- **What the underlying theory is:** This is **symbolic / rule-based AI**: language behavior is specified as **if pattern then response** rules (often regex). There is **no learned model**; behavior is **transparent** and **editable** by humans. NLTK’s `Chat` is a thin engine: match input against ordered patterns, return a template—optionally with **reflection** (simple pronoun swaps). Theoretically it sits opposite **statistical NLP** and **deep learning**: coverage is limited to what authors encoded.
- **Why it matters in AI curricula:** It shows the **knowledge engineering** era of NLP and is still relevant as a **baseline** and for **controlled domains** where you need predictable answers.
- **How useful it is in practice:** Great for **FAQs**, **IT support scripts**, **keyword triage**, and **compliance-sensitive** bots where every utterance should be traceable to a rule. Weak for **paraphrase**, **long context**, and **open-domain** chat—there you move to retrieval + LLMs or intent classifiers. For viva: emphasize **interpretability** vs **scalability of coverage**.

### Likely viva Q&A
1. **Q: Is this chatbot AI or hardcoded?**  
   **A:** It is rule-based AI using predefined regex patterns and responses; it does not learn from data.

2. **Q: Why `nltk.download('punkt')`?**  
   **A:** It downloads tokenizer resources; in this code, chat mainly uses regex rules, but NLTK setup often includes this dependency.

3. **Q: What is the role of `pairs` list?**  
   **A:** It maps user input patterns to possible bot responses.

4. **Q: What happens if input does not match any pattern?**  
   **A:** Chat may give default/empty behavior depending on `Chat` handling; typically no meaningful custom response unless fallback rule is added.

5. **Q: How can we improve it?**  
   **A:** Add more patterns, fallback intent, context memory, or switch to ML/NLU approach.

### Improvement points
- Add catch-all fallback pattern for unmatched queries.
- Make regex case-insensitive robustly.

---

## Practical 6: `Assignment-C6.py` (Medical Expert System)

### What this practical is
A small **expert system** for diagnosis based on symptoms.
- Knowledge base maps diseases to symptom list
- Program asks yes/no symptom questions
- Computes score = number of matched symptoms for each disease
- Displays disease(s) with highest score

### Core concepts
- Knowledge base + inference
- Rule-based decision support
- Score-based matching (not probabilistic model)
- Input validation loop (`yes/no`)

### Theory & usefulness (`Assignment-C6.py`)
- **What the underlying theory is:** An **expert system** encodes **domain knowledge** (here: diseases → symptoms) separately from the **inference procedure** (here: count symptom matches per disease and rank). This follows the classic **knowledge base + inference engine** split from early AI. The scoring used is a **simple evidential tally**, not **Bayesian** posteriors or **certainty factors** (MYCIN-style), but the *architecture* is the same family: **rule-based decision support**.
- **Why it matters in AI:** It illustrates **knowledge representation** and **automated reasoning** without ML, and shows limitations (ties, no symptom importance, no negation/uncertainty in the basic score).
- **How useful it is in practice:** **Clinical decision support**, **equipment fault diagnosis**, and **helpdesk trees** still use rule engines plus curated knowledge—often **combined** today with ML for risk scores. For viva: stress **education only**, **not** for real diagnosis; real tools need validated models, regulation, and human oversight.

### Likely viva Q&A
1. **Q: Why is this called expert system?**  
   **A:** Because it uses domain knowledge encoded as rules/symptom mappings to infer possible diagnosis.

2. **Q: What inference approach is used?**  
   **A:** Simple score-based matching over rule base (not full forward-chaining engine, but conceptually rule-based inference).

3. **Q: Can multiple diseases be output?**  
   **A:** Yes, if two or more diseases have the same maximum score.

4. **Q: Is this medically accurate for real diagnosis?**  
   **A:** No, it is educational and simplified; real systems need large validated datasets and clinical supervision.

5. **Q: How is invalid input handled?**  
   **A:** `ask()` loops until user enters `yes` or `no`.

### Improvement points
- Add weighted symptoms instead of equal weights.
- Add certainty percentage and tie-breaking logic.

---

## Cross-Practical Theory Questions (Very Common in Viva)

1. **What is the difference between uninformed and informed search?**  
Uninformed search uses only problem definition (e.g., DFS/BFS), informed uses heuristic knowledge (e.g., A\*).

2. **What is heuristic function?**  
A function that estimates cost from current state to goal to guide search efficiently.

3. **What is backtracking?**  
A recursive trial-and-error method that abandons partial solutions when they violate constraints.

4. **What is a greedy choice in Prim's algorithm?**  
At each step, choose minimum weight edge connecting visited and unvisited set.

5. **Difference between rule-based system and machine learning model?**  
Rule-based uses manually written logic; ML learns patterns from data.

6. **What is time complexity and space complexity? Why important?**  
They measure algorithm efficiency in resource usage and scalability.

---

## Quick Last-Minute Viva Answers (1-liners)

- **DFS uses stack/recursion, BFS uses queue.**
- **BFS finds shortest path in unweighted graph.**
- **A\* uses `f(n)=g(n)+h(n)` to choose best node.**
- **N-Queen is a classic backtracking CSP.**
- **Prim's algorithm finds MST in weighted connected graph.**
- **Chatbot code is rule-based NLP, not deep learning.**
- **Medical expert system uses symptom-rule matching.**


Prepare one dry run per practical and one improvement suggestion per practical; this creates a strong viva impression.

