import pandas as pd

def transform_users(user_iterator):
    records = []

    for user in user_iterator:
        records.append({
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]
        })

    dataframe = pd.DataFrame(records)

    dataframe["name_length"] = dataframe["name"].str.len()
    dataframe["email_domain"] = dataframe["email"].str.split("@").str[-1]
    dataframe["city_upper"] = dataframe["city"].str.upper()

    return dataframe

def summarize_users(dataframe):
    return dataframe.groupby("city").size().reset_index(name="user_count")