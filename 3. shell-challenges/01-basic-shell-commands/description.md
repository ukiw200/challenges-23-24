# Shell

## 1. Introduction

The Linux shell is a command-line interface (CLI) that allows users to interact with the Linux operating system by entering text-based commands. It provide tools for file system management, text processing, scripting and much more.

Users working in a Linux environment have access to the shell by default. Windows users can use a terminal emulator to have the same functionality available. `Git Bash` is one such terminal emulator that comes with Git for Windows, providing a collection of tools commonly used in Linux environments.

Read the basics about using the shell and some frequently used commands on [Linux Journey](https://linuxjourney.com/lesson/the-shell).

## 2. Challenge

Try to complete the following steps using only the shell. You can use the website above as a reference.

1. Navigate to the `shell-challenges` folder using the `cd` command:

   ```console
   $ cd shell-challenges
   ```

2. Create a new directory called `solution` using the appropriate command.
3. Navigate to the `solution` folder using the `cd` command.
4. Create a new file called `solution.md` using the appropriate command.
5. Navigate back to the `shell-challenges` folder. You can use the `..` shortcut to navigate to the parent folder:
   ```console
   $ cd ..
   ```
6. Copy (not move) the `solution.md` file to the current folder using the appropriate command. You can refer to the current folder by using the `.` shortcut.
7. Rename the `solution.md` file to `solution.txt` using the appropriate command.
8. Remove the solution folder. Since the folder is not empty, you cannot use the `rmdir` command.
9. Open `solution.txt` and add:

   - On the first line the full command you used in step 2.
   - On the second line the full command you used in step 4.
   - On the third line the full command you used in step 6.
   - On the fourth line the full command you used in step 7.
   - On the fifth line the full command you used in step 8.

   Like always, make sure that you don't have any leading or trailing spaces in your file.

10. Display the contents of the `solution.txt` in the shell using the appropriate command. Put this command on the sixth line of the solution file.
11. If you followed the steps precisely as instructed, the verification script should return "SUCCESS". Please commit your solution.txt to GitHub.

## 3. General rules

In order to get a "SUCCESS" from the verify script, you will need to make sure that:

- You have followed the instructions exactly as described in the text. Do not put extra text in files or create extra folders unless asked to do so.
- Assume that the verify script is case-sensitive. Pay attention to the exact naming of files and folders.
- Never make changes to the verify script (yes, we will verify all verify scripts afterwards). Changes to the verify script will result in a "FAIL" for the entire challenge.
- You will only receive a "SUCCESS" if you complete all the steps successfully. If you only complete part of the challenge steps, you will receive a "FAIL" for the entire challenge.
