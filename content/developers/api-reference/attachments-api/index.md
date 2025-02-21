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
The Attachments API enables attaching and querying Binary Large OBjects (BLOBs) such as documents, process artifacts and images to Assets and Events.

{{< note >}}
Attachments apply to [Asset-Events](/developers/api-reference/asset-events-api/), and Asset-free [Events](/developers/api-reference/events-api/) (preview).
There are subtle differences that are documented below.
{{< /note >}}

The steps to make an attachment include:

1. Uploading content to the DataTrails [Blobs API](/developers/api-reference/blobs-api/).
1. Attaching the blob to an [Asset](/developers/api-reference/assets-api/) or an [Event](/developers/api-reference/events-api/)
1. Querying the Attachment, through an Asset or an Event

### Asset-Event Attachments

Assets support attachments by creating an [Asset-Event](/developers/api-reference/asset-events-api/) with nested `arc_` [reserved attributes](/glossary/reserved-attributes/).

- `"arc_attribute_type": "arc_attachment"`
- `"arc_blob_identity": "blobs/b1234567-890b"`
- `"arc_blob_hash_alg": "SHA256"`
- `"arc_blob_hash_value": "h1234567h"`
- `"arc_file_name": "conformance.pdf"`
- `"arc_display_name": "Conformance Report"`

An example of an Asset-event with two attachments:

```json
  {
    "identity": "assets/a1234567-890a/events/e1234567-890e",
    "asset_identity": "assets/a1234567-890a",
    "event_attributes": {
      "arc_description": "Conformance approved for version 1.6",
      "arc_display_type": "Conformance Report",
      "conformance_report": {
        "arc_attribute_type": "arc_attachment",
        "arc_blob_identity": "blobs/b1234567-890b",
        "arc_blob_hash_alg": "SHA256",
        "arc_blob_hash_value": "h1234567h",
        "arc_file_name": "conformance.pdf",
        "arc_display_name": "Conformance Report"
      },
      "security_report": {
        "arc_attribute_type": "arc_attachment",
        "arc_blob_identity": "blobs/b890123-456b",
        "arc_blob_hash_alg": "SHA256",
        "arc_blob_hash_value": "h8901234h",
        "arc_file_name": "security-report.pdf",
        "arc_display_name": "Security Report"
      }
    },
    "..."
  }
```

In the above example, the name of the parent attribute (`"conformance_report"`) can be any value, providing a means to name multiple attachments within a single event, such as the additional `"security_report"` attachment.

The DataTrails platform evaluates `"arc_attribute_type": "arc_attachment"` to reference a DataTrails [Blob](/developers/api-reference/blobs-api/) based attachment.

## Create an Asset-Event Based Attachment

- [Create a bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.
- [Create an Asset](/developers/api-reference/assets-api/) to associate the attachment.
- Upload the content of an Attachment using the [Blobs API](/developers/api-reference/blobs-api/).

### Asset-Event Attachment Variables

- To associate an existing Blob, set the `ASSET_ID`, `BLOB_ID`, `BLOB_HASH` value and `BLOB_FILE` from the [Blobs API](/developers/api-reference/blobs-api/):

  {{< note >}}
  The `BLOB_HASH` is required, as it creates integrity protection between the content uploaded through the Blobs API, and the integrity protected reference of the Attachment.
  Storing the hash in the attachment assures any tampering of the blob storage, including tampering within the DataTrails platform, would be evident.
  
  When retrieving the blob, the hash retrieved should be compared to the hash of the Attachment API to assure the content has not been tampered with.
  {{< /note >}}

  ```bash
  ASSET_ID=<asset-id>
  BLOB_ID=<blob-id>
  BLOB_HASH=<hash-value>
  BLOB_FILE=conformance.pdf
  ```

  Example:

  ASSET_ID=assets/a1234567-890a  
  BLOB_ID=blobs/b1234567-890b  
  BLOB_HASH=h1234567h  
  BLOB_FILE=cat.jpg

### Create an Asset-Event Attachment

- Create an event, referencing the Blob as an integrity protected Attachment:

  ```bash
  cat > /tmp/event.json <<EOF
  {
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "event_attributes": {
      "arc_display_type": "Cat-ID",
      "arc_description": "Fydor, the cat on the scene",
      "cat-id": {
        "arc_attribute_type": "arc_attachment",
        "arc_blob_hash_value": "$BLOB_HASH",
        "arc_blob_identity": "$BLOB_ID",
        "arc_blob_hash_alg": "SHA256",
        "arc_file_name": "$BLOB_FILE",
        "arc_display_name": "Fydor"
      }
    }
  }
  EOF
  ```

- Post to the Asset resource:

  ```bash
  curl -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/tmp/event.json" \
    https://app.datatrails.ai/archivist/v2/$ASSET_ID/events \
    | jq
  ```

  The response:

  ```json
  {
    "identity": "assets/a1234567-890a/events/e1234567-890e",
    "asset_identity": "assets/a1234567-890a",
    "event_attributes": {
      "arc_description": "Safety conformance approved for version 1.6.",
      "cat-id": {
        "arc_attribute_type": "arc_attachment",
        "arc_blob_hash_value": "h1234567h",
        "arc_blob_identity": "blobs/b1234567-890b",
        "arc_blob_hash_alg": "SHA256",
        "arc_file_name": "cat.jpg",
        "arc_display_name": "Fydor"
      },
      "arc_display_type": "Cat-ID"
    },
    "..."
  }
  ```

### Retrieve an Asset-Event Attachment

- When creating an attachment, an Asset-Event is created.
  In addition to the Asset_ID captured above, capture the Event_ID

  ```bash
  EVENT_ID=events/e1234567-890e
  ```

- The `attachments/assets` Resource does not support `/blobs/` as part of the resource identifier.
  The `ATTACHMENT_ID` variable will parse the ID from the `$BLOB_ID`

  ```bash
  ATTACHMENT_ID=$(echo ${BLOB_ID} | cut -d '/' -f 2)

  curl -H "@$HOME/.datatrails/bearer-token.txt" \
      --output $BLOB_FILE \
      https://app.datatrails.ai/archivist/v2/attachments/$ASSET_ID/$EVENT_ID/$ATTACHMENT_ID
  ```

### Retrieve Metadata About an Asset-Event Attachment

Metadata information includes the `scanned_status` of the attachment.
Attachment scanning happens daily batches.

- Issue a request as above with the suffix `/info`.

  ```bash
  curl -H "@$HOME/.datatrails/bearer-token.txt" \
      https://app.datatrails.ai/archivist/v2/attachments/$ASSET_ID/$EVENT_ID/$ATTACHMENT_ID/info \
      | jq
  ```

The response will include basic information about the attachment:

```json
{
  "hash": {
    "alg": "SHA256",
    "value": "xxxxxxxx"  },
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

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/attachmentsv2.swagger.json" >}}
{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/publicattachmentsv2.swagger.json" >}}
