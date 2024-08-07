import nltk
nltk.download('stopwords')

import tkinter as tk
from tkinter import filedialog, Text
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string

class WordCloudApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Cloud Generator")

        self.open_button = tk.Button(root, text="Open Text File", command=self.open_file)
        self.open_button.pack()

        self.generate_button = tk.Button(root, text="Generate Word Cloud", command=self.generate_word_cloud)

        self.text = ""

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text = file.read()
            if len(self.text) > 0 and not self.generate_button.winfo_ismapped():
                self.generate_button.pack()

    def generate_word_cloud(self):
        if not self.text:
            return

        # Remove punctuation and lowercase the text
        translator = str.maketrans('', '', string.punctuation)
        text = self.text.translate(translator).lower()

        # Remove stopwords
        stop_words = set(stopwords.words('spanish'))
        words = [word for word in text.split() if word not in stop_words]

        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))

        # Display the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCloudApp(root)
    root.mainloop()
