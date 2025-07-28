import json

from objects.consonants import classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel
from guess_lexical_sets import guess_lexical_sets

def main():
    
    filtered_dict = {}

    with open("cmu.json", "r" , encoding="utf-8") as f:
        CMU_dict = json.load(f)

        word_list = []

        for word in CMU_dict:
            for transcription in CMU_dict[word]:
                if any(
                    arpa in transcription for arpa in ["IY", "IY0", "IY1", "IY2"]
                ):
                    word_list.append(word)

        for word in word_list:
            homonyms = CMU_dict[word]
            for homonym in homonyms:
                phones = []
                for phone in homonym:
                    if phone[0] in vowel_list:
                        new_phone = classify_vowel(phone)
                    else:
                        new_phone = classify_consonant(phone)
                    phones.append(new_phone)

                lexical_sets = guess_lexical_sets(word, phones)

                if word not in filtered_dict:
                    if all(both in lexical_sets for both in ["FLEECE", "happY"]):
                        filtered_dict[word] = ["FLEECE", "happY"]
                    elif "FLEECE" in lexical_sets:
                        filtered_dict[word] = ["FLEECE"]
                    elif "happY" in lexical_sets:
                        filtered_dict[word] = ["happY"]
                    else:
                        continue
                elif word in filtered_dict:
                    if all(both in lexical_sets for both in ["FLEECE", "happY"]):
                        filtered_dict[word] = ["FLEECE", "happY"]
                    elif "FLEECE" in lexical_sets and "FLEECE" not in filtered_dict[word]:
                        filtered_dict[word].append("FLEECE")
                    elif "happY" in lexical_sets and "happY" not in filtered_dict[word]:
                        filtered_dict[word].append("happY")
                    else:
                        continue

    with open("fleecefinder_results.txt", "w") as f:
        for word, sets in filtered_dict.items():
            f.write(f"{" ".join(sets)} {word}\n")

main()