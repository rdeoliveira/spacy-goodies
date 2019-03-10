def get_entity_spans(doc):
    '''
    Returns the combined tokens that refer to an entity. Assumes doc has NER info.
    '''

    spans = list(doc.ents)
    for span in spans:
        span.merge()

    return spans

def get_n_gram(doc, token, n):
    """
    Returns an n-gram with the token as centre. Start at 0 if the token doesn't have as many left neighbours as n.
    """
    
    start = 0 if token.i < n else token.i - n
    end = token.i + n + 1

    return doc[start:end]

def is_head_of_np(token):
    """
    Returns true if the token's dependency label is that of a typical head of noun phrase (based on https://stackoverflow.com/questions/33289820/noun-phrases-with-spacy).
    """
    np_head_deps = ['nsubj', 'nsubjpass', 'dobj', 'iobj', 'pobj']
    return True if token.dep_ in np_head_deps else False
