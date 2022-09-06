from textblob import TextBlob

text = ['Idiot','Smart']

non_toxic = []
toxic = []

for texts in text:
    text_polarity = TextBlob(text).sentiment.polarity
    if text_polarity > 0:
        non_toxic.append(text)
        continue
    toxic.append(text)

print('Non toxic : ',non_toxic)
print('Toxic : ',toxic)
