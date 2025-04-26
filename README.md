# The-salesman-problem-greedily
The salesman problem greedily - shortest edges

A credit project for the subject "Heuristic Methods".

A simple desktop application written in Python with a graphical user interface built using the tkinter library.
The application searches for the shortest route between a set of points on a plane, starting and ending at the same point.
The minimum number of points required is 4.

The path is determined using a greedy algorithm, which selects the shortest available paths between points without revisiting any point and ensures that all points are visited.
Users can manually input coordinates or automatically generate random points by pressing a dedicated button in the application.
Additionally, the application displays the selected edges in the order of their inclusion in the solution, sorted by their length from the shortest.

Technologies Used
Python 3.x,
tkinter (standard Python library),
numpy,
matplotlib

Features
Finding a path that visits all given points exactly once and returns to the start
Greedy algorithm approach for shortest path estimation
Random point generation
Graphical display of points and paths
Display of edges ordered by their length during the process

How to Run
1. Clone the repository.
2. You have two options to run the application:
a)  Launch the provided komiwojazer.exe file directly.
  (No need to have Python installed)
b)  Run the Python script manually:
  Make sure you have Python 3.10 installed.
  Make sure you have the tkinter library available (it is included by default with standard Python installation).
  Run the script:
  python code_1.py
