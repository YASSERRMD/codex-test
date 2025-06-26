# Data Analyzer

This repository contains a simple command-line tool and a Gradio web application for analyzing CSV, Excel, and JSON files.

## Setup

Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI analyzer:

```bash
python data_analyzer.py <path_to_file>
```

Launch the web interface:

```bash
python web_app.py
```

## Testing Workflow

1. Attempt to run the scripts before installing requirements. They will fail with `ModuleNotFoundError` if the packages are missing.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the scripts again. They should execute without import errors once the packages are installed.

