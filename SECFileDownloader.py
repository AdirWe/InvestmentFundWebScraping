import requests as req
from bs4 import BeautifulSoup
import urllib.request


def getURL_by_companyName(company_name, file_type, prior_to_date, count):
    baseURL = "https://www.sec.gov/cgi-bin/browse-edgar?"
    name = "+".join(company_name.split())  # name format in the URL
    # create the URL request:
    wanted_URL = baseURL + "company=" + str(company_name) + \
        "&type=" + str(file_type) + "&dateb=" + \
        str(prior_to_date) + "&count=" + str(count)
    return wanted_URL


def getURL_by_CIK(CIK, file_type, prior_to_date, count):
    baseURL = "https://www.sec.gov/cgi-bin/browse-edgar?"
    # create the URL request:
    wanted_URL = baseURL + "action=getcompany&CIK=" + str(CIK) + \
        "&type=" + str(file_type) + "&dateb=" + \
        str(prior_to_date) + "&count=" + str(count)
    return wanted_URL


def get_data_fromURL(URL):
    """
    Return the data from the URL request
    """
    resp = req.get(URL)
    return resp.text

# company=


def donwload_allRelatedFiles_from_sec(wanted_URL):

    data = get_data_fromURL(wanted_URL)  # extract the data from URL
    # transform to soup object to parse
    soup = BeautifulSoup(data, 'html.parser')
    # iterate each one of the given URLS in sec table:
    tag_list = soup.find_all('a', id='documentsbutton')
    index = 0
    for tag in tag_list:
        index += 1
        # To obtain the absolute URL, prepend https://www.sec.gov to the href value
        # print("https://www.sec.gov" + tag['href'])
        subData = get_data_fromURL("https://www.sec.gov" + tag['href'])
        sub_soup = BeautifulSoup(subData, 'html.parser')
        table = sub_soup.select(".tableFile")[0]
        # drop the first title tr..
        table_TRs_withOut_titleTR = table.find_all("tr")[1:]
        # print(table_TRs_withOut_titleTR)
        for tr in table_TRs_withOut_titleTR:
            try:
                tds = tr.find_all("td")
                if ".txt" in tds[2].string:
                    with urllib.request.urlopen("https://www.sec.gov" + tds[2].find("a")["href"]) as f:
                        html = f.read().decode('utf-8')
                        with open('C:/Users/adirwe/Desktop/DownloadsExample/' + str(index) + ".html", 'w') as f:
                            f.write(html)
                    # print(tds[2].find("a")["href"])
                    break
            except:
                continue
        # print(str(index) + " - - - - - - - - - - - - - - ")


# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=872448
# https://www.sec.gov/Archives/edgar/data/1043382/000095012311022168/0000950123-11-022168-index.htm


# company=
def donwload_file_from_sec(wanted_URL, newFile_name):
    data = get_data_fromURL(wanted_URL)  # extract the data from URL
    # transform to soup object to parse
    soup = BeautifulSoup(data, 'html.parser')
    # iterate each one of the given URLS in sec table:
    tag_list = soup.find_all('a', id='documentsbutton')
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
                    with open('C:/Users/adirwe/Desktop/DownloadsExample/' + str(newFile_name) + ".html", 'w') as f:
                        f.write(html)
                # print(tds[2].find("a")["href"])
                break
        except:
            continue
    print("Successfuly download the file!")


def main():
    URL = getURL_by_CIK(872448, "DEF+14A", 20110504, 40)
    donwload_file_from_sec(URL, 872448)


if __name__ == "__main__":
    main()
