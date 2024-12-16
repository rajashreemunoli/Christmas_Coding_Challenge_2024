#Leetcode 183. Customers Who Never Order


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    non_ordering_customers=customers[~customers['id'].isin(orders['customerId'])][['name']]
    non_ordering_customers.columns=['Customers']
    return pd.DataFrame(non_ordering_customers)

if __name__ == "__main__":
    customers=pd.DataFrame({
        "id":[1,2,3,4],
        "name":['Joe', 'Henry', 'Sam', 'Max']
    })

    orders=pd.DataFrame({
        "id": [1,2],
        "customerId":[3,1]
    })

    result=find_customers(customers, orders)
    print(result)
