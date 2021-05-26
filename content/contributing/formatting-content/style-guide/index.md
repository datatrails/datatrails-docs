---
title: "Style Guide"
description: ""
lead: ""
date: 2021-05-20T19:23:22+01:00
lastmod: 2021-05-20T19:23:22+01:00
draft: false
images: []
menu: 
  contributing:
    parent: "formatting-content"
weight: 8
toc: true
---

It is important in any documentation to have a readable, sane and consistent experience, to that end we have defined some guidelines to ensure all content meets the same standard.

## Documentation Structure

Content is organised at a directory level using the standard Hugo format, we then have four seperate areas of content.

Typically, only Docs should be edited but permission to add to the other sections will be decided on a case by case basis by Jitsuin Emplyees and Organizational Reviewers.

{{< tabs name="directory_structure" >}}
{{< tab name="Root" codelang="bash" >}}
.
├── archetypes
├── assets
├── babel.config.js
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── config
├── content
├── data
├── images
├── jitsuin-doks
├── layouts
├── LICENSE
├── netlify.toml
├── node_modules
├── package.json
├── package-lock.json
├── README.md
├── resources
├── static
└── theme.toml
{{< /tab >}}
{{< tab name="Content" codelang="bash" >}}
.
├── contributing
├── docs
├── _index.md
├── privacy-policy
├── sales
└── support
{{< /tab >}}
{{< tab name="Docs" codelang="bash" >}}
.
├── _index.md
├── overview
├── quickstart
├── setup-and-administration
└── user-patterns
{{< /tab >}}
{{< /tabs >}}

### Articles and Sections

The Jitsuin Docs are primarily written in `Articles`, individual bodies of text, which are then organised by `Sections` that belong to an `Area` such as Docs or Contributing.

At a directory level this looks like this:

```bash
./content/docs/quickstart/when-who-did-what-to-a-thing/index.md
```

Where under the root content folder we can see the `docs` area, followed by the `quickstart` section, containing the article `when-who-did-what-to-a-thing`.

Note that all of these are directories, ending in the file `index.md`, where the actual content of the article is written to.

Every Article and Section contains an `index.md` file with some slight differences in the name depending on which type you are dealing with.

* Articles use `index.md` which represents a standard content file
* Sections use `_index.md` which has special significance as it will automatically index all of the sub-folders and their `index.md` files

Both of these may be prefilled using a template described in the `Archetypes` folder when using the `jitsuin-doks` wrapper to create content.

In terms of naming convention, at the directory level you should always use a sluggified name that represents the title of the Article or Section you are creating.

For example, `When Who Did What to a Thing` becomes `when-who-did-what-to-a-thing`.

This is important as not only will that be represented at a URL level when accessing the docs; the `jitsuin-doks` wrapper will also be able to prefill the titles of `index.md` files in any templates. 

{{< caution >}}
**Caution:** Title rendering in templates is not perfect, you should always verify the title of an Article or Section is correct in the metadata manually.
{{< /caution >}}

Follow these links for more information on adding [Articles](../../adding-content/adding-articles-to-jitsuin-docs/) or [Sections](../../adding-content/adding-content-sections-to-jitsuin-docs/) to Jitsuin Docs.

### Article Metadata

The standard template for both Docs and Contributing is as follows:

```toml
---
title: "Style Guide"
description: "Documentation Style Guide"
lead: "Documentation Style Guide"
date: 2021-05-20T19:23:22+01:00
lastmod: 2021-05-20T19:23:22+01:00
draft: false
images: []
menu: 
  contributing:
    parent: "formatting-content"
weight: 8
toc: true
---
```

While most of this will come prefilled you will need to make sure the correct details are filled in when publishing, some parameters ar enot required but should not be deleted.

