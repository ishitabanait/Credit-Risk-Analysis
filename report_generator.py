import click
import os
import pandas as pd
from dataprep.eda import create_report
from ydata_profiling import ProfileReport
import sweetviz as sv


@click.command()
@click.option('--report', default='all', help='Report type: all, dataprep, ydata, sweetviz')
@click.argument('dataframe_to_profile')
def profiler(report, dataframe_to_profile):
    imported_df = read_file(dataframe_to_profile)

    match report:
        case "all":
            ydata_report_generator(imported_df)

            dataprep_report_generator(imported_df)

            sweetviz_report_generator(imported_df)
        case "dataprep":
            dataprep_report_generator(imported_df)

        case "ydata":
            ydata_report_generator(imported_df)

        case "sweetviz":
            sweetviz_report_generator(imported_df)


# Data import helper functions
def detect_file_type(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()


file_readers = {
    '.csv': pd.read_csv,
    '.xlsx': pd.read_excel,
    '.json': pd.read_json,
    '.pkl': pd.read_pickle
}


def read_file(file_path):
    file_type = detect_file_type(file_path)
    read_func = file_readers.get(file_type)

    try:
        return read_func(file_path)
    except ValueError:
        ValueError(f"Unsipported file type: {file_type}")


# Report generators

# ydata profile report
def ydata_report_generator(process_data):
    try:
        profile = ProfileReport(process_data, title="Ydata Profiling Report")
        profile.to_file("ydata_profiling.html")
    except:
        print("Failed to generate Ydata Profiling Report")


# Dataprep Report
def dataprep_report_generator(process_data):
    try:
        report = create_report(process_data, title="DataPrep Profiling Report")
        report.save('dataprep_report')
    except:
        print("Failed to generate DataPrep Profiling Report")


# Sweetviz report
def sweetviz_report_generator(process_data):
    try:
        my_report = sv.analyze(process_data)
        my_report.show_html(filepath='sweetviz_report.html', open_browser=False, layout='widescreen')
    except:
        print("Failed to generate Sweetviz Profiling Report")


if __name__ == "__main__":
    profiler()
