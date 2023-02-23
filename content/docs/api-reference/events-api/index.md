---
title: "Events API"
description: "Events API Reference"
lead: "Events API Reference"
date: 2021-06-09T11:48:40+01:00
lastmod: 2021-06-09T11:48:40+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 107
toc: true
---

{{< note >}}
For more information on creating an Event against an Asset, visit our [RKVST Basics guide](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/).
{{< /note >}}

## Events API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.
### Event Creation

Define the Event parameters and store in `/path/to/jsonfile`:

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "Safety Conformance",
    "Safety Rating": "90",
    "inspector": "spacetime"
  },
  "timestamp_declared": "2019-11-27T14:44:19Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  }
}
```

{{< note >}}
**Note:** `RecordEvidence` is the primary, default behaviour for creating Events.
{{< /note >}}

Add the request to the Asset record by POSTing it to the resource:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets/add30235-1424-4fda-840a-d5ef82c4c96f/events
```

The response is:

```json
{
  "identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b37-e0b8-42e0-8dcf-dc8c4aefc000",
  "asset_identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f",
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "Safety Conformance",
    "Safety Rating": "90",
    "inspector": "spacetime"
  },
  "timestamp_accepted": "2019-11-27T15:13:21Z",
  "timestamp_declared": "2019-11-27T14:44:19Z",
  "timestamp_committed": "2019-11-27T15:15:02Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  },
  "principal_accepted": {
    "issuer": "job.idp.server/1234",
    "subject": "bob@job"
  },
  "confirmation_status": "CONFIRMED",
  "block_number": 12,
  "transaction_index": 5,
  "transaction_id": "0x07569"
}
```
### Adding Attachments

The following assumes that an attachment has been uploaded to RKVST using the [Blob API](../blobs-api). 

This attachment uuid is generically referred to as:

```bash
blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
Each attachment has an associated hash value and the name of the hash algorithm used that you can also get from the Blob API response.

Once you've uploaded your file, you can use the `"arc_attribute_type": "arc_attachment"` key-value pair within a dictionary of blob information to add the attachment to either your Asset or Event.

The following example shows you usage with both the `event_attributes` and the `asset_attributes`:

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "Safety Conformance",
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report",
    },
  },
  "asset_attributes": {
    "latest_conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Latest Conformance Report",
    },
  },
  "timestamp_declared": "2019-11-27T14:44:19Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  },
}
```
Add the request to the Asset Record by POSTing it to the resource:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets/add30235-1424-4fda-840a-d5ef82c4c96f/events
```

You should see the response:

```json
{
  "identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/11bf5b37-e0b8-42e0-8dcf-dc8c4aefc000",
  "asset_identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f",
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "Safety Conformance",
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report",
    },
  },
  "asset_attributes": {
    "latest_conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Latest Conformance Report",
    },
  },
  "timestamp_accepted": "2019-11-27T15:13:21Z",
  "timestamp_declared": "2019-11-27T14:44:19Z",
  "timestamp_committed": "2019-11-27T15:15:02Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  },
  "principal_accepted": {
    "issuer": "job.idp.server/1234",
    "subject": "bob@job"
  },
  "confirmation_status": "CONFIRMED",
  "block_number": 12,
  "transaction_index": 5,
  "transaction_id": "0x07569"
}
```
## Events OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/master/doc/openapi/b-recordevidencev2.swagger.json" >}}