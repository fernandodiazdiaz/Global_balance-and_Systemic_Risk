def adjacency_matrix(obj):
    """
    Converts a NetworkX graph to an adjacency matrix if needed.
    Input:
        obj: NetworkX graph or NumPy array
    Output:
        A: adjacency matrix (NumPy array)
    """
    if isinstance(obj, nx.Graph):
        return nx.to_numpy_array(obj)
    elif isinstance(obj, np.ndarray):
        return obj
    else:
        raise ValueError("Input must be a NetworkX graph or a NumPy array")


def global_balance(obj):
    """
    Computes the Estrada-Benzi index (global balance) of a signed network.
    Input:
        obj: NetworkX graph or NumPy array
    Output:
        EB: Estrada-Benzi balance index
    """
    
    A = adjacency_matrix(obj)
    A_abs = np.abs(A)
    Comm = expm(A)
    Comm_abs = expm(A_abs)
    return np.trace(Comm) / np.trace(Comm_abs)
    

def local_balance(obj):   
    """
    Computes the local balance of every node in a signed network.
    Input:
        obj: NetworkX graph or NumPy array
    Output:
        Ki: dict with the local balance of every node
    """

    A = adjacency_matrix(obj)
    A0 = np.abs(A)
    
    Comm = la.expm(A)
    Comm0 = la.expm(A0)
    
    # calculate balance
    Ki = np.diag(Comm)/np.diag(Comm0)       # node balance
    
    # convert to dict
    Ki = {node: Ki[index] for index, node in enumerate(G.nodes())}
    
    return Ki


