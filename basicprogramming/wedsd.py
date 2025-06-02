hangul = ['가','나','다','라','마','바','사','아','자','차','카','타','파','하']
roman = ['ga','na','da','ra','ma','ba','sa','ah','ja','cha','ka','ta','pa','ha']
joined = []


for a in range(len(roman)):
    # range(14)
    joined.append(f'{hangul[a]}({roman[a]})')


print(joined)