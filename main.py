import json
import pandas as pd
import functions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data_json = json.load(open("data.json", 'r'))

for variant in data_json.keys():
    print(f"{variant}: ")
    data = data_json.get('a')
    print(pd.DataFrame(data))

    bool_data = functions.prepros(data)
    print(pd.DataFrame(bool_data))

    df = pd.DataFrame(bool_data)

    frequent_itemsets = apriori(df, min_support=0.3)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    print("Частые наборы элементов:")
    print(frequent_itemsets)

    print("\nПравила ассоциации:")
    print(rules)

    print("=========================================")












