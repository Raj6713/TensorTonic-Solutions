import numpy as np
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    print(prob_distributions)
    print(actual_tokens)
    pi = [pr[t] for pr,t in zip(prob_distributions, actual_tokens)]
    H = -np.sum(np.log(np.asarray(pi)))/len(pi)
    return np.exp(H)
    
    