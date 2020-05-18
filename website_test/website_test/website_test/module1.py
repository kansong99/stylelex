import spacy

nlp = spacy.load("en_core_web_sm")

def oxfords(str):

    # "He wants to buy red apples, green grapes, and yellow bananas. I like Jill, Jane, and Mary."
    doc = nlp(str)
    noun_count = 0;
    errors = [];
    for chunk in doc.noun_chunks:
        if chunk.root.dep_ == 'conj':
            noun_count = noun_count + 1
            comma_index = chunk[0].i - 2
        else:
            if noun_count > 1:
                errors.append(comma_index)
                noun_count = 0
    if noun_count > 1:
        errors.append(comma_index)

    return errors
