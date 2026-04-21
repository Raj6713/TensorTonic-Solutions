def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    print(values)
    print(degree)
    outputs = []
    for item in values:
        outputs.append([item**i for i in range(degree+1)])
    return outputs
    
    # Write code here