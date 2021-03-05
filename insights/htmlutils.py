import constant
import os
import pkg_resources
import shutil


def get_html_file():
    return os.getcwd() + "/index.html"


def get_css_file():
    return os.getcwd() + "/style.css"


def create_html():
    try:
        shutil.copy(pkg_resources.resource_filename(__name__, "data/" + constant.HTML_TEMPLATE), get_html_file())
        shutil.copy(pkg_resources.resource_filename(__name__, "data/" + constant.CSS_FILE), get_css_file())
    except Exception as ex:
        print("Warning: Exception while copying HTML or CSS files." + str(ex))
        pass


def end_html():
    append_html('</div></body>' + "\n" + '</html>')
    print('HTML file is generated at ', get_html_file())


def append_html(html_data):
    with open(get_html_file(), 'a+') as htmlFile:
        htmlFile.write(html_data)


# class Heading:
#     def __init__(self, text):
#         append_html('<h3>' + text + '</h3>')


class Table:
    def __init__(self, caption):
        self.list_column_lists = []
        self.__header_columns = []
        self.__caption = caption
        self.html = '<table>'

    def add_header_row(self, header_columns_names):
        self.__header_columns = header_columns_names

    def add_column_data(self, column_data):
        self.list_column_lists.append(column_data)

    def write_html(self):
        self.html += '<caption>' + self.__caption + '</caption>' + "\n"
        self.__add_row(self.__header_columns, header=True)
        num_rows = len(self.list_column_lists[0])  # All columns have same length
        for index in range(num_rows):
            row = []
            for data_item_list in self.list_column_lists:
                row.append(data_item_list[index])
            self.__add_row(row)
        self.html += '</table>' + '</br>' + '</br>' + "\n"
        append_html(self.html)

    def __add_row(self, row, header=False):
        row_html = '    <tr>'
        table_data_start_tag = '<th>' if header else '<td>'
        table_data_end_tag = '</th>' if header else '</td>'
        for item in row:
            row_html += table_data_start_tag + str(item) + table_data_end_tag
        row_html += "\n"
        self.html += row_html
