import os
import pandas as pd
import polars as pl
from main import (
    load_data,
    load_data_pl,
    calculate_statistics,
    calculate_statistics_pl,
    create_histogram_pl,
    benchmark_pandas_vs_polars,
)

file_path = "rdu-weather-history.csv"


# Test Pandas functions
def test_load_data():
    """Function to test the load_data function (Pandas)."""
    data = load_data(file_path)
    assert not data.empty, "Loaded data should not be empty"
    assert isinstance(data, pd.DataFrame), "Loaded data should be a DataFrame"


def test_calculate_statistics():
    """Function to test the calculate_statistics function (Pandas)."""
    data = load_data(file_path)
    stats = calculate_statistics(data)

    # Assert statements to check the calculated values against the expected values
    assert (
        abs(stats.at["mean", "Temperature Minimum"] - 44.225166) < 1e-6
    ), "Mean of Temperature Minimum is incorrect"
    assert (
        abs(stats.at["median", "Temperature Minimum"] - 45.000000) < 1e-6
    ), "Median of Temperature Minimum is incorrect"
    assert (
        abs(stats.at["std_dev", "Temperature Minimum"] - 14.538763) < 1e-6
    ), "Standard deviation of Temperature Minimum is incorrect"

    assert (
        abs(stats.at["mean", "Temperature Maximum"] - 66.966887) < 1e-6
    ), "Mean of Temperature Maximum is incorrect"
    assert (
        abs(stats.at["median", "Temperature Maximum"] - 70.000000) < 1e-6
    ), "Median of Temperature Maximum is incorrect"
    assert (
        abs(stats.at["std_dev", "Temperature Maximum"] - 14.719337) < 1e-6
    ), "Standard deviation of Temperature Maximum is incorrect"

    assert (
        abs(stats.at["mean", "Precipitation"] - 0.127020) < 1e-6
    ), "Mean of Precipitation is incorrect"
    assert (
        abs(stats.at["median", "Precipitation"] - 0.000000) < 1e-6
    ), "Median of Precipitation is incorrect"
    assert (
        abs(stats.at["std_dev", "Precipitation"] - 0.327184) < 1e-6
    ), "Standard deviation of Precipitation is incorrect"


# Test Polars functions
def test_load_data_pl():
    """Function to test the load_data_pl function (Polars)."""
    data = load_data_pl(file_path)
    assert data.shape[0] > 0, "Loaded data should not be empty"
    assert isinstance(data, pl.DataFrame), "Loaded data should be a Polars DataFrame"


def test_calculate_statistics_pl():
    """Function to test the calculate_statistics_pl function (Polars)."""
    data = load_data_pl(file_path)
    stats = calculate_statistics_pl(data)

    mean_temp_min = stats["mean"].to_numpy()[0][0]
    median_temp_min = stats["median"].to_numpy()[0][0]
    std_dev_temp_min = stats["std_dev"].to_numpy()[0][0]

    assert (
        abs(mean_temp_min - 44.225166) < 1e-6
    ), "Mean of Temperature Minimum is incorrect (Polars)"
    assert (
        abs(median_temp_min - 45.000000) < 1e-6
    ), "Median of Temperature Minimum is incorrect (Polars)"
    assert (
        abs(std_dev_temp_min - 14.538763) < 1e-6
    ), "Standard deviation of Temperature Minimum is incorrect (Polars)"


def test_create_histogram_pl():
    """Function to test the create_histogram_pl function (Polars)."""
    data = load_data_pl(file_path)
    histogram_path = "temperature_minimum_distribution_pl.png"
    create_histogram_pl(data, "Temperature Minimum", histogram_path)
    assert os.path.isfile(histogram_path), "Histogram file should be created"
    os.remove(histogram_path)  # Cleanup after test


def test_benchmark_pandas_vs_polars():
    """Function to test the structure of the profiling output for Pandas and Polars."""
    pandas_profile, polars_profile = benchmark_pandas_vs_polars(file_path)

    # Ensure profiling results are non-empty
    assert pandas_profile, "Pandas profiling should not be empty"
    assert polars_profile, "Polars profiling should not be empty"


if __name__ == "__main__":
    test_load_data()
    test_calculate_statistics()

    test_load_data_pl()
    test_calculate_statistics_pl()
    test_create_histogram_pl()

    test_benchmark_pandas_vs_polars()
