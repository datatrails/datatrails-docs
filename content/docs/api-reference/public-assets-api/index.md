---
title: "Public Assets API"
description: "Public Assets API Reference"
lead: "Public Assets API Reference"
date: 2021-06-09T11:56:23+01:00
lastmod: 2021-06-09T11:56:23+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 112
toc: true
---

Public Assets are created using the [Assets API](../assets-api/) and setting the value of `public` to `true`.

To see more information about creating a Public Asset see [Creating a Public Asset](../assets-api/#creating-a-public-asset).

Each Public Asset has a Private and a Public Interface, the Private Interface is used to update the asset by the creating tenancy, the Public is a read-only view of the Asset that you do not need to be authenticated for. 

The methods described below cover interacting with the Public Interface Only, to interact with the Private Interface, use the standard [Assets API](../assets-api/). 

## Public Assets API Examples

### Fetch a Public Asset Record

### Fetch all of a Public Asset's Events Records

### Fetch a Public Asset's specific Event Record

## Public Assets OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/publicassetsv2.swagger.json" >}}
