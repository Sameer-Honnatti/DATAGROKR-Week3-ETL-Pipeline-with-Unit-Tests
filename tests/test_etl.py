import pandas as pd
import pytest
from etl.api import user_generator
from etl.transform import transform_users, summarize_users
from etl.pipeline import run_pipeline_from_data

def test_user_generator(sample_users):
    result = list(user_generator(sample_users))

    assert len(result) == 3
    assert result[0]["name"] == "John Doe"

def test_transform_users(sample_users):
    dataframe = transform_users(iter(sample_users))

    assert isinstance(dataframe, pd.DataFrame)
    assert len(dataframe) == 3
    assert "name_length" in dataframe.columns
    assert "email_domain" in dataframe.columns
    assert "city_upper" in dataframe.columns
    assert dataframe.iloc[0]["email_domain"] == "example.com"

def test_summarize_users(sample_users):
    dataframe = transform_users(iter(sample_users))
    summary = summarize_users(dataframe)

    assert set(summary.columns) == {"city", "user_count"}
    assert len(summary) == 2

def test_pipeline_from_data(sample_users):
    result = run_pipeline_from_data(sample_users)

    assert "dataframe" in result
    assert "summary" in result
    assert len(result["dataframe"]) == 3

@pytest.mark.parametrize(
    "email,expected",
    [
        ("john@example.com", "example.com"),
        ("user@gmail.com", "gmail.com"),
        ("student@outlook.com", "outlook.com")
    ]
)
def test_email_domain(email, expected):
    assert email.split("@")[-1] == expected
