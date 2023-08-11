# TO BE DEFINED

![Alt text](images/SunTzu.jpg?raw=true "Sun Tzu - The Art of War")

## 0. Code Of Conduct
In these challenges you will learn some basic cyber security skills including ethical hacking. It is crucial to understand (and therefor necessary to do as a first challenge) that you need to follow a code of conduct and respect any laws and regulations applicable. If you are not sure if it is legal and without consequences --> DO NOT PROCEED! 

The examples below all refer to the UCLL website for which you have the right to perform the suggested actions. If you - unintentionally - do find confidential or personal data, you should inform us asap through e-mail at the following email address: privacy@ucll.be 

## 1. Prerequisites

-   Challenges that need to be completed before this one.
-   ...

## 2. Introduction

This challenge is built upon the structure of a cyber attack (as described by Martin Lockheed in the Cyber Kill Chain paper). The Cyber Kill Chain paper can be found at https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf. However, there is a really cool video explaining it all very well - if you don't like to read: https://www.youtube.com/watch?v=II91fiUax2g 

Other frameworks about the attaking process have been defined and are very relevant if you ever want to work in cyber security (either as a pentester or as a defender). Please take a look at the following:
- MITRE ATT&CK Framework (https://attack.mitre.org/): A map of all tactics, techniques and procedures already used by some really advanced hacker groups (also called APT's = Advanced Persistent Threat). Explanation Video: https://youtu.be/GYyLnff2XRo 
- Unified Kill Chain (https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf): Combining the Cyber Kill Chain and MITRE ATT&CK framework since more and more attacks are not just one end-to-end process and one attack can involve multiple cyber kill chains in order to obtain the final objective.

## 3. Challenge

For each challenge there will be a flag to find. The flag (and format) will be specified. Each challenge requires a new line in your solution.txt file.

### 3.1. Reconnaissance
Read about the reconnaissance phase of the cyber kill chain, what is the difference between active and passive reconnaissance? 

#### 3.1.1 Active versus Passive Reconnaissance

Below are three actions performed by a hacker, what type of reconnaissance is the hacker doing (answer only with “A” for active and “P” for Passive)? 
- The hacker visits the website of the UCLL school, hoping to get some of their employee names. What kind of reconnaissance activity is this? (A for active, P for passive) 
- The hacker pings the IP address of the UCLL school webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? (A for active, P for passive)
- The hacker meets the IT administrator of the UCLL and tries to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? (A for active, P for passive)

The flag corresponds to the three letters (A or P) that correspond to the answers. No spaces in between, for example, if you would answer P three times: __PPP__).

#### 3.1.2 Google Dorking

Info: https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/

Google Dork the internet to find a PDF file from the UCCL college in which there is a list of student numbers listed in classes for a certain bachelor programme ("indeling") in the year 2019. All you know is that it's for the year 2019. In case you would find two similar files, take the one where some student numbers are highlighted.

The flag corresponds to the highligthed number (xxxxxxx) in the third column. Example: __0864795__

#### 3.1.3 Whois

Using the whois command is often the first thing to check for a website. It is available in any Linux environment or WSL in your Windows environment (or also in the Microsoft SysInternals Suite, highly underestimated tools which are very useful for security purposes, documentation: https://learn.microsoft.com/en-us/sysinternals/). Using whois, answer the following questions.

The flag is composed of several lines, one line per answer:
- Line 1: The name of the registrar for the UCLL website
- Line 2: The name (EN abbreviation) of the law preventing to show too much information when performing the whois command
- Line 3: The name of the registrar for the Microsoft website
- Line 4: The date when  Microsoft.com was registered? DDMMYYYY is the format to use (no other special characters)
- Line 5: The full mail address of the domain administrator


### 3.3. Task 

...

### 3.4. Task 

...

### 3.5. Task 

...

### 3.6. Task 

...

## 4. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
