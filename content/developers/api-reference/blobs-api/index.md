---
title: "Blobs API"
description: "Blobs API Reference"
lead: "Blobs API Reference"
date: 2021-06-09T13:32:57+01:00
lastmod: 2021-06-09T13:32:57+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 104
toc: true
aliases: 
  - /docs/api-reference/blobs-api/
---
{{< note >}}
This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-official/workspace/datatrails-public-official/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## Blob API Examples

The Blobs API enables you to upload Binary Large OBjects (BLOBs) such as documents, process artifacts and images to attach to your evidence ledger.

{{< note >}}
**Note:** Blobs cannot be searched or listed as a collection in their own right: they must always be associated with an Asset or Event through an Attachment Attribute and can only be downloaded by users with appropriate access rights to that Attachment. For information on Attachments and how to implement them, please refer to [the Events API Reference](../events-api/#adding-attachments).
{{< /note >}}

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Upload a Blob

Upload the blob stored at /path/to/file:

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "content_type=image/jpg" \
    -F "file=@/path/to/file" \
    https://app.datatrails.ai/archivist/v1/blobs
```

The response is:

```json
{
  "hash": {
    "alg": "SHA256",
    "value": "xxxxxxxxxxxxxxxxxxxxxxx"  },
  "identity": "blobs/<blob-id>",
  "issuer": "local",
  "mime_type": "image/jpeg",
  "size": 81254,
  "subject": "user@datatrails.com",
  "tenantid": "tenant/<tenant-id>",
  "timestamp_accepted": "2023-02-06T16:04:31Z",
  "scanned_status": "NOT_SCANNED",
  "scanned_bad_reason": "",
  "scanned_timestamp": ""
}
```

### Retrieve a Blob

Retrieve a specific Blob:

```bash
curl -v \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "content_type=image/jpg" \
    --output "/path/to/file" \
    https://app.datatrails.ai/archivist/v1/blobs/08838336-c357-460d-902a-3aba9528dd22
```

The response is:

```json
{
  "hash": {
    "alg": "SHA256",
    "value": "xxxxxxxxxxxxxxxxxxxxxxx"  },
  "identity": "blobs/<blob-id>",
  "issuer": "local",
  "mime_type": "image/jpeg",
  "size": 81254,
  "subject": "user@datatrails.com",
  "tenantid": "tenant/<tenant-id>",
  "timestamp_accepted": "2023-02-06T16:04:31Z",
  "scanned_status": "NOT_SCANNED",
  "scanned_bad_reason": "",
  "scanned_timestamp": ""
}
```

## Blobs OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/archivist-docs-old/master/doc/openapi/blobsv1.swagger.json" >}}
