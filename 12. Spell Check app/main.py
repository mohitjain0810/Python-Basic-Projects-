# Step 1: Importing the required library
from spellchecker import SpellChecker

# Step 2: Creating the app class

# Advantage of building a class:
# We can place multiple functions in an organized structure.

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()  # Example: 'hellow world' -> ['hellow', 'world']
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word:
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)

        # Step 4: Returning the corrected text
        return ' '.join(corrected_words)

    # Step 5: Running the app
    def run(self):
        print("\n--- Spell Checker ---")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')

            if text.lower() == 'exit':
                print('Closing the program...')
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected Text: {corrected_text}')


# Step 6: Running the main program
if __name__ == "__main__":
    SpellCheckerApp().run()
