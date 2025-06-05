# AI-Snake-Agent

An intelligent agent for the classic Snake game implemented in Python. This project integrates informed and uninformed search algorithms to guide the snake toward food while avoiding collisions and boundaries. The agent uses classic search strategies such as BFS, DFS, and A*.

---

## Project Goal

The goal of this project is to develop a search-based intelligent agent that controls a snake in the traditional Snake game environment. The agent makes decisions by evaluating paths to food using different search strategies, ensuring safe navigation and optimal performance.

---

## Implemented Search Algorithms

- **Breadth-First Search (BFS)** 
- **Depth-First Search (DFS)** 
- **A Star Search** 
- **Heuristics**:
  - **Manhattan Distance**
  - **Euclidean Distance**

---

## File Structure & Components

| File | Description |
|------|-------------|
| `A_STAR.py` | Implements the A* search algorithm |
| `BFS.py` | Implements Breadth-First Search |
| `DFS.py` | Implements Depth-First Search |
| `Algorithm.py` | Provides heuristic functions (Manhattan & Euclidean), neighbor handling, and utility functions |
| `Main.py` | Main file to run the game and switch between algorithms |
| `Node` structure | Represents positions in the game grid |

Each file implements a `run_algorithm(snake)` function where the logic of that search algorithm is defined.

---

## How to Run

### 1. Install Required Packages

Use `pip` to install the dependencies:

```bash
pip install numpy
pip install pygame==2.0.1
````

> Recommended: Run the project using **PyCharm IDE** or any Python IDE of your choice for ease of visualization.

### 2. Run the Game

Launch the game using:

```bash
python Main.py
```

You can switch between different search algorithms and compare their behavior.

---

## Key Functions

| Function                             | Purpose                                            |
| ------------------------------------ | -------------------------------------------------- |
| `run_algorithm(snake)`               | Core algorithm logic per search method             |
| `get_initstate_and_goalstate(snake)` | Extracts start (snake head) and goal (food) states |
| `manhattan_distance(nodeA, nodeB)`   | Heuristic function for A\*                         |
| `euclidean_distance(nodeA, nodeB)`   | Alternative heuristic                              |
| `get_path(node)`                     | Reconstructs the path from goal to start           |
| `inside_body(snake, node)`           | Checks collision with snake body                   |
| `outside_boundary(node)`             | Checks collision with game boundary                |
| `get_neighbors(node)`                | Returns adjacent nodes (up/down/left/right)        |

---

## Educational Context

This project was developed as part of an AI course to apply classic search techniques in a game environment. The agent shows how AI planning can be integrated into simple, interactive systems.
