import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    #pass
    pos_enc = np.concatenate((np.zeros((1, d_model)), np.ones((seq_len-1, d_model))), axis=0)
    pos_enc = np.cumsum(pos_enc, axis=0)

    print(pos_enc)
                             
    for idx in range(0, d_model, 2):
        dim_vector = np.copy(pos_enc[:, idx]) #DO NOT FORGET THE COPY
        pos_enc[:, idx] = np.sin(dim_vector / np.pow(base, idx/d_model))
        if (idx + 1) < d_model:
            pos_enc[:, idx + 1] = np.cos(dim_vector / np.pow(base, idx/d_model))
    
    return pos_enc
    
    