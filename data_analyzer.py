import sys
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.json'):
        df = pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    return df


def analyze(df: pd.DataFrame) -> dict:
    analysis = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.apply(lambda x: x.name).to_dict(),
        'summary': df.describe(include='all').fillna('').to_dict()
    }
    return analysis


def print_analysis(analysis: dict):
    print(f"Rows: {analysis['shape'][0]}, Columns: {analysis['shape'][1]}")
    print("\nData Types:")
    for col, dtype in analysis['dtypes'].items():
        print(f"  {col}: {dtype}")
    print("\nSummary Statistics:")
    for col, stats in analysis['summary'].items():
        print(f"\nColumn: {col}")
        for stat, value in stats.items():
            print(f"  {stat}: {value}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python data_analyzer.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    df = load_data(file_path)
    analysis = analyze(df)
    print_analysis(analysis)


if __name__ == '__main__':
    main()
