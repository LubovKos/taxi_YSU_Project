import sys
from typing import TextIO


class MyMap(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyMap, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Map(metaclass=MyMap):
    def __init__(self):
        self.__adj_matrix = []
        self.__adj_list = []
        self.__stops_count = 0
        self.__stops_names = {}

    def download_connection(self, f: TextIO) -> None:
        """Setting the adjacency matrix for the map"""
        contents = f.read()
        for string in contents.split("\n"):
            if len(string) != 0:
                self.__adj_matrix.append([int(i) for i in string.split()])

        for string in self.__adj_matrix:
            self.__adj_list.append([])
            index = 0
            for elem in string:
                if elem != 0:
                    self.__adj_list[-1].append(index)
                index += 1
        self.__stops_count = len(self.__adj_list)

    def download_places(self, f: TextIO) -> None:
        """Downloading places on the map"""
        contents = f.read()
        counter = 0
        for string in contents.split("\n"):
            self.__stops_names[string] = counter
            counter += 1

    def calc_distance(self, start: str, end: str) -> int:
        """Dijkstra algorithm for calculating distance"""

        start_point = self.__stops_names[start]
        end_point = self.__stops_names[end]

        used = [False] * self.__stops_count
        dist = [sys.maxsize] * self.__stops_count

        dist[start_point] = 0
        for i in range(0, self.__stops_count):
            curr = -1
            for j in range(0, self.__stops_count):
                if used[j] is False and (curr == -1 or dist[j] < dist[curr]):
                    curr = j
            if dist[curr] == sys.maxsize:
                break
            used[curr] = True
            for to in range(0, self.__stops_count):
                if self.__adj_matrix[curr][to] == 0:
                    continue
                length = self.__adj_matrix[curr][to]
                if dist[curr] + length < dist[to]:
                    dist[to] = dist[curr] + length
        return dist[end_point]
