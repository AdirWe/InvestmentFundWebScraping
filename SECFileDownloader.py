# coding=utf-8
# -*- coding: utf-8 -*-

import requests as req
from bs4 import BeautifulSoup
import urllib.request
import re
from selenium import webdriver
import time

# from lxml import etree

# from openpyxl import load_workbook


# def get_data_fromURL(URL):
#     """
#     Return the data from the URL request
#     """
#     resp = req.get(URL, timeout=(3.05, 27))
#     return resp.text


def get_data_fromURL_with_delay(URL):
    browser = webdriver.Chrome('chromedriver')
    browser.get(URL)
    # time.sleep(10)
    links = browser.find_elements_by_tag_name('a')
    desired_links = []
    for link in links:
        link_url = link.get_attribute("href")

        if link_url and "reports/details" in link_url:
            desired_links.append(link_url)
    browser.quit()
    return desired_links


def get_fundData_fromURL_with_delay(URL):
    browser = webdriver.Chrome('chromedriver')
    browser.get(URL)
    time.sleep(5)
    namesAndIds = browser.find_element_by_id("Row0Field6")
    # namesAndIds_array = namesAndIds.find_attributr
    valueBefore = browser.find_element_by_id('Row0Field9')
    valueAfter = browser.find_element_by_id('Row0NewField1')
    # sendDate = browser.find_element_by_xpath(
    #     "..span[@id='HeaderSendDate']/following-sibling::td")
    changeDate = browser.find_element_by_id('Field3')

    print(namesAndIds)
    print(valueBefore)
    print(valueAfter)
    print(changeDate)

    # links = browser.find_elements_by_tag_name('a')
    # desired_links = []
    # for link in links:
    #     link_url = link.get_attribute("href")

    #     if link_url and "reports/details" in link_url:
    #         desired_links.append(link_url)
    # browser.quit()
    # return desired_links


def get_mayafiles_htmlFIle(URL):
    try:
        browser = webdriver.Chrome('chromedriver')
        browser.get(URL)
        time.sleep(5)
        links = browser.find_elements_by_tag_name('a')
        desiredHrefNumber = str(URL.split("/")[-1]) + ".htm"
        desired_links = []
        for link in links:
            link_url = link.get_attribute("href")
            if link_url and desiredHrefNumber in link_url:
                desired_links.append(link_url)
        browser.quit()
        if len(desired_links) > 0:
            return(desired_links[0])
        return ""
    except:
        return ""


def get_requiredData_from_htmlURL(URL):
    tries = 0
    while tries < 5:
        try:
            page = req.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.original_encoding)

            sendDate = ""  # init
            # try each one of the 2 options, starting from the more specific:
            sendDate_firstAttempt = soup.find_all(id='HeaderSendDate')[
                0].find_parent().find_next_sibling("td")
            # sendDate = soup.find_all(id='HeaderSendDate')[
            #     0].find_parent().find_next_sibling("td").text
            if sendDate_firstAttempt != None:
                sendDate = sendDate_firstAttempt.text
            else:
                sendDate_secondAttempt = sendDate = soup.find_all(id='HeaderSendDate')[
                    0].find_parent()
                # sendDate = soup.find_all(id='HeaderSendDate')[
                #     0].find_parent().text
                if sendDate_secondAttempt != None:
                    sendDate = sendDate_secondAttempt.text

            only_date_char = re.findall(
                "[0-9]{2}/[0-9]{2}/[0-9]{4}", sendDate)
            # print(only_date_char)
            if len(only_date_char) > 0:
                sendDate = only_date_char[0]

            changeDate = soup.find_all(id='Field3')[0].text
            # numOfFounds = len(soup.find(id="Section1").find("tr", recursive=False).find(
            #     "td", recursive=False).find_all("table", recursive=False))
            # print("numOfFounds = ", numOfFounds)
            data_to_return = {"sendDate": sendDate,
                              "changeDate": changeDate, "foundsData": []}
            # for i in range(0, numOfFounds):
            rowIndex = 0
            while True:
                checkIfRowExist = soup.find_all(
                    id="Row" + str(rowIndex) + "Field6")
                if len(checkIfRowExist) == 0:
                    break  # row doesn't exist! so break..
                namesAndIds = checkIfRowExist[0].text
                # print("namesAndIds: ", namesAndIds)
                end_of_name = namesAndIds.rfind("(") - 1
                beggin_of_id = namesAndIds.rfind(":") + 2
                valueBefore = float(soup.find_all(
                    id="Row" + str(rowIndex) + "Field9")[0].text)
                firstAttempt_valueAfter = soup.find_all(
                    id="Row" + str(rowIndex) + "NewField1")
                valueAfter = 10000000
                if len(firstAttempt_valueAfter) > 0:
                    valueAfter = float(firstAttempt_valueAfter[0].text)
                else:
                    # print("not such id -NewFIeld!-")
                    secondAttempt_valueAfter = soup.find_all(
                        id="Row" + str(rowIndex) + "Field11")
                    if len(secondAttempt_valueAfter) > 0:
                        valueAfter = float(secondAttempt_valueAfter[0].text)
                # valueAfter = soup.find_all(id="Row" + str(i) + "NewField1")[0].text
                data_to_return["foundsData"].append(
                    {"foundId": int(namesAndIds[beggin_of_id: -1]), "foundName": namesAndIds[: end_of_name], "valueBefore": valueBefore, "valueAfter": valueAfter})
                rowIndex += 1

            return data_to_return
        except:
            tries += 1


