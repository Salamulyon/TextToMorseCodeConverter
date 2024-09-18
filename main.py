import pandas as pd

morse_data = pd.read_csv('morse.csv')
morse_dict: dict = {row.character:row.code for (_,row) in morse_data.iterrows()}

def main_loop():
    loop: bool = True
    while loop:
        try:
            sentence: str = input().upper()
            sentence_list: list = [letter for letter in sentence if letter != " "]
            sentence_in_morse = [morse_dict[character] for character in sentence_list]
            print("/".join(sentence_in_morse))
        except KeyboardInterrupt:
            loop = False


if __name__ == "__main__":
    main_loop()