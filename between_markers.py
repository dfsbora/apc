def between_markers(text, begin, end):
    begin_pos = text.find(begin)
    if begin_pos != -1:   
        end_pos = text.find(end)
        if end_pos != -1:  #abriu e fechou
            if begin_pos < end_pos:  #ordem certa
                return text[begin_pos+len(begin):end_pos]
            else:    #ordem errada
                print("ordem errada")
                print(text)
                return ''
        else:   #abriu mas nao fechou
            return text[begin_pos+len(begin): len(text)] 
    else:   
        end_pos = text.find(end)
        if end_pos != -1: #nao abriu mas fechou
            return text[0: end_pos]
        else:
            return text    #nao abriu nem fechou


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
    assert between_markers("No <hi> one", ">", "<") == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
