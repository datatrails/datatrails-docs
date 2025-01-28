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

The Attachments API enables attaching and querying Binary Large OBjects (BLOBs) such as documents, process artifacts and images to Assets and Events.
Events can also have a primary image associated with the event, providing feedback within the DataTrails application.

The steps include:

1. Uploading content to the DataTrails [Blobs API](/developers/api-reference/blobs-api/).
1. Attaching the blob to an [Asset](/developers/api-reference/assets-api/) or an [Event](/developers/api-reference/events-api/)
1. Querying the Attachment, through an Asset or an Event

## Attachment API Examples

- Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

- Upload the content of the Attachment using the [Blobs API](/developers/api-reference/blobs-api/).

### Event Attachments

- To associate an existing Blob, set the `Asset_ID`, `BLOB_HASH` value and `BLOB_FILE`:

  {{< note >}}
  NOTE: The `ASSET_ID` dependency will be removed with Non-asset based Events
  {{< /note >}}

  ```bash
  ASSET_ID=<asset-id>
  BLOB_ID=<blob-id>
  BLOB_FILE=file.jpg
  BLOB_HASH=<hash-value>
  ```

### Asset Attachments

Set the `"arc_attribute_type": "arc_attachment"` key-value pair within a dictionary of blob information to add the attachment to the Event.
The name of the attribute (`"conformance_report"` in the following example), can be any value.
The DataTrails platform evaluates `arc_attribute_type` within the attribute properties to understand it references a DataTrails Blob based attachment.

- Create the event payload, referencing the Blob as an integrity protected Attachment:

  ```bash
  cat > /tmp/event.json <<EOF
  {
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "event_attributes": {
      "arc_display_type": "Safety Conformance",
      "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
      "arc_evidence": "DVA Conformance Report attached",
      "conformance_report": {
        "arc_attribute_type": "arc_attachment",
        "arc_blob_hash_value": "$BLOB_HASH",
        "arc_blob_identity": "blobs/$BLOB_ID",
        "arc_blob_hash_alg": "SHA256",
        "arc_file_name": "$BLOB_FILE",
        "arc_display_name": "Conformance Report"
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
    https://app.datatrails.ai/archivist/v2/assets/$ASSET_ID/events \
    | jq
  ```

  The response:

  ```json
  {
    "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/4eaa5fe6-a88f-4228-89c5-bdc3f4351066",
    "asset_identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "event_attributes": {
      "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
      "arc_evidence": "DVA Conformance Report attached",
      "arc_display_type": "Safety Conformance",
      "conformance_report": {
        "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "arc_blob_hash_alg": "SHA256",
        "arc_file_name": "file.jpg",
        "arc_display_name": "Conformance Report",
        "arc_attribute_type": "arc_attachment",
        "arc_blob_hash_value": "xxxxxxxxx"
      }
    },
    "asset_attributes": {},
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "timestamp_declared": "2025-01-28T01:50:14Z",
    "timestamp_accepted": "2025-01-28T01:50:14Z",
    "timestamp_committed": "2025-01-28T01:50:16Z",
    "principal_declared": {
      "issuer": "https://app.datatrails.ai/appidpv1",
      "subject": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "display_name": "my-integration",
      "email": ""
    },
    "principal_accepted": {
      "issuer": "https://app.datatrails.ai/appidpv1",
      "subject": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "display_name": "my-integration",
      "email": ""
    },
    "confirmation_status": "PENDING",
    "transaction_id": "",
    "block_number": 0,
    "transaction_index": 0,
    "from": "",
    "tenant_identity": "",
    "merklelog_entry": {
      "commit": null,
      "confirm": null,
      "unequivocal": null
    }
  }
  ```

### Event Primary Image

Events can use the same Blobs API to associate a primary image in the DataTrails Application.
The same, or different blobs can be an attribute attachment and/or the primary image.

- Associate a Blob as the Event Primary Image:

  ```json
  cat > /tmp/event.json <<EOF
  {
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "event_attributes": {
      "arc_primary_image": {
        "arc_attribute_type": "arc_attachment",
        "arc_blob_hash_value": "$BLOB_HASH",
        "arc_blob_identity": "blobs/$BLOB_ID",
        "arc_blob_hash_alg": "SHA256",
        "arc_file_name": "$BLOB_FILE",
        "arc_display_name": "arc_primary_image"
      }
    }
  }
  EOF
  ```

- POST the Event Primary Image:

  ```bash
  curl -X POST \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      -H "Content-type: application/json" \
      -d "@/tmp/event.json" \
      https://app.datatrails.ai/archivist/v2/assets/$ASSET_ID/events \
      | jq
  ```

### Retrieve a Specific Attachment on an Asset

```bash
curl -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/attachments/assets/$ASSET_ID/$ATTACHMENT_ID
```

### Retrieve a Specific Attachment on an Event

```bash
ASSET_ID=<asset-id>
curl -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/attachments/assets/$ASSET_ID/events/$EVENT_ID/$ATTACHMENT_ID
```

### Retrieve Information About a Specific Attachment

It’s also possible to retrieve information about specific attachment using the Attachments API.

This information includes the `scanned_status` of the attachment.
Attachment scanning happens in batch, daily.

To do so, simply issue a request as above with the suffix `/info`.

```bash
curl -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/attachments/assets/$ASSET_ID/$ATTACHMENT_ID/info
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

### Integrity Protecting External Content

To integrity protect content located external to the DataTrails platform, exclude the `"arc_attribute_type": "arc_attachment"`, `"arc_blob_identity"` and `"arc_display_name"` as not being relevant to external content.

  ```json
  cat > /tmp/event.json <<EOF
  {
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "event_attributes": {
      "arc_blob_hash_value": "$BLOB_HASH",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "$BLOB_FILE"
    }
  }
  EOF
  ```

- Post to the Integrity protected content as an Event:

  ```bash
  curl -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/tmp/event.json" \
    https://app.datatrails.ai/archivist/v2/assets/$ASSET_ID/events \
    | jq
  ```

- Capture the new Event ID from above:

  ```bash
  EVENT_ID=<event-id>
  ```

- Query the newly created Event, with integrity protection:

  ```bash
  curl -H "@$HOME/.datatrails/bearer-token.txt" \
      https://app.datatrails.ai/archivist/v2/assets/$ASSET_ID/events/$EVENT_ID \
      | jq
  ```

## Attachment OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/attachmentsv2.swagger.json" >}}
{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/publicattachmentsv2.swagger.json" >}}
