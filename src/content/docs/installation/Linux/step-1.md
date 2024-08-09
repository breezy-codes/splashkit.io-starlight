---
title: Install Command Line Tools
sidebar:
  label: 1. Command Line Tools
  attrs:
    class: linux
---

To install SplashKit, you will firstly need to install some command line tools using the apt or apt-get package manager.

## Steps

1. Open up a terminal,you can do this by either going to the applications menu and searching for "Terminal" or by pressing `Ctrl + Alt + T` on your keyboard.

    ![Opening a terminal in Linux](/gifs/linux/open-terminal.gif)

2. Update the package list using the following command:

    ```shell
    sudo apt update && sudo apt upgrade -y
    ```

    You will be prompted to enter your password. This is the password you use to log in to your computer.

3. Then install Command Line Tools: **curl** and **git**, which will be used in the SplashKit install process.

    Install using your package manager. For example:

    ```shell
    sudo apt-get install curl git
    ```
