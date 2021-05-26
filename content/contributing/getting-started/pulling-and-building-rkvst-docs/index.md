---
title: "Pulling and Building RKVST Docs"
description: ""
date: 2021-05-20T12:03:27+01:00
lastmod: 2021-05-20T12:03:27+01:00
draft: false
menu:
  contributing:
    parent: "getting-started"
weight: 1
images: []
toc: true
---

1. To begin pull the latest RKVST docs from Github.

```bash
git clone <the final resting place>
```

2. Move into the directory.

```bash
cd rkvst-doks
```

3. Install the DOKS Dependencies.

```bash
npm install
```

Note: If you do not have npm installed please use the following guide:

{{< tabs name="tab_with_code" >}}
{{{< tab name="Ubuntu" codelang="bash" >}} 
apt install npm
{{< /tab >}}
{{< tab name="Cent OS/RHEL" codelang="bash" >}}
yum install npm 
{{< /tab >}}}
{{< tab name="MacOS" codelang="bash" >}}
brew install npm 
{{< /tab >}}
{{< /tabs >}}
<br>
4. To run a local RKVST Docs Server it is advisable to use the `jitsuin-doks` wrapper

```bash
jistuin-doks start
```

This will build a local version of the server that can be accessed at [http://localhost:1313](https://localhost:1313).

You can keep this running in the background while making any edits and the developer server should automatically pick up your changes for you.

{{< note >}}
**Note:** The development server logs to stdout by default, you will need to keep the Terminal Session open while in use.
{{< /note>}}

5. To stop the Doks Server use `ctrl+c` in the Terminal Session you started it in.









