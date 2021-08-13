---
title: "Tenancies API"
description: "Tenancies API Reference"
lead: "Tenancies API Reference"
date: 2021-06-09T13:29:57+01:00
lastmod: 2021-06-09T13:29:57+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 112
toc: true
---

## Tenancies API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Set the URL (for example):

```bash
export URL=https://app.rkvst.io 
```

### Retrieve the Current List of Root Principals

To fetch the list of root principals, simply `GET` the `tenancies/root_principals` resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v1/tenancies/root_principals
```

### Update the List of Root Principals

Define the update parameters and store in `/path/to/jsonfile`:

```json
{
   "root_principals": [
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
    }
}
```

Update the root principals by PATCHing the `tenancies/root_principals` resource:

```bash
curl -v -X PATCH \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v1/tenancies/root_principals
```

## Tenancies OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/tenancies.swagger.json" >}}
