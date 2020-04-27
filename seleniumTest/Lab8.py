import time
import unittest
from collections import OrderedDict
import xlrd
from selenium import webdriver
from xlutils.copy import copy

excel_file_name = "results.xls"
student_marks_html_page = "https://gnsaddy.github.io/webAutomationSelenium/seleniumTest/student.html"
driver = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
driver.maximize_window()


def read_from_excel(excelFile):
    book = xlrd.open_workbook(excelFile)
    first_sheet = book.sheet_by_index(0)  # read the first sheet
    print("Number of rows ", first_sheet.nrows)
    print("Number of columns ", first_sheet.ncols)
    print("Col Schema/names: ", first_sheet.col_values(0, 1))

    marks_dict = OrderedDict()
    for each_name, index in zip(first_sheet.col_values(0, 1), range(1, first_sheet.nrows)):
        each_rows = first_sheet.row_values(index, 1)
        marks_dict[str(each_name)] = each_rows
    return marks_dict


def calculate_result(ch_driver, marks_dict):
    # Send dictionary keys and values to browser inputs.
    number_of_rows = 10
    student_name_objects = ch_driver.find_elements_by_xpath("//*[@id='student_name']")
    marks_objects = ch_driver.find_elements_by_class_name("marks")
    for (each_item_key, values), index in zip(marks_dict.items(), range(0, number_of_rows)):
        student_name_objects[index].send_keys(each_item_key)
        for each_marks, index_value in zip(values, range(0, len(values))):
            marks_objects[0].send_keys(str(each_marks))
            del marks_objects[0]
    time.sleep(3)
    driver.find_element_by_id("calculate").click()
    print("Clicked on calculate!")


def get_total_percentage_result(ch_driver):
    time.sleep(5)
    total_objects = ch_driver.find_elements_by_class_name("total")
    percentage_objects = ch_driver.find_elements_by_class_name("percentage")
    result_objects = ch_driver.find_elements_by_class_name("result")
    total = []
    percent = []
    result = []
    for each_total_obj in total_objects:
        total.append(str(each_total_obj.get_attribute('value')))
    for each_percentage_obj in percentage_objects:
        percent.append(str(each_percentage_obj.get_attribute('value')))
    for each_result_obj in result_objects:
        result.append(str(each_result_obj.get_attribute('value')))
    print("total:" + str(total))
    print("Percentage:" + str(percent))
    print("Result:" + str(result))
    return total, percent, result


def append_to_excel(calculated_results):
    """
   Appends total, percentage, result to excel sheet.
   """
    number_of_rows = 10
    total, percent, result = calculated_results
    rb = xlrd.open_workbook(excel_file_name)
    r_sheet = rb.sheet_by_index(0)
    c = r_sheet.ncols  # number of columns
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(0, c, "Total")  # Add the column 'Total' at the end in excel sheet
    for each_total_value, index in zip(total, range(1, number_of_rows + 1)):
        sheet.write(index, c, each_total_value)
    sheet.write(0, c + 1, "Percentage")  # Add the column 'Percentage' at the end in excel sheet
    for each_percent_value, index in zip(percent, range(1, number_of_rows + 1)):
        sheet.write(index, c + 1, each_percent_value)
    sheet.write(0, c + 2, "Result")  # Add the column 'Result' at the end in excel sheet
    for each_result_value, index in zip(result, range(1, number_of_rows + 1)):
        sheet.write(index, c + 2, each_result_value)
    wb.save(excel_file_name)
    print('Saved excel sheet successfully.')


# function calls

if __name__ == "__main__":
    marks_dictionary = read_from_excel(excel_file_name)
    print(marks_dictionary)

    path = student_marks_html_page
    driver.get(path)  # load web page
    time.sleep(4)

    calculate_result(driver, marks_dictionary)

    calculation_results = get_total_percentage_result(driver)

    append_to_excel(calculation_results)
    print("Closing the browser")
    unittest.main()
