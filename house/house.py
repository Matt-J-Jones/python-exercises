def recite(start_verse, end_verse):
    verses = [
        "This is ",
        "the horse and the hound and the horn that belonged to ",
        "the farmer sowing his corn that kept ",
        "the rooster that crowed in the morn that woke ",
        "the priest all shaven and shorn that married ",
        "the man all tattered and torn that kissed ",
        "the maiden all forlorn that milked ",
        "the cow with the crumpled horn that tossed ",
        "the dog that worried ",
        "the cat that killed ",
        "the rat that ate ",
        "the malt that lay in ",
        "the house that Jack built."
    ]

    return_arr = []

    for line in range(start_verse, end_verse+1):
        return_arr.append(verses[0] + "".join(verses[-line:len(verses)]))
    return return_arr
