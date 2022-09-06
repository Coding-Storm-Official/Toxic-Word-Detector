from textblob import TextBlob

feedbacks = ['Idiot','Smart']

non_toxic = []
toxic = []

for feedback in feedbacks:
    feedback_polarity = TextBlob(feedback).sentiment.polarity
    if feedback_polarity > 0:
        non_toxic.append(feedback)
        continue
    toxic.append(feedback)

print('Non toxic : ',non_toxic)
print('Toxic : ',toxic)