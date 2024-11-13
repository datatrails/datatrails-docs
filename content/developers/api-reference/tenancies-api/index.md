---
title: "Tenancies API"
description: "Tenancies API Reference"
lead: "Tenancies API Reference"
date: 2021-06-09T13:29:57+01:00
lastmod: 2021-06-09T13:29:57+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 114
toc: true
aliases: 
  - /docs/api-reference/tenancies-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

## Tenancies API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Retrieve the Current List of Administrators

To fetch the list of Administrators, simply `GET` the `tenancies/root_principals` resource:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v1/tenancies/root_principals
```

### Update the List of Administrators

Define the update parameters and store in `/path/to/jsonfile`:

```json
{
   "administrators": [
       {
           "issuer": "https://login.microsoftonline.com/5c129635-5858-4fe3-9bef-444f6c7ee1cf/v2.0",
           "subject": "58589bef-4fe3-9a3b-23df-8527bc45e1cf",
           "display_name": "Jane Smith",
           "email":  "jane.smith@synsation.org"
       },
       {
           "issuer": "https://login.microsoftonline.com/5c129635-5858-4fe3-9bef-444f6c7ee1cf/v2.0",
           "subject": "27bc5b4f-9a3b-4fe3-23df-e1c7bc45e1cf",
           "display_name": "Nate Rogers",
           "email":  "nate.rogers@synsation.org"
       }
    ]
}
```

Update the Administrators by PATCHing the `tenancies/root_principals` resource:

```bash
curl -v -X PATCH \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v1/tenancies/root_principals
```

## Tenancies OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/tenanciesv1.swagger.json" >}}<br>
