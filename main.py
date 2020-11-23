import pandas as pd
import numpy as np
from pathlib import Path


def test_scaling(max: int = 10000, steps: int = 10):
    for size in map(round, np.linspace(0, max, num=steps)):
        print(get_excel_file_size_for(size))


def get_excel_file_size_for(number_of_entries):
    file_path = Path('./tmp.xlsx')

    if file_path.exists():
        file_path.unlink()

    d = pd.DataFrame()
    d = d.append([0] * number_of_entries)
    d.to_excel(file_path)

    size = file_path.stat().st_size
    file_path.unlink()
    return size


test_scaling()