from subStringFinder import find_between, find_substring_only_after_given_string, find_substring_only_after_given_string_with_oppenings, tableFinder_after_begginingText


def main():
    text = "a<table>errvlubegviuegbuevvbu</table>"
    result = find_between(text, "<table>", "</table>")
    result2 = find_substring_only_after_given_string(
        text, "a", "<table>", "</table>")
    print(result)
    print(result2)

    requeredTitle = "Change of Control Severance Plan/Performance Share Award Agreements"
    tableOpening = "<TABLE"
    tableClosure = "</TABLE>"
    with open("C:/Users/adirwe/Desktop/seminaryon/project/example.htm", "r") as f:
        data = f.read()
        # result3 = find_substring_only_after_given_string_with_oppenings(
        #     data, requeredTitle, tableOpening, tableClosure)
        result3 = tableFinder_after_begginingText(data, requeredTitle)
        print(result3)


if __name__ == "__main__":
    main()