def donwload_file_from_maya(wanted_URL):
    data = get_data_fromURL_with_delay(wanted_URL)  # extract the data from URL
    # transform to soup object to parse
    with open("somepath", 'w') as f:
        f.write(data)
    soup = BeautifulSoup(data, 'html.parser')
    print(soup)

    print("Successfuly download the file!")
    return "Success"


def get_file_from_maya(wanted_URL):
    data = get_data_fromURL(wanted_URL)  # extract the data from URL
    # transform to soup object to parse
    soup = BeautifulSoup(data, 'html.parser')
    # iterate each one of the given URLS in sec table:
    tag_list = soup.find_all('a', id='documentsbutton')
    if len(tag_list) == 0:
        return ""  # not found any match file!!
    # To obtain the absolute URL, prepend https://www.sec.gov to the href value
    subData = get_data_fromURL("https://www.sec.gov" + tag_list[0]['href'])
    sub_soup = BeautifulSoup(subData, 'html.parser')
    table = sub_soup.select(".tableFile")[0]
    # drop the first title tr..
    table_TRs_withOut_titleTR = table.find_all("tr")[1:]
    for tr in table_TRs_withOut_titleTR:
        try:
            tds = tr.find_all("td")
            if ".txt" in tds[2].string:
                with urllib.request.urlopen("https://www.sec.gov" + tds[2].find("a")["href"]) as f:
                    html = f.read().decode('utf-8')
                    return html
                break
        except:
            continue
    return ""  # not found relevant document


def main():
    # URL = "https://maya.tase.co.il/reports/fund?q=%7B%22DateFrom%22:%222011-12-15T22:00:00.000Z%22,%22DateTo%22:%222021-01-30T22:00:00.000Z%22,%22events%22:%5B5600%5D,%22subevents%22:%5B5605%5D,%22Page%22:70%7D"
    # # donwload_file_from_maya(URL)
    # links = get_data_fromURL_with_delay(URL)
    # print(links)

    # get_fundData_fromURL_with_delay(
    #     "https://maya.tase.co.il/reports/details/1247863")
    # donwload_allRelatedFiles_from_sec(
    #     "https://mayafiles.tase.co.il/RHtm/1249001-1250000/H1249090.htm")
    # print(get_mayafiles_htmlFIle("https://maya.tase.co.il/reports/details/701663"))
    print(get_requiredData_from_htmlURL(
        "https://mayafiles.tase.co.il/RHtm/902001-903000/H902854.htm"))


if __name__ == "__main__":
    main()
