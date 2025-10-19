import pandas as pd

def test_columns_exist():
    df = pd.read_csv("data/iris.csv")
    expected = {"sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)","target"}
    assert expected.issubset(df.columns), "Missing expected columns!"

def test_no_nulls():
    df = pd.read_csv("data/iris.csv")
    assert not df.isnull().values.any(), "Dataset contains null values!"
