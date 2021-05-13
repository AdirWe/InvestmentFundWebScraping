def find_between(s, first_word, last_word):
    try:
        start = s.index(first_word) + len(first_word)
        end = s.index(last_word, start)
        return s[start:end]  # return the string between
    except ValueError:
        return ""
    except:
        return ""


def find_substring_only_after_given_string(s, beggining_word, subS_start, subS_end):
    try:
        beggining_word_index = s.index(beggining_word) + len(beggining_word)
        start = s.index(subS_start, beggining_word_index) + \
            len(subS_start)  # only find after beggining_word

        # find the subS_end after the start we just find..
        end = s.index(subS_end, start)
        return s[start:end]  # return the string between
    except ValueError:
        return ""
    except:
        return ""


def find_substring_only_after_given_string_with_oppenings(s, beggining_word, subS_start, subS_end):
    try:
        beggining_word_index = s.index(beggining_word) + len(beggining_word)
        # only find after beggining_word
        start = s.index(subS_start, beggining_word_index)

        # find the subS_end after the start we just find..
        end = s.index(subS_end, start) + len(subS_end)
        return s[start:end]  # return the string between
    except ValueError:
        return ""
    except:
        return ""


def tableFinder_after_begginingText(s, beggining_text):
    """
    return the first table occurrance after the beggining_text
    """
    try:
        beggining_text_index = s.index(beggining_text) + len(beggining_text)
        # only find after beggining_text
        start = s.index("<TABLE", beggining_text_index)

        # find the subS_end after the start we just find..
        end = s.index("</TABLE>", start) + len("</TABLE>")
        return s[start:end]  # return the string between
    except ValueError:
        return ""
    except:
        return ""


def tableFinder_after_last_occurrence_key(s, key):
    """
    return the first table occurrence after the last occurance of the beggining_text
    """
    try:
        # we assume that the table is after the *last* occurrence of the key in the document
        last_key_occurrence_index = s.rindex(key) + len(key)
        # only find after key
        start = s.index("<TABLE", last_key_occurrence_index)

        # find the subS_end after the start we just find..
        end = s.index("</TABLE>", start) + len("</TABLE>")
        return s[start:end]  # return the string between
    except ValueError:
        return ""
    except:
        return ""


def table_finder(s):
    possiblesTitles = ["Payments for Termination for Good Reason or Other Than For Cause – Following a Change in Control",
                       "Change of Control Severance Plan/Performance Share Award Agreements",
                       "Potential Payments upon Change of Control", "Potential Payments on Termination or Change in Control"]
    wantedTable = ""
    for key in possiblesTitles:
        try:
            # we assume that the table is after the *last* occurrence of the key in the document
            last_key_occurrence_index = s.rindex(key) + len(key)
            # only find after key
            start = s.index("<TABLE", last_key_occurrence_index)

            # find the subS_end after the start we just find..
            end = s.index("</TABLE>", start) + len("</TABLE>")
            wantedTable = s[start:end]  # return the string between
        except ValueError:
            pass
        except:
            pass
        finally:
            if wantedTable != "":  # if fond a table - stop searching
                break


def titleFinder(data):
    possiblesTitles = ["Payments for Termination for Good Reason or Other Than For Cause – Following a Change in Control",
                       "Change of Control Severance Plan/Performance Share Award Agreements",
                       "Potential Payments upon Change of Control", "Potential Payments on Termination or Change in Control"]

    # beggining_text_index = s.index(beggining_text) + len(beggining_text)

    # tableOpening = "<TABLE"
    # tableClosure = "</TABLE>"
