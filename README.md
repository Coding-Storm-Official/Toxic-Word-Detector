# <div align="center">Toxic Word Detector</div> 
 <p align="center">
  <img 
    width="500"
    height="350"
    src="https://user-images.githubusercontent.com/96690322/188764931-ffe77a5d-e849-4b38-938a-eeb001eab6e9.jpeg"
  >
</p>
<div align = "center">
The program uses TextBlob to analyse the text and determine if it is a toxic or a non toxic text. 

<br>
<br>

![Logo](https://img.shields.io/github/commit-activity/w/Coding-Storm/Text-Sentimetal-Analysis?color=brightgreen&label=commits&logo=python&logoColor=gold&style=for-the-badge) &nbsp; &nbsp; &nbsp; ![Maintained - Yes](https://img.shields.io/badge/Maintained-Partially-gold?style=for-the-badge&logo=github&logoColor=gold) &nbsp; &nbsp; &nbsp; [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&logo)](https://opensource.org/licenses/Apache-2.0)
</div>

## Working of the Program
1. An array contains the string(s) to check for toxicity 
2. The string(s) are analysed by TextBlob which uses the averaging technique to determine the polarity of the word contained in the string(s).
3. The polarity value is returned either as 1 or -1 where 1 defines a non toxic word and -1 defines a toxic word.
4. The program uses an if statement to check if the polarity value is greater than 0 or not.
5. It then classifies the word as toxic or non toxic and adds them to their specific array which is then displayed.
![Text](https://user-images.githubusercontent.com/96690322/188584499-75e4e382-8606-4d2d-a0d1-63914ccb5b47.png)

> __Note__
The program is not 100% accurate and might falsely flag non toxic texts as toxic and vice versa.The software/license owner can be charged for damages.

<br>

Thank you!