{{< table >}}
|Parameter|Required|Description|
|---------|--------|-----------|
|`title`|True| Title of the Article (will be rendered as the top level header) |
|`description`|True|Description of the Article (will be used when the article is searched)|
|`lead`|True|Should match the description of the Article|
|`date`|False|This should be auto-generated but is not used|
|`lastmod`|False|This is the last time the document was modified, this is not necessary as we can use Git Blame to track when something was changed more effectively|
|`draft`|True|When set to `true` the article will not be published on the site, by default this is set to `false` as drafting should be done locally before being merged|
|`images`|False|This is not needed as images should be in the same directory|
|`menu`|True|This is required to have the left-sidebar work correctly, you should mark the `Area` this article belongs to as a key and then the `Section` aginst the `parent` value like the example|
|`weight`|True|This is required to place the article in the correct order on the left-sidebar and also the navigation buttons on the bottom of the page it will affect the order acros the entire `Area`, not just the `Section`|
|`toc`|True|Standing for 'Table of Contents' this enables the Article to be listed in the left-sidebar, should be set to `true` by default|
{{< /table >}}

## Headings

When seperating Articles into Topics and Subsections it is preferred to use Headings as a delimiter instead of alternatives like Horizontal Rules.

Markdown does support different formats for defining Headers including underlining text with either `=` or `-`; as those formats only apply to `#Header 1` and `Header 2` respectively, for consistency across all Header sizes we have opted to use `#` instead.

The top level header ( `# Header 1`) is defined in the Article's metadata, so it is necessary to only use `## Header 2` or below.

It is also preferable to only use either `## Header 2` for Topics or `### Header 3` for Subsections of a Topic, while smaller sizes are permitted they do not render in the right-hand overview so should be used sparingly.

