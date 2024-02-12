#!/usr/bin/env python3
"""
Author: Vikram Nithyanandam

Description:
The following implementation is a robust unweighted Graph data structure
implemented using an adjacency matrix. This vertices and edges of this graph can be
effectively initialized and modified while storing your chosen generic
value in each vertex.

Adjacency Matrix: https://mathworld.wolfram.com/AdjacencyMatrix.html

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


class GraphAdjacencyMatrix(Generic[T]):
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
        self.directed = directed
        self.vertex_to_index: dict[T, int] = {}
        self.adj_matrix: list[list[int]] = []

        # Falsey checks
        edges = edges or []
        vertices = vertices or []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                msg = f"Invalid input: {edge} must have length 2."
                raise ValueError(msg)
            self.add_edge(edge[0], edge[1])

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

        # Get the indices of the corresponding vertices and set their edge value to 1.
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_matrix[v][u] = 1

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

        # Get the indices of the corresponding vertices and set their edge value to 0.
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 0
        if not self.directed:
            self.adj_matrix[v][u] = 0

    def add_vertex(self, vertex: T) -> None:
        """
        Adds a vertex to the graph. If the given vertex already exists,
        a ValueError will be thrown.
        """
        if self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} already exists in this graph."
            raise ValueError(msg)

        # build column for vertex
        for row in self.adj_matrix:
            row.append(0)

        # build row for vertex and update other data structures
        self.adj_matrix.append([0] * (len(self.adj_matrix) + 1))
        self.vertex_to_index[vertex] = len(self.adj_matrix) - 1

    def remove_vertex(self, vertex: T) -> None:
        """
        Removes the given vertex from the graph and deletes all incoming and
        outgoing edges from the given vertex as well. If the given vertex
        does not exist, a ValueError will be thrown.
        """
        if not self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} does not exist in this graph."
            raise ValueError(msg)

        # first slide up the rows by deleting the row corresponding to
        # the vertex being deleted.
        start_index = self.vertex_to_index[vertex]
        self.adj_matrix.pop(start_index)

        # next, slide the columns to the left by deleting the values in
        # the column corresponding to the vertex being deleted
        for lst in self.adj_matrix:
            lst.pop(start_index)

        # final clean up
        self.vertex_to_index.pop(vertex)

        # decrement indices for vertices shifted by the deleted vertex in the adj matrix
        for vertex in self.vertex_to_index:
            if self.vertex_to_index[vertex] >= start_index:
                self.vertex_to_index[vertex] = self.vertex_to_index[vertex] - 1

    def contains_vertex(self, vertex: T) -> bool:
        """
        Returns True if the graph contains the vertex, False otherwise.
        """
        return vertex in self.vertex_to_index

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

        u = self.vertex_to_index[source_vertex]
        v = self.vertex_to_index[destination_vertex]
        return self.adj_matrix[u][v] == 1

    def clear_graph(self) -> None:
        """
        Clears all vertices and edges.
        """
        self.vertex_to_index = {}
        self.adj_matrix = []

    def __repr__(self) -> str:
        first = "Adj Matrix:\n" + pformat(self.adj_matrix)
        second = "\nVertex to index mapping:\n" + pformat(self.vertex_to_index)
        return first + second