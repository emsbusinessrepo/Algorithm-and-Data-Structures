"""
Name: Soh En Ming
Student ID: 32024975
Title: FIT2004 S1/2022: Assignment 2
Unit Code: FIT2004

This assignment was done on Python Version 3.9.2.
"""
"""
1 Location Optimisation (4 marks + 1 mark for documentation)
"""
def ideal_place(relevant):
    """
        This function takes inputs which is sets of n relevant points and uses the relevant points to find one
        optimal solution which is in a array that shows the x coordinates, and y coordinates of the optimal
        intersection.
        Written by Soh En Ming

        Precondition: A set of arrays which contains the n relevant points of all intersections in the grid.
        Postcondition: An array which contains x coordinates and y coordinates of the optimal intersection/solution

        Input:
            relevant: relevant = [[5,8], [7,5], [9, 1], [0,7], [1,9], [2,1]]
        Return:
            answer: [5, 7]

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n). How I ended up with this complexity is because inside the function ideal_place, it calls out
            another function which is location_mid and for that function, the total complexity is O(n) therefore the
            total complexity will be O(n)
        Space complexity:
            Input: O(n)
            Aux: O(1) since no new array has been created in this function.
    """
    optimal_solution = [location_mid(relevant, 0), location_mid(relevant, 1)]
    return optimal_solution

