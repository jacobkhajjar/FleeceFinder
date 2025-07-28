from objects.consonants import Consonant, Action
from objects.vowels import Vowel

def guess_lexical_sets(word, phones):

    lexical_sets = set()
    
    # loop over each phone
    for i, phone in enumerate(phones):
        
        # skip consonants
        if isinstance(phone, Vowel):
            vowel = phone
        else:
            continue

        # define previous / first
        if i == 0:
            previous = None
            first = True
        else:
            previous = phones[i - 1]
            first = False

        # define next / last
        if i < len(phones) - 1:
            next = phones[i + 1]
            last = False
        else:
            next = None
            last = True
            

        # begin logic based on CMU ARPA
        match vowel.arpa:
            
            # LOT/START/PALM - need logic to split LOT/PALM
            case "AA":
                if next and next.arpa == "R":
                    lexical_sets.add("START")
                else:
                    lexical_sets.add("LOT/PALM")
            
            # TRAP/BATH - need logic to split
            case "AE":
                lexical_sets.add("TRAP/BATH")

            # STRUT - COMPLETE
            case "AH":
                if vowel.is_stressed:
                    lexical_sets.add("STRUT")
                else:
                    lexical_sets.add("commA (strut)")
            
            # THOUGHT/CLOTH/NORTH/FORCE - need logic to split
            case "AO":
                lexical_sets.add("THOUGHT/CLOTH/NORTH/FORCE")

            # MOUTH - COMPLETE
            case "AW":
                lexical_sets.add("MOUTH")

            # PRICE - COMPLETE
            case "AY":
                lexical_sets.add("PRICE")

            # DRESS - assumes DRESS + R is always SQUARE?
            case "EH":
                if next and next.arpa == "R":
                    lexical_sets.add("SQUARE")
                elif vowel.is_stressed:
                    lexical_sets.add("DRESS")
                else:
                    lexical_sets.add("commA (dress)")
            
            # NURSE/LETTER - COMPLETE
            case "ER":
                if vowel.is_stressed:
                    lexical_sets.add("NURSE")
                else:
                    lexical_sets.add("lettER")

            # FACE - COMPLETE
            case "EY":
                lexical_sets.add("FACE")

            # KIT / NEAR - assumes assumes NEAR is never unstressed and KIT + R is always NEAR
            case "IH":
                if vowel.is_stressed:
                    if next and next.arpa == "R":
                        lexical_sets.add("NEAR")
                    else:
                        lexical_sets.add("KIT")
                else:
                    lexical_sets.add("commA (kit)")

            # FLEECE / happY / commA / NEAR - assumes NEAR is never unstressed and FLEECE + R is always NEAR
            case "IY":
                if not vowel.is_stressed:
                    if first:
                        lexical_sets.add("commA (fleece)")
                    else:
                        lexical_sets.add("happY")
                elif next and next.arpa == "R":
                    lexical_sets.add("NEAR")
                else:
                    lexical_sets.add("FLEECE")
            
            # GOAT/GOAL - COMPLETE
            case "OW":
                if next and next.arpa == "L":
                    lexical_sets.add("GOAL (goat)")
                else:
                    lexical_sets.add("GOAT")

            # CHOICE - COMPLETE
            case "OY":
                lexical_sets.add("CHOICE")

            # FOOT/CURE - assumes FOOT + R is always CURE
            case "UH":
                if next and next.arpa == "R":
                    lexical_sets.add("CURE")
                elif vowel.is_stressed:
                    lexical_sets.add("FOOT")
                else:
                    lexical_sets.add("commA (foot)")

            # GOOSE/CURE - assumes GOOSE + R is always CURE
            case "UW":
                if next and next.arpa == "R":
                    lexical_sets.add("CURE")
                elif vowel.is_stressed:
                    lexical_sets.add("GOOSE")
                else:
                    lexical_sets.add("commA (goose)")
            
    return lexical_sets