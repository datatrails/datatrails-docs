---
title: "Attachments API"
description: "Attachments API Reference"
lead: "Attachments API Reference"
date: 2021-06-09T12:05:02+01:00
lastmod: 2021-06-09T12:05:02+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 102
toc: true
---

## Attachment API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

### Retrieve a Specific Attachment on an Asset

```bash
curl -v \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v2/attachments/assets/c04d5ecf-02e0-4be2-a014-ffbbf0e8ddeb/08838336-c357-460d-902a-3aba9528dd22
```

### Retrieve a Specific Attachment on an Event 

```bash
curl -v \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v2/attachments/assets/c04d5ecf-02e0-4be2-a014-ffbbf0e8ddeb/events/de834094-f6c3-4e38-9b37-8c61dea312c9/08838336-c357-460d-902a-3aba9528dd22
```

### Retrieve Information about a specific Attachment

It’s also possible to retrieve information about specific attachment using this API. 

To do that simply issue request as above with a suffix `/info`

```bash
curl -v \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v2/attachments/assets/c04d5ecf-02e0-4be2-a014-ffbbf0e8ddeb/08838336-c357-460d-902a-3aba9528dd22/info
```

The response will include basic information about the attachment:

```json
{
    "identity": "attachments/08838336-c357-460d-902a-3aba9528dd22",
    "hash": {
        "alg": "SHA256",
        "value": "xxxxxxxxxxxxxxxxxxxxxxx"
    },
    "mime_type": "image/jpeg",
    "timestamp_accepted": "2019-11-07T15:31:49Z",
    "size": 31424
}
```

## Attachment OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/attachmentsv1.swagger.json" >}}

