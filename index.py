from subStringFinder import find_between, find_substring_only_after_given_string, find_substring_only_after_given_string_with_oppenings, tableFinder_after_begginingText
from fileDownloader import get_data_fromURL_with_delay
from excelReader import readExcel
from excelWriter import writeToExcel


def get_all_links():
    # get all links for each page:
    for pageIndex in range(1, 75):  # not including 75..
        URL = "https://maya.tase.co.il/reports/fund?q=%7B%22DateFrom%22:%222011-12-15T22:00:00.000Z%22,%22DateTo%22:%222021-01-30T22:00:00.000Z%22,%22events%22:%5B5600%5D,%22subevents%22:%5B5605%5D,%22Page%22:" + \
            str(pageIndex) + "%7D"
        links = get_data_fromURL_with_delay(URL)
        writeToExcel(links, pageIndex)


def main():
    print("Beggining!")
    # get_all_links()
    # writeToExcel2()


if __name__ == "__main__":
    main()
