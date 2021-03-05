import constant
from commons import readcsv
from commons import remove_element_list
import insights.htmlutils as htmlutils


import matplotlib.pyplot as plt


def get_best_tags(csv_filename, show_graphs, max_indices):
    df = readcsv(csv_filename)
    for metric in constant.METRICS_COLUMNS:
        _get_best_tag_based_on(metric, df, max_indices, show_graphs)


def _get_best_tag_based_on(column_name, initial_df, max_indices, show_graphs):
    tag_avg_impressions = dict()
    df = initial_df.copy(deep=True)
    columns_without_impressions = remove_element_list(constant.DEFAULT_COLUMNS, column_name)
    df = df.drop(columns_without_impressions, axis=1)
    tags_columns = remove_element_list(df.columns.values, column_name)
    for tag in tags_columns:
        tag_avg_impressions.update({tag: (df[tag]*df[column_name]).sum()/(df[tag].sum())})
    sorted_avg = dict(sorted(tag_avg_impressions.items(), key=lambda item: item[1]))

    table = htmlutils.Table('Tags based on ' + column_name)
    table.add_header_row(['Best tags', 'Metric values', 'Worst tags', 'Metric values'])

    print(f'Best  tags based on {column_name}           : {list(sorted_avg.keys())[-max_indices:][::-1]}')
    print(f'Their corresponding {column_name} values are: {list(sorted_avg.values())[-max_indices:][::-1]}')
    print()

    table.add_column_data(list(sorted_avg.keys())[-max_indices:][::-1])
    table.add_column_data(list(sorted_avg.values())[-max_indices:][::-1])

    print(f'Worst tags based on {column_name}           : {list(sorted_avg.keys())[:max_indices]}')
    print(f'Their corresponding {column_name} values are: {list(sorted_avg.values())[:max_indices]}')
    print()

    table.add_column_data(list(sorted_avg.keys())[:max_indices])
    table.add_column_data(list(sorted_avg.values())[:max_indices])

    table.write_html()

    if show_graphs:
        plt.bar(*zip(*sorted_avg.items()))
        plt.savefig(column_name + ".png")
    return list(sorted_avg.keys())[-1], list(sorted_avg.keys())[0]
