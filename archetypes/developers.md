---
title: "{{ replace .Name "-" " " | title }}"
description: ""
lead: ""
date: {{ .Date }}
lastmod: {{ .Date }}
draft: false
images: []
menu: 
  developers:
    parent: ""
weight: 999
toc: true
---

{{< img src="{{ .Name | urlize }}.jpg" alt="{{ replace .Name "-" " " | title }}" caption="{{ replace .Name "-" " " | title }}" >}}
