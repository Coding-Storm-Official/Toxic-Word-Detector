from textblob import TextBlob

texts = ['Idiot','Smart']

non_toxic = []
toxic = []

for text in texts:
    text_polarity = TextBlob(text).sentiment.polarity
    if text_polarity > 0:
        non_toxic.append(text)
        continue
    toxic.append(text)
print("Made by Coding-Storm")
print('Non toxic : ',non_toxic)
print('Toxic : ',toxic)
