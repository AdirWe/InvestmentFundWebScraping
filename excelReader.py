# import tkinter as tk
from tkinter import filedialog
import pandas as pd

# root = tk.Tk()

# canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue')
# canvas1.pack()


# def getExcel():
#     global df

#     import_file_path = filedialog.askopenfilename()
#     df = pd.read_excel(import_file_path)
#     print(df)


# browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel,
#                                bg='green', fg='white', font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 150, window=browseButton_Excel)

# root.mainloop()


def readExcel(path, requeredSheet, columns):
    # import_file_path = filedialog.askopenfilename()
    # data = pd.read_excel(import_file_path, sheet_name=requeredSheet)
    data = pd.read_excel(path, sheet_name=requeredSheet)
    if len(columns) == 0:
        return data
    else:
        df = pd.DataFrame(
            data, columns=columns)
        return df
    # print(df)


def main():
    print("hereee - ExcelReader")
    data = readExcel('C:/Users/adirwe/Desktop/seminaryon/companiesData.xlsx',
                     'companies', ["Date Announced", "Target Name", "Target Primary Ticker Symbol"])
    print(data)
    # data2 = readExcel('C:/Users/adirwe/Desktop/seminaryon/companiesData.xlsx',
    #                   'companies', [])
    # print(data2)


if __name__ == "__main__":
    main()
