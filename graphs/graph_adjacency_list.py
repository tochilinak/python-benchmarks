#!/usr/bin/env python3
"""
Author: Vikram Nithyanandam

Description:
The following implementation is a robust unweighted Graph data structure
implemented using an adjacency list. This vertices and edges of this graph can be
effectively initialized and modified while storing your chosen generic
value in each vertex.

Adjacency List: https://en.wikipedia.org/wiki/Adjacency_list

Potential Future Ideas:
- Add a flag to set edge weights on and set edge weights
- Make edge weights and vertex values customizable to store whatever the client wants
- Support multigraph functionality if the client wants it
"""
from __future__ import annotations

import random
import unittest
from pprint import pformat
from typing import Generic, TypeVar

T = TypeVar("T")


class GraphAdjacencyList(Generic[T]):
    def __init__(
        self, vertices: list[T], edges: list[list[T]], directed: bool = True
    ) -> None:
        """
        Parameters:
         - vertices: (list[T]) The list of vertex names the client wants to
        pass in. Default is empty.
        - edges: (list[list[T]]) The list of edges the client wants to
        pass in. Each edge is a 2-element list. Default is empty.
        - directed: (bool) Indicates if graph is directed or undirected.
        Default is True.
        """
        self.adj_list: dict[T, list[T]] = {}  # dictionary of lists of T
        self.directed = directed

        # Falsey checks
        edges = edges or []
        vertices = vertices or []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                msg = f"Invalid input: {edge} is the wrong length."
                raise ValueError(msg)
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, vertex: T) -> None:
        """
        Adds a vertex to the graph. If the given vertex already exists,
        a ValueError will be thrown.
        """
        if self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} is already in the graph."
            raise ValueError(msg)
        self.adj_list[vertex] = []

    def add_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Creates an edge from source vertex to destination vertex. If any
        given vertex doesn't exist or the edge already exists, a ValueError
        will be thrown.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge already exists between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        # add the destination vertex to the list associated with the source vertex
        # and vice versa if not directed
        self.adj_list[source_vertex].append(destination_vertex)
        if not self.directed:
            self.adj_list[destination_vertex].append(source_vertex)

    def remove_vertex(self, vertex: T) -> None:
        """
        Removes the given vertex from the graph and deletes all incoming and
        outgoing edges from the given vertex as well. If the given vertex
        does not exist, a ValueError will be thrown.
        """
        if not self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} does not exist in this graph."
            raise ValueError(msg)

        if not self.directed:
            # If not directed, find all neighboring vertices and delete all references
            # of edges connecting to the given vertex
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
        else:
            # If directed, search all neighbors of all vertices and delete all
            # references of edges connecting to the given vertex
            for edge_list in self.adj_list.values():
                if vertex in edge_list:
                    edge_list.remove(vertex)

        # Finally, delete the given vertex and all of its outgoing edge references
        self.adj_list.pop(vertex)

    def remove_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Removes the edge between the two vertices. If any given vertex
        doesn't exist or the edge does not exist, a ValueError will be thrown.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if not self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge does NOT exist between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        # remove the destination vertex from the list associated with the source
        # vertex and vice versa if not directed
        self.adj_list[source_vertex].remove(destination_vertex)
        if not self.directed:
            self.adj_list[destination_vertex].remove(source_vertex)

    def contains_vertex(self, vertex: T) -> bool:
        """
        Returns True if the graph contains the vertex, False otherwise.
        """
        return vertex in self.adj_list

    def contains_edge(self, source_vertex: T, destination_vertex: T) -> bool:
        """
        Returns True if the graph contains the edge from the source_vertex to the
        destination_vertex, False otherwise. If any given vertex doesn't exist, a
        ValueError will be thrown.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} "
                f"or {destination_vertex} does not exist."
            )
            raise ValueError(msg)

        return destination_vertex in self.adj_list[source_vertex]

    def clear_graph(self) -> None:
        """
        Clears all vertices and edges.
        """
        self.adj_list = {}

    def __repr__(self) -> str:
        return pformat(self.adj_list)