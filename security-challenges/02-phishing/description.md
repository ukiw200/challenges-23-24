# Git basics

## 1. Prerequisites

- Creating a free account on the www.tryhackme.com platform (niet meer nodig in mijn nieuwe vorm)


## 2. Introduction



## 3. Challenge


### 3.1. Add, commit and push a file

-   Create a new empty file in the same folder as these instructions with the name "solution.txt".
-   In Git bash (started in the root challenges folder), run the following command:

    ```console
    $ git status
    ```

-   You will see that git is not yet tracking the file. The output should look like:

    ```text
    On branch master
    Your branch is up to date with 'origin/master'.

    Untracked files:
        (use "git add <file>..." to include in what will be committed)
            ...

    no changes added to commit (use "git add" and/or "git commit -a")
    ```

-   In the "..." in the output above, you will see a line for each untracked file. Copy the line containing your solution file and paste it on the first line of solution.txt. Make sure you don't copy any leading or trailing spaces, just the text itself. Otherwise, the verification script will fail.
-   Stage the file and commit it to your local repository:
    ```console
    $ git add solution.txt
    $ git commit -m "Solution file"
    ```
    Via `git add` you tell git to track the file, `git commit` is going to effectively add the file to the local repository. With the "-m" option, you add a message to the commit.
-   Now go to your github repository via a browser and navigate to the "git-challenges/01-basics" folder. As you can see, your solution.txt file is not there yet. This is because we need to "push" the changes you just made on your local repository to the remote version:
    ```console
    $ git push
    ```
    Refresh your browser and you will see that the file (with the commit message) is now present.
-   You can run the status command again. Normally, the output should be as follows:

    ```text
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean
    ```

### 3.2. Add, commit and push a folder

Create a new file "solution.txt" with the same flag as entered in the tryhackme room 

 named 'challenge-1' in the '01-basics' folder. Create a new file "solution.txt" with the text `challenge 1 completed` on the first line. Make sure that this folder is pushed to your remote repository.


## 4. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

-   You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
-   Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
-   Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
-   You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
