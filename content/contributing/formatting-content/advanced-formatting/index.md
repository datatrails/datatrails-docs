---
title: "Advanced Formatting"
description: ""
lead: ""
date: 2021-05-20T19:23:22+01:00
lastmod: 2021-05-20T19:23:22+01:00
draft: false
images: []
menu: 
  contributing:
    parent: "formatting-content"
weight: 7
toc: true
---

As Doks is based on Hugo it has many more extensible formatting options, including some custom tools we have added ourselves to enhance the delivery of documentation overall.

The examples below follow our [Style Guide](../style-guide).

## Code and Codeblocks

There are three different ways to present code and references in Jitsuin Documentation.

### Inline Code

When talking about a single word, line of code or attribute in a whole sentence you can use single backticks (`` ` ``) to highlight the specific word or phrase.

```md
This is a`single phrase` being highlighted.
```

This is a `single phrase` being highlighted.

If you wish to escape 1 or more backticks in inline code use double backticks ``` `` ```.

```md
`` This is `an example` that uses backticks. ``
```

`` This is `an example` that uses backticks. ``

### Syntax Highlighting

Syntax highlighting is built into codeblocks when a language is specified, as such there should ***always*** be a language specified against at the beginning of any codeblock.

Supported Languages:

* `javascript`
* `json`
* `bash`
* `html`
* `ini`
* `toml`
* `yaml`
* `md` (markdown)
* `go`
* `python`

### Simple Codeblock

If you want to add a simple codeblock for a specific example, say it is a single bash command or some example markdown you can use three backticks `` ``` `` as a fence around the block.

By specifying the language at the beginning of the code block the website will know add the `copy-to-clipboard` functionality to the block.

<pre><code>
```md
This is markdown.
```
</code></pre>


```md
This is markdown.
```

And with Bash

<pre><code>
```bash
echo "This is a Bash Example."
```
</code></pre>


```bash
echo "This is a Bash Example."
```

### Tabbed Codeblock

Tabbed Codeblocks are not built into either Doks or Markdown, we instead use a customised HTML template that can perform the same function using Hugo Shortcodes.

Each `Tabs` object on a page should have a unique identifier, you should also specify the language syntax highlighting to use per tab, this should be reflected in the title of the tab where appropriate.

Similarly to the Simple Codeblocks by adding the language the website will know to add the `copy to clipboard` functionality to the block.

```go
{{</* tabs name="tab_with_code" >}}
{{{< tab name="Bash" codelang="bash" >}}
echo "This is a Bash Example."
{{< /tab >}}
{{< tab name="Go" codelang="go" >}}
println "This is a Go Example."
{{< /tab >}}}
{{< /tabs */>}}
```

{{< tabs name="tab_with_code" >}}
{{< tab name="Bash" codelang="bash" >}}
echo "this is a command"
{{< /tab >}}
{{< tab name="Go" codelang="go" >}}
func main() {
    fmt.Println("hello world")
}
{{< /tab >}}}
{{< /tabs >}}

### Adding OpenAPI Docs

OpenAPI (formely Swagger) is an open standard for documenting which methods, parameters and responses are available for REST API Endpoints in `JSON` format.

Jitsuin RKVST maintains up-to-date records of every API we present to users in an OpenAPI format, these are fairly plain however so we have written a custom shortcode to template the details in a more presentable package.

There will be no rendered output here as it will otherwise interrupt the document, however here is the reference to include when making an OpenAPI Page:

```go
{{</* openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/access_policies.swagger.json" */>}}
```

This shortcode will fetch the docs from the specified url and then render it completely fully templating out each method and endpoint, the parameters, responses and examples.

## Callouts and Blocked Quotes

Sometimes when writing documentation it is necessary to add notes, warnings and other callouts in order to highlight specific information, we have added some custom callouts using Hugo Shortcodes.

### Notes

To add a note use the following syntax, notes are always highlighted by a left ***purple*** border.

```go
{{</* note >}}
**Note:** This is a note.
{{< /note */>}}
```


