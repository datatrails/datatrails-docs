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
weight: 107
toc: true
aliases: 
  - /docs/api-reference/attachments-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance.
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.io) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

The Attachments API enables you to attach and query Binary Large OBjects (BLOBs) such as documents, process artifacts and images that are attached to your evidence ledger.

The steps include:

1. Uploading content to the DataTrails [Blobs API](/developers/api-reference/blobs-api/).
1. Attaching the blob to an Asset or an Event
1. Querying the attachment, through an Asset or an Event

## Attachment API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Create a Blob

To create an attachment, upload the content using the [Blobs API](/developers/api-reference/blobs-api/).

### Event Attachments

Associate a Blob as an Attachment to an Event.

...

### Asset Attachments

...

```bash
ASSET_ID=<asset-id>
ATTACHMENT_ID=<attachment-id>
EVENT_ID=<event-id>
```

### Retrieve a Specific Attachment on an Asset

```bash
curl -v \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/attachments/assets/$ASSET_ID/$ATTACHMENT_ID
```

### Retrieve a Specific Attachment on an Event

```bash
ASSET_ID=<asset-id>
curl -v \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/attachments/assets/$ASSET_ID/events/$EVENT_ID/$ATTACHMENT_ID
```

### Retrieve Information About a Specific Attachment

It’s also possible to retrieve information about specific attachment using this API.

This information includes the `scanned_status` of the attachment. Attachment scanning happens each day.

To do so, simply issue a request as above with the suffix `/info`.

```bash
curl -v \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/attachments/assets/$ASSET_ID/$ATTACHMENT_ID/info
```

The response will include basic information about the attachment:

```json
{
  "hash": {
    "alg": "SHA256",
    "value": "75debbfc7a4d988f2321dfb158fe65c62dabe50d4d7b6efb961e83be43a8aa77"  },
  "identity": "attachments/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "issuer": "local",
  "mime_type": "image/jpeg",
  "size": 81254,
  "subject": "user@datatrails.ai",
  "tenantid": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "timestamp_accepted": "2023-02-06T16:04:31Z",
  "scanned_status": "NOT_SCANNED",
  "scanned_bad_reason": "",
  "scanned_timestamp": ""
}
```

## Attachment OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/attachmentsv2.swagger.json" >}}
{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/publicattachmentsv2.swagger.json" >}}
