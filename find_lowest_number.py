class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        words = self.text.split()
        return len(words)


class TextFileSaver:
    def save(self, text, filename):
        with open(filename, "w") as f:
            f.write(text)
        print(f"Text saved to {filename}")


# Demo usage
text = "An example that fixes SRP."
analyzer = TextAnalyzer(text)
print(f"Word count: {analyzer.word_count()}")

saver = TextFileSaver()
saver.save(text, "example.txt")
