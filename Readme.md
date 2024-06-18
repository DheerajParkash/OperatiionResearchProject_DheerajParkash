#  Maximum Flow Minimum Cost Problem Solver

## Overview
This project aims to solve the Maximum Flow Minimum Cost problem for a graph, given in a specific text file format. The algorithms implemented include Maximum Flow, Minimum Cut, and Maximum Flow Minimum Cost.

## Files Included
1. edge.py: Defines classes AdjNode and AdjFlow which represent edges in the graph.
2. graph.py: Contains the Graph class implementing the algorithms for Maximum Flow, Minimum Cut, and Maximum Flow Minimum Cost.
3. main.py: Main script to parse the input file, create the graph, and demonstrate the algorithms.
4. inputGraph.txt: Sample input file containing the graph description in the specified format.


## Project Structure
### edge.py
    This file defines the edge classes used in the graph representation:
        * AdjNode: Represents a basic directed edge with capacity and cost.
        * AdjFlow: Extends AdjNode to include flow information, essential for flow-related algorithms.

### graph.py
    The Graph class encapsulates the graph structure and operations:
        * Initialization: Constructs a graph from an adjacency list.
        * Algorithms Implemented:
            * Maximum Flow: Uses the Ford-Fulkerson method to find the maximum amount of flow from a source to a sink.
            * Minimum Cut: Identifies edges that form the minimum cut separating the source from other nodes.
            * Maximum Flow Minimum Cost: Computes the maximum flow with the minimum possible cost using the Bellman-Ford algorithm to find shortest paths in terms of cost.

### main.py
    This script serves as the entry point and demonstrates the functionalities of the implemented algorithms:
        * Parsing Input File: Reads the graph description from inputGraph.txt.
        * Execution: Executes each algorithm on the graph and prints results.
        * Output: Displays maximum flow values, flow distributions, minimum cut edges, and maximum flow minimum cost details.

### inputGraph.txt
    Sample input file containing the graph description in the specified format:
        * Format: First line includes numNodes, numArcs, sourceNode, and sinkNode.
        * Subsequent lines describe each arc with emanatingNode, terminatingNode, maxCapacity, and cost.

## How to Use
1. Setup: Ensure Python 3.x is installed on your system.
2. Clone Repository: Clone this repository to your local machine.
3. Run the Code:
    * Open a terminal or command prompt.
    * Navigate to the directory containing the cloned repository.
    * Execute python main.py to run the program.
    * Ensure inputGraph.txt is in the same directory or specify its path accordingly.
Example Usage
    python main.py