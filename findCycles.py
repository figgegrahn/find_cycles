#!/usr/bin/env python

"""
dot_find_cycles.py - uses Pydot and NetworkX to find cycles in a dot file
directed graph.

By Jason Antman  2012.

Free for all use, provided that you send any changes you make back to me,
update the changelog, and keep this comment intact.

REQUIREMENTS:
Python
python-networkx -
graphviz-python -
pydot -
(all of these are available as native packages at least on CentOS)

USAGE:
dot_find_cycles.py /path/to/file.dot

The canonical source of this script can always be found from:


$HeadURL: http://svn.jasonantman.com/misc-scripts/dot_find_cycles.py $
$LastChangedRevision: 33 $

CHANGELOG:
    Wednesday 2012-03-28 Jason Antman :
        - initial script creation
"""

import sys
import os
import tempfile
import networkx as nx
import re


def translate_nodes(cycleList, dotFile):
    """
    cycleList is a list containing arrays of cycles
    path is the dot-file to translate 'node2040' to 'ComponentsInterface'
    looking for lines like
    "node1524" [ label="ComponentsInterface" shape="diamond"];
    """
    nodeToName = dict()

    for line in dotFile:
        m = re.search(r'\"(\w+)\" \[ label="(\w+)', line)
        if m is not None:
            nodeToName[m.group(1)] = m.group(2)

    for i in cycleList:
        thisCycle = []
        for node in i:
            thisCycle.append(nodeToName[node])
        print(thisCycle)


def usage():
    sys.stderr.write("dot_find_cycles.py by Jason Antman \n")
    sys.stderr.write("  finds cycles in dot file graphs\n")
    sys.stderr.write("USAGE: dot_find_cycles.py /path/to/file.dot\n")


def main():

    path = ""
    dotFile = []
    isTmp = False

    try:
        if len(sys.argv) > 1:
            path = sys.argv[1]
            with open(path, "r") as f:
                dotFile = f.readlines()
        else:
            dotFile = sys.stdin.readlines()
            fd, path = tempfile.mkstemp()
            isTmp = True
            with os.fdopen(fd, "w") as tmp:
                tmp.writelines(dotFile)

        # read in the specified file, create a networkx DiGraph
        G = nx.DiGraph(nx.drawing.nx_pydot.read_dot(path))
    except IOError as e:
        sys.stderr.write("ERROR: could not read file " + path + "\n" + e.what())
        usage()
        sys.exit(1)
    finally:
        if isTmp:
            os.remove(path)

    C = list(nx.simple_cycles(G))
    if len(C) < 1:
        print("No cycles found")
        sys.exit(0)

    translate_nodes(C, dotFile)


# Run
if __name__ == "__main__":
    main()
