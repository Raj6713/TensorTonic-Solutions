import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    print(locals())
    param = np.asarray(param)
    grad = np.asarray(grad)
    m = np.asarray(m)
    v = np.asarray(v)
    m_t = beta1*m+ (1-beta1)*grad
    v_t = beta2*v+(1-beta2)*grad*grad
    _m_t = m_t/(1-beta1**t)
    _v_t = v_t/(1-beta2**t)
    param = param - lr * ( _m_t /(np.sqrt(_v_t)+eps))
    return param, m_t, v_t