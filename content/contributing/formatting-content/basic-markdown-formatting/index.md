---
title: "Basic Markdown Formatting"
description: ""
lead: ""
date: 2021-05-20T19:23:22+01:00
lastmod: 2021-05-20T19:23:22+01:00
draft: false
images: []
menu: 
  contributing:
    parent: "formatting-content"
weight: 6
toc: true
---

Doks uses Goldmark markdown which is primarily Github-flavoured.

The examples below follow our [Style Guide](../style-guide).

## Headings

{{< warning >}}
**Warning:** We do not allow `# Header 1` sizing, this should only be added by the title of the article, use `## Header 2` sizing and below for in-article headers.
{{< /warning >}}

Headings in markdown can be added using the `#` character at the beginning of a line of text, the more`#` you use the smaller the heading will be.

All headers, once rendered, in an article can be permalinked to easily share a specific topic quickly.

```md
## Example Header 2
### Example Header 3
```

This would render as:

## Example Header 2
### Example Header 3

## Emphasis

Markdown allows you to add emphasis to text in line using `*` at both ends of some text.

Emphasis includes Bolding and Italicizing but ***not*** Underlining.

```md
*This is italicized*
**This is bolded**
***This is both italicized and bolded***
```

*This is italicized*</br>
**This is bolded**</br>
***This is both italicized and bolded***</br>

## Linebreaks

While Markdown is usually very respectful of where a new line should be implemented it is sometimes necessary to add artifical breaks.

This can be done using the `<br>` tag.

```md
This is<br> a line break
```
This is<br> a line break

## Creating Lists

You can create both ordered lists and unordered lists with markdown.

### Ordered Lists

Ordered lists can be created either specific numbers.

```md
1. This is 
2. An Example
3. Of an Ordered List
```
1. This is 
2. An Example
3. Of an Ordered List

### Unordered Lists

Unordered Lists can be created using `*` at the beginning of a line.

```md
* This is
* An Example
* Of an Unordered List
```

* This is
* An Example
* Of an Unordered List

### Sub-Items in a List

You can also make sub-items in either ordered or unordered lists indenting by a tab.

```md
* This is
* An Example
  * Of sub items
    * And how to format them
* In an Unordered List
```

* This is
* An Example
  * Of sub items
    * And how to format them
* In an Unordered List