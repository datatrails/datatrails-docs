---
title: "Creating Your Branch"
description: "Instructions on Creating"
lead: ""
date: 2021-05-23T16:24:38+01:00
lastmod: 2021-05-23T16:24:38+01:00
draft: false
images: []
menu: 
  contributing:
    parent: "adding-content"
weight: 2
toc: true
---

As the main branch of these docs is protected you will need to create a separate branch and submit a PR to make any changes.

1. Change into your cloned repo
    ```bash
    cd rkvst-docs
    ```
1.  Checkout `main` Branch
    ```bash
    git checkout main
    ```
1. Make sure `main` is up to date with the latest changes
    ```bash
    git pull
    ```
1. Create a new branch and check it out automatically
    ```bash
    git branch -M <your-branch-name>
    ```
    If you are resolving a specific GitHub issue you should reference this in your branch name with the following syntax:
    ```md
    <issue number>-<your-branch-name>
    ```