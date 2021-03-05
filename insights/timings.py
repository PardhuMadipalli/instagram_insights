from commons import readcsv
import numpy as np
import constant
import insights.htmlutils as htmlutils


def get_timing_insights(csv_filename, max_indices):
    df = readcsv(csv_filename)
    for metric in constant.METRICS_COLUMNS:
        _get_best_timing_based_on(metric, df, max_indices)


def _get_best_timing_based_on(column_name, df, max_indices):
    # corresponds to total metric value of all the posts for that particular hour
    metrics_total = np.full([24], 0, dtype=int)

    # corresponds to number of times that a post has been made in that hour
    metrics_counter = np.full([24], 0, dtype=int)

    table = htmlutils.Table('Timings based on ' + column_name)

    for index, row in df.iterrows():
        metrics_total[row[constant.HOUR_COL]] += row[column_name]
        metrics_counter[row[constant.HOUR_COL]] += 1
    metrics_avg = np.divide(metrics_total, metrics_counter, out=np.zeros(metrics_total.shape, dtype=float), where=metrics_counter!=0)

    # Find a total of max_indices maximums
    idx = np.argpartition(metrics_avg, -max_indices)[-max_indices:]
    idx = idx[np.argsort(metrics_avg[idx])][::-1]

    np.set_printoptions(formatter={'float_kind': "{:.1f}".format})
    print(f'Top {max_indices} hours to post for maximum {column_name} are {idx}')
    print(f'Average {column_name}s at these hours are {metrics_avg[idx]} respectively.')
    print()

    table.add_header_row(['Best hours', 'Average metric values'])
    table.add_column_data(idx)
    table.add_column_data(metrics_avg[idx])
    table.write_html()