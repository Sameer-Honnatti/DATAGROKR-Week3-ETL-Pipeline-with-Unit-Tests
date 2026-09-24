from pathlib import Path
import json
from .api import fetch_user_generator
from .transform import transform_users, summarize_users

OUTPUT_DIR = Path("output")

def run_pipeline():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    user_iterator = fetch_user_generator()

    dataframe = transform_users(user_iterator)

    summary = summarize_users(dataframe)

    csv_file = OUTPUT_DIR / "users_transformed.csv"
    json_file = OUTPUT_DIR / "city_summary.json"

    dataframe.to_csv(csv_file, index=False)

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(summary.to_dict("records"), file, indent=4)

    return csv_file

def run_pipeline_from_data(users):
    dataframe = transform_users(iter(users))
    summary = summarize_users(dataframe)

    return {
        "dataframe": dataframe,
        "summary": summary
    }