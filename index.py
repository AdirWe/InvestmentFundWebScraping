from subStringFinder import find_between, find_substring_only_after_given_string, find_substring_only_after_given_string_with_oppenings, tableFinder_after_begginingText
from SECFileDownloader import donwload_file_from_sec, getURL_by_companyName, getURL_by_companyName
from excelReader import readExcel


def main():
    print("Beggining!")
    # get the companies data:
    excel_data = readExcel('C:/Users/adirwe/Desktop/companiesData.xlsx',
                           'companies', ["Date Announced", "Target Name", "Target Primary Ticker Symbol"])
    excel_data_length = len(excel_data)
    print("Got " + str(excel_data_length) + " rows in the excel.")

    for i in range(5):
        company_name = excel_data["Target Name"][i]
        company_name_in_URL_format = "+".join(company_name.split())
        date = str(excel_data["Date Announced"][i])
        date_in_URL_format = "".join((date.split()[0]).split("-"))
        # symbol = excel_data["Target Primary Ticker Symbol"][i]
        file_type = "DEF+14A"
        count = 10
        print(company_name)
        print("company_name_in_URL_format = ", company_name_in_URL_format)
        # print(symbol)
        print("date= ", date)
        print("date_in_URL_format= ", date_in_URL_format)

        URL = getURL_by_companyName(
            company_name_in_URL_format, file_type, date_in_URL_format, count)
        print(URL)
        # URL = getURL_by_companyName(872448, "DEF+14A", 20110504, 10)

        donwload_file_from_sec(URL, str(company_name))

    # with open("C:/Users/adirwe/Desktop/seminaryon/project/example.htm", "r") as f:
    #     data = f.read()
    #     result3 = tableFinder_after_begginingText(data, requeredTitle)
    #     print(result3)


if __name__ == "__main__":
    main()
