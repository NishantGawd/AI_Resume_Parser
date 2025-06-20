import pandas as pd
import json

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)