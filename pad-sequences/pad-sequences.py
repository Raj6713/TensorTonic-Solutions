import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    maxi = max([len(item) for item in seqs])
    if max_len is None:
        maximum = maxi
    else:
        maximum = max_len
    for i in range(len(seqs)):
        if len(seqs[i])>=maximum:
            seqs[i]=seqs[i][:maximum]
        else:
            new_item = seqs[i]+[pad_value]*(maximum-len(seqs[i]))
            seqs[i]=new_item
    return seqs
    