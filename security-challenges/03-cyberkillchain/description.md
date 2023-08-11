# The Cyber Kill Chain

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
Read about the reconnaissance phase of the cyber kill chain. Can you tell the difference between active and passive reconnaissance? 

#### 3.1.1 Active versus Passive Reconnaissance

Below are three actions performed by a hacker, what type of reconnaissance is the hacker doing (answer only with “A” for active and “P” for Passive)? 
- The hacker visits the website of the UCLL school, hoping to get some of their employee names. What kind of reconnaissance activity is this? 
- The hacker pings the IP address of the UCLL school webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? 
- The hacker meets the IT administrator of the UCLL and tries to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? 

The flag corresponds to the three letters (A or P) that correspond to the answers. For example, if you would answer P three times: __PPP__.

#### 3.1.2 Google Dorking

Info: https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/

Google Dork the internet to find a PDF file from the UCCL college in which there is a list of student numbers listed in classes for a certain bachelor programme ("indeling") in the year 2019. All you know is that it's for the year 2019. In case you would find two similar files, take the one where some student numbers are highlighted.

The flag corresponds to the highligthed number (xxxxxxx) in the third column. Example: __0864795__

#### 3.1.3 Whois

Using the whois command is often the first thing to check for a website. It is available in any Linux environment or WSL in your Windows environment (or also in the Microsoft SysInternals Suite, highly underestimated tools which are very useful for security purposes, documentation: https://learn.microsoft.com/en-us/sysinternals/). Using whois, answer the following questions.

The flag is composed of several lines, one line per answer:
- Line 1: The name of the registrar for the UCLL website
- Line 2: The name (EN abbreviation) of the law preventing to show too much information when performing the whois command
- Line 3: The full name of the registrar for the Microsoft website 
- Line 4: The IANA ID number of the registrar for the Microsoft website 
- Line 5: The full mail address of the domain administrator


### 3.2. Weaponization
Read about the weaponization phase of the cyber kill chain. What kind of weapons could an attacker create? The most common weapon is some kind of malware. A list of different malware types can be found at: https://www.malwarefox.com/malware-types/

Now, take a look at the attached document "WinPrices.docm" in the folder "attachments" and answer the following questions.

Did you enable the macro in Word on your computer? This could have been dangerous! Always use a sandbox if you are unsure! Any.run (https://app.any.run/) is a free online sandbox you can use to run on any suspicious file. Also, virustotal (https://www.virustotal.com) is a great resource as well. Any.Run will execute the file and you can watch the activity. Virustotal will mainly check the checksum of the file and match with signature databases from antivirus products.

Check both tools for this file.

The solution.txt is composed of several lines, one line per answer:
- Line 1: MD5 hash of the file
- Line 2: What MITRE Technique is being used (we need the identifier, starting with T)? 
- Line 3: What was the main goal of using this technique? Hint: two words starting with “D”
- Line 4: How do hackers mostly do this? Hint: One word starting with “O”
- Line 5: What's the hidden flag in this document? Hint: the flag starts with "flag{"


### 3.3. Delivery 

Try to send this document to yourself ... does the mail solution detects anything suspicious?

#### 3.3.1 

#### 3.3.2

#### 3.3.3 

#### 3.3.4 



### 3.4. Exploitation 
Exploitation is the fase where a vulnerability in the system is being exploited. However, most of the time, the vulnerability being exploited is the human behind the system. This type of attack can be described as "Social Engineering". The most common attack is a phishing attack that, which we will explore in detail in here. However, the social engineering attack starts with some basic reconnaissance, weaponization and delivery as well. 

Map the following activities to the correct phase of the Cyber Kill Chain (R for reconnaissance, W for weaponization and D for Delivery):
- the attacker must prepare a web page to grab credentials
- the attacker must know where to send his message to 
- the attacker must prepare a convincing message to persuade users into clicking the link
- the attacker must find a way of getting his message to the users






### 3.5. Installation 

...

### 3.6. Command & Control (C2) 

Command and Control (C2) infrastructure is a critical component of various cyberattacks, often associated with malicious activities such as creating botnets, executing remote commands on compromised systems, and distributing malicious payloads. Let's break down the key concepts in this context:

    - Zombies: In the context of C2, zombies are computers or devices that have been compromised by a malicious actor. These compromised systems are under the control of the attacker and can be used to carry out various tasks without the knowledge or consent of the device owner.

    - Botnet: A botnet is a network of compromised devices (zombies) that are controlled by a central entity, usually the attacker. Botnets are used for various malicious purposes, such as launching distributed denial-of-service (DDoS) attacks, distributing spam, or carrying out coordinated cyberattacks.

    - Shell: A shell refers to a command-line interface that allows a user to interact with a computer's operating system. In the context of C2, gaining a shell on a compromised system provides the attacker with direct access to execute commands on that system.

    - Agent: An agent is a piece of malicious software (malware) that is installed on a compromised system and acts as a conduit for the attacker. The agent communicates with the C2 server, receiving commands and sending back information about the compromised system.

    - Payload: A payload is the malicious code or action that an attacker delivers to a compromised system. This could include executing a malicious program, stealing sensitive data, or initiating further actions, all of which are dictated by the attacker through the C2 server.

    - Beacon: A beacon is a signal or message sent by a compromised system to the C2 server to indicate that the system is still active and ready to receive commands. Beacons are often designed to be stealthy, making detection more difficult.

    - C2 Server: The C2 server is the central control point for the attacker. It receives communication from the compromised agents (zombies), issues commands to these agents, and gathers information from the compromised systems. The C2 server plays a pivotal role in managing the botnet and orchestrating the attack.

C2 Frameworks (Products) and Capabilities:

Several C2 frameworks (also known as C2 tools or platforms) are used by both malicious actors and security professionals for testing and defense. Here are a few notable ones:

    - Metasploit: Metasploit is a widely used penetration testing framework that includes a robust C2 infrastructure. It allows security professionals to simulate real-world attacks, assess vulnerabilities, and test defenses.

    - Cobalt Strike: Cobalt Strike is a commercial penetration testing tool that includes advanced C2 capabilities. It's often used by security teams for red teaming exercises to test an organization's security posture.

    - Empire: Empire is an open-source post-exploitation framework that provides a versatile C2 platform. It's designed for offensive security operations, enabling operators to interact with compromised systems.

    - PowerShell Empire: A post-exploitation framework built on top of PowerShell, enabling attackers to control compromised systems through PowerShell scripts. It's particularly effective in environments where PowerShell is commonly used.

These C2 frameworks provide various capabilities, including the ability to execute commands on compromised systems, pivot through networks, maintain persistence, exfiltrate data, and simulate different types of attacks. It's important to note that while these tools can be used by security professionals for legitimate purposes, they can also be misused by malicious actors, highlighting the importance of cybersecurity awareness and defense.

Remember, the knowledge and understanding of C2 infrastructure are essential for both offensive (ethical hacking, penetration testing) and defensive (cybersecurity) purposes.

### 3.6. Action On Objectives 
A threat actor can either be an individual, but most likely it will be a group of hackers that have sophisticated skills and a lot of money (often referred to as an APT). A threat actor can have several motivations to perform a cyber attack. They might be interested in:

- the money (performed by criminal organizations), often by compromising systems or exfiltrating data and asking for a ransom 
- seeking the thrill and satisfaction (performed by thrill-seekers)
- espionage for geopolitical advantages, cyber warfare (performed by nation states)
- making a statement for good purposes (performed by hacktivists) or for bad purposes like terrorism (performed by terrorist groups), often by performing a denial-of-service (DoS) attack
- making a statement for bad purposes form inside of the organization (performed by insiders)





## 4. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
