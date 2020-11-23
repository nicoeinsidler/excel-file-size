import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path


def plot_scaling(df: pd.DataFrame):
    sns_plot = sns.lineplot(x='Number of Rows', y='File Size [MB]',
                            data=df).get_figure()
    sns_plot.savefig('file_sizes.png')


def test_scaling(max: int = 10000, steps: int = 10) -> pd.DataFrame:
    results = pd.DataFrame(columns=['Number of Rows', 'File Size [MB]'])

    for size in map(round, np.linspace(0, max, num=steps)):
        file_size = get_excel_file_size_for(size)
        results = results.append(
            {
                'Number of Rows': size,
                'File Size [MB]': file_size
            },
            ignore_index=True)

    results = results.astype({'Number of Rows': int})
    return results


def get_excel_file_size_for(number_of_entries) -> float:
    file_path = Path('./tmp.xlsx')

    if file_path.exists():
        file_path.unlink()

    d = pd.DataFrame()
    d = d.append([0] * number_of_entries)
    d.to_excel(file_path)

    size = file_path.stat().st_size / 1_000_000
    file_path.unlink()
    return size


t = test_scaling(1_000_000, 100)
print(t)

plot_scaling(t)