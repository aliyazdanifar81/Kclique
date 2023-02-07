class Graph:
    def __init__(self):
        self.edges = list()
        my_file = open("graph.txt", "r")  # text file is open and ready to read
        self.nod_number = int(my_file.readline())
        self.cliquenumber = int(my_file.readline())
        for i in range(self.nod_number):  # make Adjacency Matrix and initilize it with 0
            self.edges.append([0] * self.nod_number)
        for i in my_file:
            edge = i.strip()  # make the edges
            edge = edge.split()
            row = int(edge[0]) - 1
            column = int(edge[1]) - 1
            self.edges[row][column] = 1
            self.edges[column][row] = 1
        my_file.close()  # close the text file

    def __serch_for_ind__(self, ilist, column):
        for i in ilist:
            if self.edges[i - 1][column] != 0:
                return 0
        return 1

    def __search_in_tl__(self, _list, row):
        for i in _list:
            if i == row:
                return 0
        return 1

    def __search_in_res__(self, _list, new_list):
        for i in _list:
            if i == new_list:
                return 0
        return 1

    def MIS(self):  # Max Independent Set
        i, j = 0, 0
        temp_matrix = self.edges
        temp_list, result, stack = list(), list(), list()
        while i < self.nod_number:
            while j < self.nod_number:
                if i != j:
                    if temp_matrix[i][j] == 0:
                        if self.__serch_for_ind__(temp_list, i) and self.__search_in_tl__(temp_list, i + 1):
                            temp_list.append(i + 1)
                        if len(temp_list) > 1 and self.__search_in_res__(result, sorted(temp_list)):
                            result.append(sorted(temp_list.copy()))
                        stack.append([i, j])
                        i = j
                else:
                    if temp_matrix[i][j] == 0:
                        temp_list.append(i + 1)
                        result.append([i + 1])
                j += 1
            if stack:
                i = stack[-1][0]
                j = stack[-1][1] + 1
                if len(temp_list) == len(stack):
                    temp_list.pop()
                stack.pop()

            else:
                i += 1
                j = 0
                temp_list.clear()
        result = sorted(result)
        print(sorted(result, key=len))
        print(len(result))

    def clique(self):
        temp_list, result, temp_result = self.edges, list(), list()
        i, j = 0, 0
        clique_counter = 2
        while i < self.nod_number:
            while j < self.nod_number:
                if temp_list[i][j] == 1:
                    result.append(sorted([i + 1, j + 1]))
                j += 1
            i += 1
            j = i
        while clique_counter < self.cliquenumber:
            i, j = 0, 1
            len_res = len(result)
            while i < len_res:
                while j < len_res:
                    my_set = set(result[i] + result[j])
                    undup_var = [list(set(result[i]) - set(result[j])), list(set(result[j]) - set(result[i]))]
                    if len(my_set) == clique_counter + 1:
                        my_set = list(my_set)
                        if temp_list[undup_var[0][0] - 1][undup_var[1][0] - 1] == 1 and self.__search_in_res__(temp_result,
                                                                                                   my_set):
                            temp_result.append(my_set.copy())
                    j += 1
                i += 1
                j = i + 1
            result.clear()
            result = temp_result.copy()
            temp_result.clear()
            clique_counter += 1
        print(result)
        print(len(result))

    def print(self):
        for i in self.edges:
            print(i)


a = Graph()
a.clique()
