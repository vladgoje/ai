def testP1():
    assert solveP1("ana are mere rosii si galbene si verzi") == "verzi"
    assert solveP1("ana are mere rosii si galbene sii a") == "sii"
    assert solveP1("ana alearga") == "ana"
    assert solveP1("") == ""


def solveP1(text):
    '''
    Determina ultimul cuvant dpdv alfabetic dintr-un text
    input: string - textul
    output: ultimul cuvant
            - string vid daca textul dat e vid
    '''
    if text == "":
        return ""

    split = text.split(" ")
    last = split[0]

    for word in split:
        if word > last:
            last = word
    
    return last


def main():
    text = input("Text: ")
    result = solveP1(text)
    print("Last: " + result)

testP1()
main()
