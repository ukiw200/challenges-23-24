# Git basics

## 1. Prerequisites

-   Introduction challenge (with git installation and explanation) is completed.

## 2. Introduction

You already got the general explanation of Git and its installation in the introduction challenge. In this challenge, you will be introduced to the basic operations of version control with Git: add, commit and push.

Initially, when you make changes to files in your working directory, Git considers them to be in "untracked" state. By using the `git add` command, you can selectively choose which files to include in the next commit (move them to the "staged" state).

The command `git commit` is used to save all the staged changes in the Git history. Every commit represents a snapshot of the changes made to the git repository.

Finally, with `git push` you upload your local commits to a remote git repository. In this course, your remote repository is hosted in Github.

## 3. Challenge

### 3.1. Add, commit and push a file

-   Create a new file in this folder named "solution.txt" and put your name on the first line and your student number on the second line.
-   In Git bash, run the following command:

    ```bash
    $ git status
    ```

-   As you can see, git is now detecting the file. But it has not yet been added to our local git repository. To do this you execute:
    ```bash
    $ git add solution.txt
    $ git commit -m "Solution file"
    ```
    Via `git add` you tell git to track the file, `git commit` is going to effectively add the file to the local repository. With the "-m" option, you add a message to the commit.
-   Now go to your github repository via a browser and navigate to the "git-challenges/01-basics" folder. As you can see, your solution.txt file is not there yet. This is because we need to "push" the changes you just made on your local repository to the remote version:
    ```bash
    $ git push
    ```
    Refresh your browser and you will see that the file (with the commit message) is now present.
-   You can run the status command again. Normally, the output should be as follows:

    ```text
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean
    ```

### 3.2. Add, commit and push a folder

Create a subfolder named 'challenge-1' in the '01-basics' folder. Create a new file "solution.txt" with the text "challenge 1 completed" on the first line. Make sure that this folder is pushed to your remote repository.

## 4. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
