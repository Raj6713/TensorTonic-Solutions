import pandas as pd
def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    model = pd.DataFrame(models)
    model['latency'] = -model['latency']
    model = model.sort_values(by=["accuracy", 'latency', 'timestamp'], ascending=False)
    max_accuracy = max(model['accuracy'])
    max_data = model[model['accuracy']==max_accuracy]
    print(max_data)
    # if len(max_data)==1:
    return list(max_data['name'])[0]
    # else:
        # return list(max_data[""])
    