We observe the [Markdown Guide Best Practice](https://www.markdownguide.org/basic-syntax/#heading-best-practices) of leaving a space after the `#`.

We follow [Chicago Manual of Style](https://en.wikipedia.org/wiki/Title_case) Capitalization rules for Headings:

* Always capitalize the first and last words of titles and subtitles.
* Always capitalize "major" words (nouns, pronouns, verbs, adjectives, adverbs, and some conjunctions).
* Lowercase the conjunctions and, but, for, or, and nor.
* Lowercase the articles the, a, and an.
* Lowercase prepositions, regardless of length, except when they are stressed, are used adverbially or adjectivally, or are used as conjunctions.
* Lowercase the words to and as.
* Lowercase the second part of Latin species names.


```md
## Example Header 2
### Example Header 3
```

Follow this link for more information on using [Headings](../basic-markdown-formatting/#headings) in markdown.

## Body

Content is written in place and without any special tagging or formatting.

### Grammar

We do expect standard English Grammar, this includes full use of appropriate punctuation; however Emphasis using Exclamation Marks `!` should be minimized where possible.

It is relevant to note that the authors of this documentation are primarily native British English speakers, however, there is a conscious effort to align to certain standards observed in most other technical documentation including Americanized Spellings for consistency.

This includes:
* Use of the Oxford Comma
* Use of 'z' instead of 's' in words like 'Organization'
* Use of the '-or' suffix instead of '-our' in words like 'Color' and 'Humor' 

We expect any contributors to also match these standards.

### Sentences

One-liner Sentences are preferable to paragraphs where possible and should be seperated by newlines in a semi-bullet standard.

Sentences should preferably be between 1-2 clauses where possible, using 3 clauses is permitted but should be minimized.

One-Liner Sentences are useful when describing how to do something, including making simple instructions.

```md
This is a sentence.

This is another sentence, this one does use commas though.
```

### Paragraphs

Pargraphs consist of 2 or more sentences and are better suited to creating conceptual narratives.

In order to not overwhelm users they should be kept to a minimum and only used for expository reasons such as describing a specific concept or topic in more detail than a single sentence would permit.

```md
This is a paragraph which demonstrates the value of narratives 
in documentation. This is because certain concepts can only 
be related with more complex grammatical structures demonstrating 
not only the concept in mind, but other key related features; 
not to mention the greater range of expression.
```

### Quotes

Quotes should use single quote marks `'` instead of Speech Marks `"`.

'This is a Quote'

Single Quotes are permitted when referring to a colloquial or adopted term such as 'Code Fences' that is not a code reference but you may wish to highlight.

If a nested quote is being used then you may use `"`.

'Of course, he said "Let's write out an example".'

### Emphasis

Emphasis should be used minimally but can be effective to highlight key words and phrases inside of a sentence that need specific attention.

In most scenarios it is preferable to use a [callout](./#callouts-and-blockquotes) instead.

Use of Emphasis to highlight words differs to the usage of inline code references.

Emphasis should be used when it is important to note a specific adjective/adverb or a specific noun.

While it is permitted to emphasize an entire sentence this should only be done for stylistic purposes and emphasis should be kept to single words or small phrases.

When used in the context of an adjective/adverb use both Italics and Bold adding three asterisks `***` at either end of the highlighted text.

When used in the context of a noun use only Bold adding two asterisks `**` at either end of the highlighted text.

We do not permit use of underscored `_` emphasis, only asterisks`*` will be accepted.

For example:

```md
This action is available ***only*** to **Root Users**. 
```

This action is available ***only*** to **Root Users**.

Follow this link for more information on using [Emphasis](../basic-markdown-formatting/#emphasis) in markdown

### Linebreaks

Inserting manual linebreaks is not usually necessary to include as Markdown is very effective at rendering most scenarios.

However in a situation where the rendering is not working it is permitted to use standard linebreaks `<br>` in order to fix both formatting and style.

## Lists

We support both ordered and unordered lists in markdown.

Follow this link for details on implementing [Lists](../basic-markdown-formatting/#creating-lists) in markdown.

### Ordered Lists

Ordered lists should be written using the full numerical standard.

This means that while it is possible to list items only using one number and it will be rendered correctly we will only permit fully complete numbering to be submitted.

We also only permit using periods `.` as delimiters as this is a more standardized pattern than parentheses `)`.

```md
1. This is
2. an Ordered
3. List
```

1. This is
2. an Ordered
3. List

### Unordered Lists

Unordered Lists should be written using only asterisks `*` at the beginning of a line of text.

Other unordered list styles including `+` and `-` are available in markdown but are not permitted in these Docs.

```md
* This is
* an Unordered
* List
  * Unordered Lists
  * Can have sub-items
```

* This is
* an Unordered
* List
  * Unordered Lists
  * Can have sub-items

## Code and Codeblocks

There are many ways to use Inline Code and Codeblock references within the Jitsuin Docs.

### Inline Code

Inline code is specified using backticks `` ` ``, it is preferable to label any code, object attributes or other API references using inline code to highlight.

For example:

```md
note we have included the values `arc_display_name`, `arc_description` and `arc_home_location_identity`
```

note we have included the values `arc_display_name`, `arc_description` and `arc_home_location_identity`

### Standard Codeblocks

Standard codeblocks are represented using markdown with three backticks `` ``` `` as 'code fences'.

The Docs have built in syntax highlighting using `highlight.js` which allows us to add a language to each codeblock for proper rendering in the following format:

<pre><code>
```bash
```
</pre></code>

Here is an example of the full Syntax Highlighting:

```bash
#!/bin/bash

###### CONFIG
ACCEPTED_HOSTS="/root/.hag_accepted.conf"
BE_VERBOSE=false

if [ "$UID" -ne 0 ]
then
 echo "Superuser rights required"
 exit 2
fi

genApacheConf(){
 echo -e "# Host ${HOME_DIR}$1/$2 :"
}

echo '"quoted"' | tr -d \" > text.txt
```

There is a list of Languages available in the [Advanced Formatting Section](../advanced-formatting/).

It is required that each codeblock has a language associated with it, if in doubt a standard default to use is the markdown syntax (`md`).

It is preferable that Standard Codeblocks are used for representing shell commands and API Responses in documentation where there is typically little variance across platforms, and not scripting examples which should use Tabbed Codeblocks instead.

### Shell Commands

Commands should use Standard Codeblocks with the `bash` syntax highlight, we don't permit adding a leading command prompt such as `#` or `$`.

<pre><code>
```bash
echo "this is a command"
```
</code></pre>

```bash
echo "this is a command"
```

### Tabbed Codeblocks

Where possible when writing code examples you should use Tabbed Codeblocks to offer examples in multiple languages that other users may prefer.

This creates a much more accessible and useful documentation platform for any and all users.

Tabbed Codeblocks can be created using the following reference:

```go
{{</* tabs name="tab_with_code" >}}
{{< tab name="Bash" codelang="bash" >}}
echo "This is a Bash Example."
{{< /tab >}}
{{< tab name="Go" codelang="go" >}}
println "This is a Go Example."
{{< /tab >}}}
{{< /tabs */>}}
```

Tab content is always rendered as code and should be written without special formatting where possible to allow the syntax highlighting to work as intended.

Where possible the following languages should be offered as examples in this order:

* `JSON` - A raw JSON Example of the data being submitted
* `Bash` - Curl implementation of interacting with the endpoint
* `Python` - Python implementation of interacting with the endpoint
* `Go` -  Go implementation of interacting with the endpoint

Each set of tabs on a page needs a unique name to be permitted, the name should be a sane description of the example being shown.

The title of the tabs should match the language descriptions above, with the following example:

{{< tabs name="tab_with_code" >}}
{{< tab name="JSON" codelang="json" >}}
{
  "Example": "JSON"
}
{{< /tab >}}
{{< tab name="Bash" codelang="bash" >}}
echo "This is a Bash Example."
{{< /tab >}}
{{< tab name="Python" codelang="bash" >}}
print "This is a Python Example."
{{< /tab >}}
{{< tab name="Go" codelang="go" >}}
println "This is a Go Example."
{{< /tab >}}
{{< /tabs >}}

As Jitsuin RKVST is primarily an API there are different requirements for each type of example:

{{< tabs name="tabbed_api_requirements" >}}
{{< tab name="GET" codelang="md" >}}
Minimum:
* bash

Preferably:
* bash
* python
* go
{{< /tab >}}
{{< tab name="POST" codelang="md" >}}
Minimum:
* json
* bash

Preferably:
* json
* bash
* python
* go
{{< /tab >}}}
{{< tab name="PUT" codelang="md" >}}
Minimum:
* json
* bash

Preferably:
* json
* bash
* python
* go
{{< /tab >}}}
{{< tab name="PATCH" codelang="md" >}}
Minimum:
* json
* bash

Preferably:
* json
* bash
* python
* go
{{< /tab >}}}
{{< tab name="DELETE" codelang="md" >}}
Minimum:
* bash

Preferably:
* bash
* python
* go
{{< /tab >}}}
{{< tab name="SCRIPT" codelang="md" >}}
This refers to any kind of scripted example of multiple calls

Minimum:
* bash
or
* python

Preferably:
* bash
* python
* go
{{< /tab>}}
{{< /tabs >}}

One more usecase to consider is when a screenshotted example is used; this is discussed below in [Inserting Example Screenshots](./#inserting-example-screenshots)

### OpenAPI Docs

Rendering OpenAPI docs is done using another custom made shortcode:

```go
{{</* openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/access_policies.swagger.json" */>}}
```

When making an Article for API Docs the body should only contain the OpenAPI shortcode pointed at the URL of the OpenAPI spec to be rendered.

The title of the Rendered Article needs to be entered into the metadata manually and should match the title of the API as described in the OpenAPI spec being rendered.

For an example of how this renders please see [the example OpenAPI Render Page](../../playground/openapi-example-render) in the Playground.

## Callouts and Blockquotes

Adding Callouts and Blockquotes can be very useful to highlight interesting or specific information that users should be aware of.

Callouts come in three flavours; Note, Caution and Warning that use encapsulating shortcode depending on the case.

When writing a callout you should always start with the type of callout bolded, see below for examples.

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

### Blockquotes

While use of callouts is freely permitted, use of pure blockquotes is restricted to specific cases:

* A longer quote is emplyed
* A piece of text, neither or callout, needs to be differentiated from the main body

Blockquotes do not always read as well as other elements so should not be relied on extensively.

## Tables

Tables use markdown formatting to work, use of a markup table generator simplifies usage where possible, see the [Tables Section in the Advanced Formatting Guide](../advanced-formatting/#tables).

Tables should always use the `table` shortcode like so:

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

This ensures all tables are formatted correctly using the `table-striped` and `table-bordered` property.

Tables without those properties are not permitted.

## Links

Links to other sections of documentation or external resources should use the standard markdown notation:

```md
[This is a link](https://info.jitsuin.com/demo-request)
```

Other forms of links such as using `<a>` tags will not be permitted.

### Section References

To reference another part of the docs you should always as be as specific as possible, for example:

```md
[The links formatting guide](../advanced-formatting/#links)
```

In this example `../` implies the content is in another article, `advanced-formatting` is the sluggified name of the article, `#` can then be used to specify the sluggified name of the topic in that article (in this case `#links`).

To refer to a topic in the same article use `./#your-section` instead of `

To refer to another section it is necessary to use `../../` instead and then follow on from there.

While it is permitted to only specify the article name and not include a `#` reference to the topic, ideally you should be as specific as possible where appropriate.

### External Links

External Links are not generally permitted as Jitsuin has little to no control on the content being presented and if it is change dor moved in future.

If you would like to include an external link then it will be decided on a case by case basis.

## Images

Images should be used sparingly and we encourage users to not commit images to the main repository unless necessary (e.g. static images such as logos).

If an image does need to be added it should be included in the folder of the Article.

All images should be `.png` files.

### Standard Images

Standard images can be included using the `image` shortcode.

{{</* img src="AssetCreationDetails.png" alt="Rectangle" caption="<em>Asset Creation Example</em>" class="border-0" */>}}

{{< img src="AssetCreationDetails.png" alt="Rectangle" caption="<em>Asset Creation Example</em>" class="border-0" >}}

Images should appear readable and legible across both Light Mode and Dark Mode, if it does not then you need to use the `imgDark` shortcode as described in the [next topic](./#light-mode-and-dark-mode-images).

All images should use the `Rectangular` alt value, `border-0` class and captions should use the `<em>` tags to encapsulate text.

### Light Mode and Dark Mode Images

When a particular image does not suit either the Dark or Light Theme it will be necessary to specify two images, one for light and one for dark, instead.

You can do this using the special `imgDark` shortcode.

{{< imgDark src="Jitsuin_Logo_RGB.png" srcDrk="Jitsuin_WhtType_RGB.png" alt="Rectangle" caption="<em>Jitsuin Dark Mode Logo Example</em>" class="border-0" >}}

All images should use the `Rectangular` alt value, `border-0` class and captions should use the `<em>` tags to encapsulate text.

### Inserting Example Screenshots

Screenshots in Jitsuin are generated using the Robot Framework and are generated automatically so that they can be maintained and kept up to date with as little human involvement as possible.

Any screenshots that accompany steps in a process to follow should be generated using Robot, you should also accompany steps like this with example code using the [Tabbed Codeblocks](./#tabbed-codeblocks).

The name of the tab if sharing screen shots should be 'UI'.

To specify an image in a Tabbed Codeblock you need to remove the `codelang` value, take the following example:

{{< tabs name="tab_with_image_example" >}}
{{< tab name="UI" codelang="" >}}
{{< img src="AssetCreationDetails.png" alt="Rectangle" caption="<em>Asset Creation Example</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" codelang="json" >}}
{
    "behaviours": ["Firmware", "Maintenance", "RecordEvidence", "LocationUpdate", "Attachments"],
    "attributes": {
        "arc_firmware_version": "",
        "arc_serial_number": "",
        "arc_display_name": "",
        "arc_description": "",
        "arc_home_location_identity": "",
        "arc_display_type": "",
        "some_custom_attribute": "",
        "arc_attachments": [
            {
                "arc_display_name": "",
                "arc_attachment_identity": "",
                "arc_hash_alg": "",
                "arc_hash_value": ""
            }
        ]
    }
}
{{< /tab >}}
{{< tab name="Bash" codelang="bash" >}}
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v2/assets
{{< /tab >}}
{{< /tabs >}}

