import gradio as gr
from data_analyzer import load_data, analyze


def analyze_file(uploaded_file):
    if uploaded_file is None:
        return None
    df = load_data(uploaded_file.name)
    analysis = analyze(df)
    return {
        "shape": {
            "rows": analysis['shape'][0],
            "columns": analysis['shape'][1]
        },
        "dtypes": analysis['dtypes'],
        "summary": analysis['summary']
    }


iface = gr.Interface(
    fn=analyze_file,
    inputs=gr.File(label="Upload CSV, Excel or JSON"),
    outputs=gr.JSON(label="Analysis"),
    title="Data Analyzer",
    description="Upload a CSV, Excel or JSON file to see dataset details."
)


if __name__ == "__main__":
    iface.launch()
