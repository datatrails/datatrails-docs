---
title: "Attachments API"
description: "Attachments API Reference"
lead: "Attachments API Reference"
date: 2021-06-09T12:05:02+01:00
lastmod: 2021-06-09T12:05:02+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 103
toc: true
---

## Attachment API Examples

The Attachments API enables you to query Binary Large OBjects (BLOBs) such as documents, process artifacts and images that are attached to your evidence ledger. For details of how to actually attach these BLOBs to Events and Assets, see the [the Events API Reference](../events-api/#adding-attachments).

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

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

### Retrieve Information About a Specific Attachment

It’s also possible to retrieve information about specific attachment using this API. 

This information includes the `scanned_status` of the attachment. Attachment scanning happens each day.

To do so, simply issue a request as above with the suffix `/info`.

```bash
curl -v \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v2/attachments/assets/c04d5ecf-02e0-4be2-a014-ffbbf0e8ddeb/08838336-c357-460d-902a-3aba9528dd22/info
```

The response will include basic information about the attachment:

```json
{
  "hash": {
    "alg": "SHA256",
    "value": "75debbfc7a4d988f2321dfb158fe65c62dabe50d4d7b6efb961e83be43a8aa77"  },
  "identity": "attachments/08838336-c357-460d-902a-3aba9528dd22",
  "issuer": "local",
  "mime_type": "image/jpeg",
  "size": 81254,
  "subject": "user@rkvst.com",
  "tenantid": "tenant/<tenant-id>",
  "timestamp_accepted": "2023-02-06T16:04:31Z",
  "scanned_status": "NOT_SCANNED",
  "scanned_bad_reason": "",
  "scanned_timestamp": ""
}
```

## Attachment OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/master/doc/openapi/attachmentsv2.swagger.json" >}}