{{< note >}}
**Note:** This is a note.
{{< /note >}}

### Cautions

To add a caution use the following syntax, cautions are always highlighted by a left ***yellow*** border.

```go
{{</* caution >}}
**Caution:** This is a caution.
{{< /caution */>}}
```

{{< caution >}}
**Caution:** This is a caution.
{{< /caution >}}

### Warnings

To add a warning use the following syntax, warnings are always highlighted by a left ***red*** border.

```go
{{</* warning >}}
**Warning:** This is a warning.
{{< /warning */>}}
```

{{< warning >}}
**Warning:** This is a warning.
{{< /warning >}}

### Block Quotes

All notes, cautions and warnings use blockquote templates and classes underneath.

Block Quotes are useful syntax to not only represent multiline quotes in markdown but also to create localised sections of content differentiated from code.

A key feature of Block Quotes is that they implement word-wrap so even if you seperate a quote by using a newline it won't render as such.

```md
>This is
>a quote.
```

>This is
>a quote.

Alternatively

```md
>This is a very very very long, almost way too long, I would say incredibly long
>multiline quote.
```

>This is a very very very long, almost way too long, I would say incredibly long
>multiline quote.

Block Quotes do respect some Markdown Syntax though which means you can implement artificial linebreaks using `<br>`.

```md
>This is<br>
>a quote
```
>This is<br>
>a quote

## Tables

Tables are useful for demonstrating a range of information, they can also be rendered in most markdown flavours using ascii denominations.

We use a mixture of markdown and a custom Hugo shortcode to format tables correctly; markdown is used to define the entries in each row and column in a more visual format, and then the encapsulating shortcode is used to parse the resultant html with the correct formatting options (and according to our style guide these are the `table-striped` and `table-bordered` options).

Rendering Markdown Tables can be difficult from scratch, you may wish to make use of an online tool like [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) to help.

```md
{{</* table >}}
|  Column 1 | Column 2  |
|-----------|-----------|
|  Cell 1   | Cell 2    |
{{< /table */>}}
```
{{< table >}}
|  Column 1 | Column 2  |
|-----------|-----------|
|  Cell 1   | Cell 2    |
{{< /table >}}

## Links

Links can be added using standard markdown `[]()` where the contents inside of the square brackets will be what appears to the user and the standard brackets containing the hyperlink.

```md
[This is an example of a link](https://info.jitsuin.com/demo-request).
```

[This is an example of a link](https://info.jitsuin.com/demo-request).

## Images

A big part of any documentation is including screenshots of workflows, architecture diagrams and infographics to help illustrate a point more clearly.

Image formatting and sizing can also be very difficult to get consistently right, luckily Doks has some built-in image shortcodes to help format things properly.

Your image should be saved to the same directory as the article's index.md to use the following examples when adding a screenshot or picture:

```go
{{</* img src="Jitsuin_Logo_RGB_Spot.png" alt="Rectangle" caption="<em>Jitsuin Logo Example</em>" class="border-0" */>}}
```

{{< img src="Jitsuin_Logo_RGB_Spot.png" alt="Rectangle" caption="<em>Jitsuin Logo Example</em>" class="border-0" >}}

### Light Mode and Dark Mode Images

For readability it may be necessary to have two images, one that suits light mode and another dark mode, so that when the mode is toggled it renders correctly.

We have added some customised shortcode that allows you to specify two individual images.

The behaviour matches the original image shortcode but adds an extra `srcDrk` variable which refers to the Dark Mode image you wish to add .

```go
{{</* imgDark src="Jitsuin_Logo_RGB.png" srcDrk="Jitsuin_WhtType_RGB.png" alt="Rectangle" caption="<em>Jitsuin Dark Mode Logo Example</em>" class="border-0" */>}}
```

{{< imgDark src="Jitsuin_Logo_RGB.png" srcDrk="Jitsuin_WhtType_RGB.png" alt="Rectangle" caption="<em>Jitsuin Dark Mode Logo Example</em>" class="border-0" >}}