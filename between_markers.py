begin_pos = text.find(begin)
if begin_pos != -1:   
    end_pos = text.find(end, begin_pos+1, len(text))
    if end_pos != -1:
        print("Trecho: ", text[begin_pos+1:end_pos])
    else:
        # end_pos == -1
        print("Trecho: ", text[begin_pos+1: XXXX])

else:   
    end_pos = text.find(end)
    if end_pos != -1:
        print("Trecho: ", text[COMEÇO : end_pos])
    else:
        print("")


print("Trecho: ", text[init_pos+1:final_pos])
