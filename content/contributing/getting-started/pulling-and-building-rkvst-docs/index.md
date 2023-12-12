---
title: "Pulling and Building DataTrails Docs"
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
sitemap_exclude: true
robotsdisallow: true
---
{{< note >}}
DataTrails Docs depend on npm version 14.
{{< /note >}}

1. If you do not have npm installed please use the following guide
    {{< tabs name="tab_with_code" >}}  {{{<tab name="Ubuntu" codelang="bash">}}apt install npm{{< /tab >}}
    {{<tab name="Cent OS/RHEL" codelang="bash">}}yum install npm{{< /tab >}}}
    {{< tab name="MacOS" codelang="bash" >}}brew install npm{{< /tab >}}  {{< /tabs >}}
1. To begin pull the latest DataTrails docs from Github

    ```bash
    git clone git@github.com:datatrails/datatrails-docs.git
    ```

1. Move into the directory

    ```bash
    cd datatrails-docs
    ```

1. Assure the npm version is at least 14

   ```bash
   npm version
   ```

   Look for `node: '14.21.3'` or greater
1. Either install npm version 14 or greater, or use a npm virtual environment such as [nvm](https://github.com/nvm-sh/nvm)

   ```bash
   nvm use 14
   ```

1. Resolve npm dependencies and build the site

    ```bash
    npm ci
    npm run build
    ```  

1. To run a local DataTrails Docs Server it is advisable to use the `datatrails-doks` wrapper

    ```bash
    ./datatrails-doks start
    ```

    This will build a local version of the server that can be accessed at [http://localhost:1313](http://localhost:1313).
    You can keep this running in the background while making any edits and the developer server should automatically pick up your changes for you.
{{< note >}}
**Note:** The development server logs to stdout by default, you will need to keep the Terminal Session open while in use.
{{< /note>}}
1. To stop the Doks Server use `ctrl+c` in the Terminal Session you started it in
