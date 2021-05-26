---
title: "Adding Articles to Jitsuin Docs"
description: ""
date: 2021-05-20T18:34:21+01:00
lastmod: 2021-05-20T18:34:21+01:00
draft: false
menu:
  contributing:
    parent: "adding-content"
weight: 3
images: []
toc: true
---

{{< note >}}
**Note:** For navigation purposes any new content is automatically added to the top level `content` folder and then follows the path you specify from there.
{{< /note >}}

1. To add a New Article use the `jitsuin-doks` command

```bash
jitsuin-doks create contributing/adding-content/adding-articles-to-doks/index.md
```
Here you can see we have specified the `contributing` area, the `adding content` section and the name of our new article with a non-underscored `index.md` to indicate this is an article

{{< note >}}
**Note:** The name of each folder should be sluggified, the command can then prefill the metadata accordingly.
{{< /note >}}

2. Edit the newly created document and you should see a metadata template that has been prefilled at the top of the article

```markdown
---
title: "Adding Content Sections to Doks"
description: ""
date: 2021-05-20T12:03:27+01:00
lastmod: 2021-05-20T12:03:27+01:00
draft: false
menu:
  contributing:
    parent: "adding-content"
weight: 2
images: []
toc: true
---
```

There are a lot of attributes here but the key ones to set are as follows:

* `title` - This is the title that users will see, this should be prefilled by the `jitsuin-doks` command
* `description` - A description of the articles
* `draft` - If set to `true` this article will not be included or visible to Users (including the Developer Serve), this should be set to `false` when ready to publish
* `menu` - This indicates the hierarchy of the article
    *  `contributing` is the name of the area this article belongs to, for `docs` use that tag instead
        *  `parent` is the content section the article belongs to, use the sluggified identifier 
* `weight` - The numerical order in which the article should appear 
* `toc` - If set to `true` this will make sure the article is listed in the sidebar

3. Once all of the correct attributs have been set the article should be visible in the sidebar