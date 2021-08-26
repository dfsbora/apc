def between_markers(text, begin, end):
    begin_pos = text.find(begin)
    if begin_pos != -1:   
        end_pos = text.find(end, begin_pos+1, len(text))
        if end_pos != -1:
            if begin_pos < end_pos:
                return text[begin_pos+len(begin):end_pos]
            else:
                return ""
        else:
            return text[begin_pos+len(begin): len(text)] 
    else:   
        end_pos = text.find(end)
        if end_pos != -1:
            return text[0: end_pos]
        else:
            return text 

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