def location_mid(relevant, axis_idx):
    """
        This function basically seperates the axis from the array of relevant points. So depending on which axis
        index is selected, 0 for x and 1 for y axis it will append the values of all the different axis points and
        put them into a array where it will be called by median of median function to find the optimal point for the
        x axis or y axis.
        Written by Soh En Ming

        Precondition: A set of arrays which contains the n relevant points of all intersections in the grid and the
        axis index of the x coordinates and y coordinates.
        Postcondition: A integer which contains the value of x coordinate or y coordinate for the optimal
        solution.

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n). How I ended up with this complexity is because in this function there is a for loop which
            has the complexity of O(n), n for the length of the relevant points array and there is another function
            which is being called out in this function which has a complexity of O(n) but since it's not inside the
            for loop, the total final complexity will be O(n).
        Space complexity:
            Input: O(n)
            Aux: O(n) this is because there is a new array created. Despite being empty, later in the code it will
            be appended with values which takes space and causes the auxiliary space complexity to be O(n)
    """
    arr_on_axis = []
    for idx in range(len(relevant)):
        arr_on_axis.append(relevant[idx][axis_idx])
    new_arr_len = len(arr_on_axis)
    if new_arr_len == 1:
        return arr_on_axis[len(relevant) // 2]
    val = median_of_medians(arr_on_axis)
    return val

def median_of_medians(arr):
    """
        This function is an algorithm called median of medians. It is used to select an approximate median to be used
        as a pivot for partitioning.
        Written by Soh En Ming

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n). How I ended up with this complexity is because the function select_pivot() has a complexity of
            O(n) therefore the total complexity will be O(n).
        Space complexity:
            Input: O(1)
            Aux: O(1)
    """
    if len(arr) == 0 or arr is None:
        return None
    return select_pivot(arr, len(arr) // 2)

def select_pivot(arr, k):
    """
        This function is used to select a pivot which is corresponding to the kth largest element in the array and is
        used to find the median of medians.
        Written by Soh En Ming

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n). How I ended up with this complexity is because of a few reasons. Firstly, there is 3 for loops
            in this function however, they all are seperate and not within a for loop. Therefore, the complexity is
            O(n). However for the 2nd for loop, inside has a function which is sorted. Normally the complexity would be
            n log n along with the for loop however, since the array has been split into 5 different sublists, it can
            get the optimal running time causing the complexity to be O(n) for the 2nd for loop. In total the complexity
            will be O(n)
        Space complexity:
            Input: O(n)
            Aux: O(1)
    """
    sublist = [arr[i:i+5] for i in range(0, len(arr), 5)]
    sorted_sublists = [sorted(chunk) for chunk in sublist]
    medians = [chunk[len(chunk) // 2] for chunk in sorted_sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select_pivot(medians, len(medians) // 2)

    p = partition(arr, pivot)

    if k == p:
        return pivot
    if k < p:
        return select_pivot(arr[0:p], k)
    else:
        return select_pivot(arr[p+1:len(arr)], k - p - 1)


def partition(arr, pivot):
    """
        This function is used as a partition for the median. Where it will partition the array around the given
        pivot.
        Written by Soh En Ming

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n). How I ended up with this complexity is because there is a while loop which has a complexity
            of O(n), which n is from the length of the array.
        Space complexity:
            Input: O(1)
            Aux: O(1)
    """
    left = 0
    right = len(arr) - 1
    i = 0

    while i <= right:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left

"""
2 On The Way (4 marks + 1 mark for documentation)
"""
"""
MinHeap Class which will be used in Task 2
"""
class MinHeap:
    """
    This is just a simple created MinHeap class which is used as a helper for Dijkstra algorithm to find shortest
    path.
    """
    def __init__(self) -> None:
        """
        This function is used to instantiate size, array and position.
        Written by Soh En Ming

        Time complexity: O(1)
        """
        self.size = 0
        self.array = []
        self.position = []

    def emptyHeap(self):
        """
            This function is used to check whether the heap is empty or not. If it is it will
            return True else it will return false.
            Written by Soh En Ming

            Time complexity: O(1)
        """
        if self.size == 0:
            return True
        else:
            return False

    def swapNode(self, node1, node2):
        """
            This function is used to swap between the different nodes.
            Written by Soh En Ming

            Time complexity: O(1)
        """
        arr = self.array
        arr[node1], arr[node2] = arr[node2], arr[node1]

    def new_heap_node(self, vertx, distance):
        """
            This function is used to create a new heap node.
            Written by Soh En Ming

            Time complexity: O(1)
        """
        heap_node = [vertx, distance]
        return heap_node

    def heap_extract_min(self):
        """
            This function is used extract the smallest/minimum heap value
            Written by Soh En Ming

            Time complexity: O(1)
        """
        arr = self.array
        position = self.position
        min = arr[0]
        lnode = arr[self.size -1]
        arr[0] = lnode

        position[lnode[0]] = 0
        position[min[0]] = self.size - 1

        self.size -= 1
        self.heapify(0)
        return min

    def left(self, i):
        """
            This function is used to find the left node
            Written by Soh En Ming

            Time complexity: O(1)
        """
        return 2 * i + 1

    def right(self, i):
        """
            This function is used to find the right node
            Written by Soh En Ming

            Time complexity: O(1)
        """
        return self.left(i) + 1

    def heapify(self, i):
        """
            This function is used to heapify the given index and this function also updates the
            position of the nodes when swapped.
            Written by Soh En Ming

            Time complexity: O(1)
        """
        n = self.size
        l = self.left(i)
        r = self.right(i)
        arr = self.array
        position = self.position
        smallest = i
        if l < n and arr[l][1] < arr[smallest][1]:
            smallest = l

        if r < n and arr[r][1] < arr[smallest][1]:
            smallest = r

        if smallest != i:
            position[arr[smallest][0]] = i
            position[arr[i][0]] = smallest

            self.swapNode(i, smallest)
            self.heapify(smallest)

    def parent(self, n):
        """
            This function is used to get the parent index
            Written by Soh En Ming

            Time complexity: O(1)
        """
        return (n - 1) // 2

    def decrease(self, vertx, distance):
        """
            This function is used to travel up the tree while the heap has not been heapified yet and also
            swaps the node with it's parent.
            Written by Soh En Ming

            Time complexity: log(n)
        """
        arr = self.array
        position = self.position
        parent = self.parent(position[vertx])
        n = position[vertx]
        arr[n][1] = distance

        while arr[n][1] < arr[parent][1] and n > 0:
            position[arr[n][0]] = parent
            position[arr[parent][0]] = n
            self.swapNode(n, parent)
            n = parent

    def in_heap(self, vertx):
        """
            This function is used as a utility function to verify whether the vertex 'vertx' is in the
            min heap or not.
            Written by Soh En Ming

            Time complexity: O(1)
        """
        position = self.position
        if position[vertx] < self.size:
            return True
        else:
            return False
"""
RoadGraph class which is used to calculate the problem
"""
class RoadGraph:
    """
    In this class RoadGraph, it contains all the functions to get the desired optimal route outcome.
    """
    def __init__(self, roads):
        """
        This function takes inputs which are list of tuples and is created into a graph using the values. In this
        function it instianties total_verticies and the roadgraph from adjacency_lst function.
        Written by Soh En Ming

        Precondition: A list of tuples which contains the values of the vertex, and the distance value in between.
        Postcondition: If ran using the code, RoadGraph(roads) it would create a graph which can be used to find the
        best optimal route using another function in the same class.

        Input:
            roads: roads = [(0,1,4), (0,3,2), (0,2,3), (2,3,2), (3,0,3)]

        Time complexity
            Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
            complexity will be the same.
            Worst: O(n). How I ended up with this complexity is because of the functions which have been called, they
            all have complexity of O(n) however since they aren't being called within the loop the complexity can
            only be O(n).
        Space complexity:
            Input: O(1)
            Aux: O(1)
        """
        self.total_vertices = self.total_vertices(roads)
        self.roadgraph, self.rear_roadgraph = self.adjacency_lst(roads)

    def adjacency_lst(self, arr):
        """
            This function is used to find the values of vertices in the adjacency list in the front and the rear.
            Written by Soh En Ming

            Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(n). How I ended up with this complexity is because there is nothing inside the while loop that
                can make the complexity turn into O(log n) therefore the final complexity will be O(n)
            Space complexity:
                Input: O(n)
                Aux: O(n). This is because there is extra arrays which are being used.
        """
        Verticies = self.total_vertices
        adjacency_lst = [None] * Verticies
        r_adjacency_lst = [None] * Verticies
        while arr != []:
            present = arr.pop()
            if adjacency_lst[present[0]] == None:
                adjacency_lst[present[0]] = [[present[1], present[2]]]
            elif adjacency_lst[present[0]] != None:
                adjacency_lst[present[0]].extend([[present[1], present[2]]])

            if r_adjacency_lst[present[1]] == None:
                r_adjacency_lst[present[1]] = [[present[0], present[2]]]
            elif r_adjacency_lst[present[1]] != None:
                r_adjacency_lst[present[1]].extend([[present[0], present[2]]])
        return adjacency_lst, r_adjacency_lst


    def total_vertices(self, arr):
        """
            This function is used to find the total number of locations/vertices in the graph.
            Written by Soh En Ming

            Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(n). How I ended up with this complexity is because there is a for loop which has been used
                and it has a complexity of O(n) where n is the array length.The rest only has a complexity of O(1).
                Therefore the total final complexity will be O(n)
            Space complexity:
                Input: O(n)
                Aux: O(1)
        """
        total = 0
        arr_len = len(arr)
        if arr == None:
            pass
        else:
            for idx in range(arr_len):
                if total < arr[idx][1]:
                    total = arr[idx][1]
                elif total < arr[idx][0]:
                    total = arr[idx][0]
            total = total + 1
        return total

    def routing(self, start, end, chores_location):
        """
            This function takes inputs which is the start location vertex, end location vertex, the different chores
            location in the graph which the optimal route must take one of them. Then the function uses the inputs
            to find an optimal route which contains the least total distance based on the inputs and the chores
            allocated in the function.
            Written by Soh En Ming

            Precondition: A integer which contains the value of which location the routing is supposed to start, a
            integer which contains the value of which location the routing is supposed to end and lastly an array
            which contains the values of the chores location.
            Postcondition: An array which contains x coordinates and y coordinates of the optimal intersection/solution

            Input:
                start: start = 0
                end: end = 1
                chores_location: chores_location = [2,3]
            Return:
                answer: [0, 3, 0, 1]

            Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(ElogV). How I ended up with this complexity is because of the different functions which are
                contained inside the function routing. The dijkstra function contains a complexity of O(ElogV). The
                optimal_location function contains a complexity of O(n). The while loop inside the routing function only
                has a complexity of O(n). Therefore if we combine all the complexity together, the worse case complexity
                for this function is O(ElogV).
            Space complexity:
                Input: O(VE)
                Aux: O(VE)
        """
        route_dist, pred_route = self.dijkstra(self.roadgraph, start)
        r_route_dist, rear_pred_route = self.dijkstra(self.rear_roadgraph, end)
        best_route = None
        best_location = self.optimal_location(chores_location, route_dist, pred_route, r_route_dist, rear_pred_route)

        if best_location != None:
            i = best_location
            j = best_location
            f_route_list = []
            b_route_list = []
            while pred_route[i] != start:
                f_route_list.append(pred_route[i])
                i = pred_route[i]

            while rear_pred_route[j] != end:
                b_route_list.append(rear_pred_route[j])
                j = rear_pred_route[j]
            best_route = [start]

            while f_route_list != []:
                best_route.append(f_route_list.pop())
            best_route.append(best_location)

            while b_route_list != []:
                best_route.append(b_route_list.pop(0))
            best_route.append(end)

        return best_route

    def optimal_location(self, chores_location, route_dist, pred_route, r_route_dist, rear_pred_route):
        """
            This function is used to find the optimal location of where the best chore is located at from the graph.
            Written by Soh En Ming

            Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(n). How I ended up with this complexity is because there is for loops which contain a
                 complexity of O(n) where n is the values inside chores location and another for loop which has a
                 complexity of O(m) where m is the value of inside the possible locations. Howvever, since there is
                 no for loop inside another for loop, the complexity can only be O(n). Therefore, the final total
                 complexity will be O(n)
            Space complexity:
                Input: O(n)
                Aux: O(n). Since there was array that was appended
        """
        optimal_location = None
        possible_locations = []
        for i in chores_location:
            if rear_pred_route[i] != None and pred_route[i] != None:
                possible_locations.append(i)

        if possible_locations != []:
            optimal_location = possible_locations[0]
            optimal_location_distance = route_dist[optimal_location] + r_route_dist[optimal_location]
            for i in possible_locations:
                if optimal_location_distance > (r_route_dist[i] + route_dist[i]):
                    optimal_location = i
                    optimal_location_distance = route_dist[i] + r_route_dist[i]

        return optimal_location


    def dijkstra(self, roadgraph, begin):
        """
            This function is an algorithm which is called dijkstra. It has been modified to use the MinHeap class
            that I've created earlier and it will be used to find the shortest path in graph using the adjacency
            list.
            Written by Soh En Ming

            Time complexity
                Best: Since there is no fast exit or any way to make the algorithm go faster, both the best and worst case
                complexity will be the same.
                Worst: O(ELogV). How I ended up with this complexity is because there is a for loop which has a
                complexity of O(V + E) where V is the length of vertices and because of min heap class, the decrease
                function also has a complexity of O(log v) and because the decrease was inside an inner loop, the
                complexity will become O(ElogV). Therefore, the final complexity is O(ElogV).
            Space complexity:
                Input: O(VE)
                Aux: O(VE). Since there was array that was appended
        """
        Verticies = self.total_vertices
        path_lst = Verticies * [float('inf')]
        path_lst[begin] = 0
        suggest_list = Verticies * [None]

        heap = MinHeap()

        for verticies in range(Verticies):
            heap.array.append(heap.new_heap_node(verticies, path_lst[verticies]))
            heap.position.append(verticies)

        heap.position[begin] = begin
        path_lst[begin] = 0
        heap.decrease(begin, path_lst[begin])
        heap.size = Verticies

        while heap.emptyHeap() == False:
            new_node = heap.heap_extract_min()
            extracted_vrtx = new_node[0]

            if roadgraph[extracted_vrtx] != None:
                for i in roadgraph[extracted_vrtx]:
                    shortest_d_v = i[0]
                    if heap.in_heap(shortest_d_v) and i[1] + path_lst[extracted_vrtx] < path_lst[shortest_d_v]:
                        path_lst[shortest_d_v] = i[1] + path_lst[extracted_vrtx]
                        suggest_list[shortest_d_v] = extracted_vrtx
                        heap.decrease(shortest_d_v, path_lst[shortest_d_v])
        return path_lst, suggest_list
