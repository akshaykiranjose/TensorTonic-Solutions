coords = [[0]*n_dim]*k 
causes a trip because a shallow copy is created instead of separate memory and that means when the first element [0,0,0] is modified, that also modifies the other elements in the list.



coords = [[0]*n_dim for _ in range(k)] works cause the elements in the nested list are immutable