
import xlrd



def read_locators(file_path,sheetname):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_name(sheetname)
    row = sheet.nrows
   # {'username_textfield':['name', 'username']}
    d = {}
    # Syntax:               i=1,
    #     var[key] = value
    for i in range(1,row):
        data = sheet.row_values(i) #['username_textfield','name', 'username']
        d[data[0]] = [data[1],data[2]]
    return d
# {'username_textfield': ['name', 'username'], 'password_textfield': ['name', 'password'], 'login_button': ['xpath', "//button[text()=' Login ']"]}


r"""
path = r"C:\Users\Admin\Desktop\A2_Selenium\HybridFramework\excel_files\locators.xlsx"
read_locators(path,"loginpage")
"""   # we want to hardcode this be creating the variables

  # C:\Users\mohan\PycharmProjects\PythonProject\hybrid_framework