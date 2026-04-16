import pandas as pd

def save_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def save_to_json(data, path):
    import json
    with open(path, "w") as f:
        json.dump(data, f, indent=4)