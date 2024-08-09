---
title: Install SplashKit
sidebar:
  label: 2. SplashKit
  attrs:
    class: linux
---

Once you have installed the [Command Line Tools](/installation/linux/step-1/) you can install SplashKit and build the SplashKit library from its source.

## Steps

### Step 1: Open a terminal

You can do this by either going to the applications menu and searching for "Terminal" or by pressing `Ctrl + Alt + T` on your keyboard.

![Opening a terminal in Linux](/gifs/linux/open-terminal.gif)

### Step 2: Install Splashkit Manager

Install the SplashKit Manager by copy/pasting the command below into your terminal and press enter.

```shell
bash <(curl -s https://raw.githubusercontent.com/splashkit/skm/master/install-scripts/skm-install.sh)
```

The output should look something like this:

![Terminal](/images/installation/linux/linux-installation-fig1.png)

### Step 3: Execute skm

**Restart** the terminal and execute `skm` to test it was successfully installed.

```shell
skm
```

You should see the following messages:

```shell
SplashKit is installed successfully!
Missing skm command. For help use 'skm help'
```

The output should look something like this:

![Terminal](/images/installation/linux/linux-installation-fig2.png)

### Step 4: skm Linux Install

Run the following command to install the necessary dependencies and compile splashkit.

```shell
skmlinux install
```

This will take some time to complete, and you may be prompted to enter your password.

![Terminal](/images/installation/linux/linux-installation-fig3.png)
![Terminal](/images/installation/linux/linux-installation-fig4.png)

### Step 5: Global Install

Run the following command to install splashkit globally.

```shell
skm global install
```

You should see the following messages:

```bash
Splashkit is installed correctly!
Done
Global command run successfully
```

![Terminal](/images/installation/linux/linux-installation-fig5.png)
