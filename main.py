def main():
        text = get_contents("books/frankenstein.txt")
        words = get_words(text)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} found in the document")
        
        letter_count = count_letters(text)
        
        sorted = sort_dict(letter_count)
        
        really_sorted = sort_by_value(sorted)

        for item in really_sorted:
               print(f"The '{item["char"]}' character was found {item["val"]} times")

        print("--- End report ---")
        
def get_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words(text):
        split_text = text.split()
        return split_text
      
def count_letters(text):
        letters_dict = {}
        lowercased_text = text.lower()
        for letter in lowercased_text:
              if letter in letters_dict:
                    letters_dict[letter] += 1
              else:
                    letters_dict[letter] = 1

        return letters_dict
      

def sort_dict(dict):
        list_of_dicts = []
        for item in dict.items():
                  if item[0].isalpha():
                         list_of_dicts.append({"char":item[0], "val":item[1]})

        return list_of_dicts

def sort_on(dict):
        return dict["val"]

def sort_by_value(dict):
        dict.sort(reverse=True, key=sort_on)
        return dict

main()