import pandas as pd
import matplotlib.pyplot as plt


def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)


def calculate_statistics(data):
    """Calculate mean, median, and standard deviation for selected columns."""
    selected_columns = ['Temperature Minimum', 'Temperature Maximum', 'Precipitation']
    data = data[selected_columns]

    stats = {
        "mean": data.mean(),
        "median": data.median(),
        "std_dev": data.std(),
    }
    return pd.DataFrame(stats).T


def create_histogram(data, column, filepath):
    """Generate a histogram for the specified column and save it."""
    plt.figure(figsize=(10, 5))
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(filepath)
    plt.close()


def generate_md_report(stats, image_paths, output_path_md):
    """Generate a markdown report with the descriptive statistics and images."""
    with open(output_path_md, "w") as file:
        file.write("# Summary Report\n\n")
        file.write("## Descriptive Statistics\n\n")
        file.write(stats.to_markdown())
        file.write("\n\n")
        for image_path in image_paths:
            file.write(f"![{image_path}]({image_path})\n")
