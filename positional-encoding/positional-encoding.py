import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    output = np.zeros((seq_len, d_model))
    rows = np.arange(seq_len)[:,np.newaxis]
    columns = np.arange(d_model)[np.newaxis,:]
    angle_rates = 1 / np.power(base, (2 * (columns // 2)) / d_model)
    angle = rows*angle_rates
    print(angle.shape, output.shape)

    output[:,0::2] = np.sin(angle[:, 0::2])
    output[:,1::2] = np.cos(angle[:, 1::2])
    return output
    