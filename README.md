# Text-Sentimetal-Analysis
The program using TextBlob to analyse the text and determine if it is a toxic or a non toxic text. 

## Working of the Program
1. An array contains the string(s) to check for toxicity 
2. The string(s) are analysed by TextBlob which uses the averaging technique to determine the polarity of the word contained in the string(s).
3. The polarity value is returned either as 1 or -1 where 1 defines a non toxic word and -1 defines a toxic word.
4. The program uses an if statement to check if the polarity value is greater than 0 or not.
5. It then classifies the word as toxic or non toxic and adds them to their specific array which is then displayed.
![Text](https://user-images.githubusercontent.com/96690322/188584499-75e4e382-8606-4d2d-a0d1-63914ccb5b47.png)


## Accuracy
The program is not 100% accurate and works properly for only 1 word in a single string.

Thank you!

