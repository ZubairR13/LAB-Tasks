class WaterJugDFS:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited = set()
        self.path = []

    def is_valid(self, state):
        return (0 <= state[0] <= self.jug1_capacity and
                0 <= state[1] <= self.jug2_capacity)

    def dfs(self, state):
        if state in self.visited:
            return False
        
        self.visited.add(state)
        self.path.append(state)
        
        j1, j2 = state
        
        if j1 == self.target or j2 == self.target:
            return True
        
        moves = [
            ((self.jug1_capacity, j2), "Fill Jug 1"),
            ((j1, self.jug2_capacity), "Fill Jug 2"),
            ((0, j2), "Empty Jug 1"),
            ((j1, 0), "Empty Jug 2"),
            ((max(0, j1 - (self.jug2_capacity - j2)), min(self.jug2_capacity, j1 + j2)), "Pour Jug 1 -> Jug 2"),
            ((min(self.jug1_capacity, j1 + j2), max(0, j2 - (self.jug1_capacity - j1))), "Pour Jug 2 -> Jug 1")
        ]
        
        for new_state, rule in moves:
            if self.is_valid(new_state) and new_state not in self.visited:
                print(f"Applying rule: {rule}, New State: {new_state}")
                if self.dfs(new_state):
                    return True
                
        self.path.pop()
        return False
    
    def solve(self):
        initial_state = (0, 0)
        if self.dfs(initial_state):
            print("Solution Path:")
            for state in self.path:
                print(state)
        else:
            print("No solution found.")

jug1_capacity = 4
jug2_capacity = 3
target = 2
solver = WaterJugDFS(jug1_capacity, jug2_capacity, target)
solver.solve()
