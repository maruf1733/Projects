from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

# Open and read the content of the text file
with open('names.txt', 'r') as file:
    text = file.read()

# Load the mask image
python_mask = np.array(PIL.Image.open("maruf.png"))

# Generate the word cloud
wc = WordCloud(stopwords=STOPWORDS, mask=python_mask, background_color="white", contour_color="black",contour_width=10, min_font_size=12,max_words=40).generate(text)

# Display the word cloud
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
