import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
from pyinstrument import Profiler


# Pandas Functions
def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)


def calculate_statistics(data):
    """Calculate mean, median, and standard deviation for selected columns."""
    selected_columns = ["Temperature Minimum", "Temperature Maximum", "Precipitation"]
    data = data[selected_columns]

    stats = {
        "mean": data.mean(),
        "median": data.median(),
        "std_dev": data.std(),
    }
    return pd.DataFrame(stats).T


# Polars Functions
def load_data_pl(filepath):
    """Load data from a CSV file using polars."""
    return pl.read_csv(filepath)


def calculate_statistics_pl(data):
    """Calculate mean, median, and standard deviation for selected columns using polars."""
    selected_columns = ["Temperature Minimum", "Temperature Maximum", "Precipitation"]
    data = data.select(selected_columns)

    # Extract mean, median, std_dev and flatten arrays
    stats = {
        "mean": data.select(
            [pl.col(c).mean().alias(c) for c in selected_columns]
        ).to_dict(as_series=False),
        "median": data.select(
            [pl.col(c).median().alias(c) for c in selected_columns]
        ).to_dict(as_series=False),
        "std_dev": data.select(
            [pl.col(c).std().alias(c) for c in selected_columns]
        ).to_dict(as_series=False),
    }

    for stat_name, stat_values in stats.items():
        for key, value in stat_values.items():
            stat_values[key] = value[0]

    return pl.DataFrame(stats)


def create_histogram_pl(data, column, filepath):
    """Generate a histogram for the specified column using polars data and save it."""
    plt.figure(figsize=(10, 5))
    plt.hist(data[column].to_pandas(), bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(filepath)
    plt.close()


# Profiling for performance comparison
def benchmark_pandas_vs_polars(data_filepath):
    """Benchmark Pandas vs Polars for loading data and performing descriptive statistics."""

    profiler = Profiler()

    # Profiling Pandas
    profiler.start()
    pandas_data = load_data(data_filepath)
    pandas_stats = calculate_statistics(pandas_data)
    print(pandas_stats)
    profiler.stop()
    pandas_profile = profiler.output_text(unicode=True, color=True)

    # Profiling Polars
    profiler.start()
    polars_data = load_data_pl(data_filepath)
    polars_stats = calculate_statistics_pl(polars_data)
    print(polars_stats)
    profiler.stop()
    polars_profile = profiler.output_text(unicode=True, color=True)

    return pandas_profile, polars_profile


# Improving profiler readability for Markdown
def clean_profiler_output(profiler_output):
    """Clean profiler output for better readability in markdown."""
    cleaned_output = profiler_output.replace("\x1b[", "").replace("\x1b[0m", "")
    return cleaned_output


# Markdown Report Generation
def generate_md_report(
    stats, image_paths, pandas_profile, polars_profile, output_path_md
):
    """Generate a markdown report with the descriptive statistics, images, and profiling results."""
    with open(output_path_md, "w") as file:
        # Descriptive statistics
        file.write("# Summary Report\n\n")

        # Polars Descriptive Statistics
        file.write("## Descriptive Statistics (Polars)\n\n")
        file.write(stats.to_pandas().to_markdown(index=True))
        file.write("\n\n")

        # Images
        for image_path in image_paths:
            file.write(f"![{image_path}]({image_path})\n")
        file.write("\n\n")

        # Profiling results
        file.write("## Pandas vs Polars Profiling Results\n\n")

        # Pandas profiling result
        file.write("### Pandas Profiling\n\n")
        file.write("```\n")
        file.write(clean_profiler_output(pandas_profile))
        file.write("\n```\n")

        # Polars profiling result
        file.write("### Polars Profiling\n\n")
        file.write("```\n")
        file.write(clean_profiler_output(polars_profile))
        file.write("\n```\n")
