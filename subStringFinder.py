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


def titleFinder(data):
    possiblesTitles = ["Payments for Termination for Good Reason or Other Than For Cause – Following a Change in Control",
                       "Change of Control Severance Plan/Performance Share Award Agreements"]

    beggining_text_index = s.index(beggining_text) + len(beggining_text)
