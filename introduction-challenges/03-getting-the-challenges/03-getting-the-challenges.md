# Getting the challenges

## 1. Prerequisites

Visual Studio Code is installed.
Git is installed.
You have a GitHub account.

## 2. Introduction

In this challenge we will make sure that you have access to the challenges on your own computer.

## 3. Challenge

### 3.1. Accept the GitHub Classroom Assignment

1. Navigate to <a href="link toevoegen" target="_blank">this page</a>
1. Select your name from the list
    * Selecting your name in assignments like this makes sure that we see your real name instead of your GitHub username in overview screens
    * This is very helpful for us when managing large groups of students (eg. when searching the repository of a certain student)
    * It can be that your name is not in the list (especially if you enrolled later), select `Skip to the next step` in this case
1. Click on `Accept this assignment`
1. A repository is now being made for you. Refresh the page every minute until your repository is ready.
1. Clink the link to your assignment repository.

### 3.2. Clone the Repository

1. If you clicked the link to your assignment repository you should land on a page that looks like this (the URLs and repository names will be different of course):

<a href="./cloning-a-repository.png" target="_blank">
    <img src="./cloning-a-repository.png">
</a>

1. This screen will make more sense after working with git for a bit. For now, just follow the instructions as provided here.
1. Make sure that `HTTPS` is selected. Then copy the URL.

<a href="./cloning-a-repository-2.png" target="_blank">
    <img src="./cloning-a-repository-2.png">
</a>

1. Open a shell by...
     * On Windows, opening start and typing `git bash` followed by enter
     * On macOS, opening a terminal (enter `terminal` in Spotlight Search)
1. Navigate to the folder where you want to store the challenges on your pc
     * You can do this by typing `cd "/path/to/folder"` in your shell
     * For example `cd "/mnt/c/Bram/Vakken/2023 - 2024/Introductieproject/challenges-23-24"`
1. Enter:
   ```bash
   git clone <copied-url>
   ```
   Github will now ask for your username and password
1. When you enter your password you will get a warning that it is not allowed to interact with GitHub via your "root" account password. You have two options:
     * [Using a Credentials Manager](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git#git-credential-manager)
     * [Using a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
1. Normally the Credentials Manager will open automatically and you can proceed. If it does not, follow the guide to create and use a Personal Access Token.
     * Note, if you have already used git in the past with a different GitHub account it might be that those credentials are still stored in your Credentials Manager. Search how you can remove them or ask a teacher for help.
1. After authenticating yourself you can retry the clone command:
   ```bash
   git clone <copied-url>
   ```
1. You now have all challenges stored locally!
1. Read the [readme](./../../README.md) to find your footing

### 3.3. Finishing up

That's it! But what have we done exactly? What is git and GitHub, why is it so important and how does it work?

The best way to find out is by continuing with the [git challenges](./../../git-challenges/01-basics/git-basics.md) on your own computer.