---
title: "Adding Content Sections to Jitsuin Docs"
description: ""
date: 2021-05-20T12:03:27+01:00
lastmod: 2021-05-20T12:03:27+01:00
draft: false
menu:
  contributing:
    parent: "adding-content"
weight: 4
images: []
toc: true
---

{{< note >}}
**Note:** For navigation purposes any new content is automatically added to the top level `content` folder and then follows the path you specify from there.
{{< /note >}}

1. To add a New Content Section use the `jitsuin-doks` command

```bash
jitsuin-doks create docs/user-patterns/_index.md
```
Here you can see we have specified the `docs` area, the name of our new section and we use the underscored `_index.md` to indicate it is an indexing section of content

{{< note >}}
**Note:** The name of each folder should be sluggified 
   The command can then prefill the metadata accordingly
{{< /note >}}

2. This will create the space in the docs folder for your new section, to then make it visible in the sidebar add it to `config/_default/menus.toml` using the following format:

```toml
[[docs]]
  name = "User Patterns"
  weight = 4
  identifier = "user-patterns"
  url = "/docs/user-patterns/"
```

Where the value in the square brackets is the area of content you are contributing to, in this case `docs`

You must also specify the following values:

* `name` - The name of the new section as it should appear to Users
* `weight` - Where the new section should be added to in the Tables of Content on the left (in numerical order)
* `identifier` - A unique idenitfier for your content section, this should be the sluggified version of the `name`
* `url` - where the new section header will lead to, this should match the directory structure of the command in Step 1

3. You should now see your new section on the left