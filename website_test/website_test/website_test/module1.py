import spacy

nlp = spacy.load("en_core_web_sm")

def oxfords(str, option):

    doc = nlp(str)
    noun_count = 0;
    errors = [];
    for chunk in doc.noun_chunks:
        if chunk.root.dep_ == 'conj':
            noun_count = noun_count + 1
            token_index = chunk[0].i - 2
            char_index = chunk[0].idx
            while str[char_index] != ",":
                char_index = char_index - 1;
        else:
            if noun_count > 1:
                if option == False and doc[token_index].text == ",":
                    errors.append(char_index)
                if option == True and doc[token_index].text != ",":
                    errors.append(char_index)
                noun_count = 0
    if noun_count > 1:
            if option == False and doc[token_index].text == ",":
                errors.append(char_index)
            if option == True and doc[token_index].text != ",":
                errors.append(char_index)

    return errors
