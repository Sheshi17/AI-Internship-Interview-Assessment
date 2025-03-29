import pandas as pd

import matplotlib.pyplot as plt

def analyze_results(results):
    df = pd.DataFrame([{
        "language": r["patient"]["language"],
        "channel": r["patient"]["channel"],
        "age_group": r["patient"]["age_group"],
        "responded": r["responded"]
    } for r in results])
    
    for metric in ['language', 'channel', 'age_group']:
        plt.figure()
        df.groupby(metric)['responded'].mean().sort_values().plot.barh(title=f'Response by {metric}')
        plt.xlabel("Response Rate")
        plt.tight_layout()
    plt.show()