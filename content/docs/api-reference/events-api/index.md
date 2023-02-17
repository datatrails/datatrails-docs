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

Once you've uploaded your file you can use the `arc_attachments` attribute to add the attachment to either you Asset or Event.

The following example shows you usage with both the `event_attributes` and the `asset_attributes`:

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "Safety Conformance",
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "arc_attachments": [
      {
        "arc_display_name": "Conformance Report",
        "arc_attachment_identity": "blobs/e2a1d16c-03cd-45a1-8cd0-690831df1273",
        "arc_hash_value": "8a1eef8ab0ad431b7e2a900fc15ad8216f010fd8e4bf739604cec39fb1f94049",
        "arc_hash_alg": "SHA-256"
      }]
  },
  "asset_attributes": {
    "arc_attachments": [
      {
        "arc_display_name": "Latest Conformance Report",
        "arc_attachment_identity": "blobs/e2a1d16c-03cd-45a1-8cd0-690831df1273",
        "arc_hash_value": "8a1eef8ab0ad431b7e2a900fc15ad8216f010fd8e4bf739604cec39fb1f94049",
        "arc_hash_alg": "SHA-256"
      }]
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
    "arc_attachments": [
      {
        "arc_display_name": "Conformance Report",
        "arc_attachment_identity": "blobs/e2a1d16c-03cd-45a1-8cd0-690831df1273",
        "arc_hash_value": "8a1eef8ab0ad431b7e2a900fc15ad8216f010fd8e4bf739604cec39fb1f94049",
        "arc_hash_alg": "SHA-256"
      }]
  },
  "asset_attributes": {
    "arc_attachments": [
      {
        "arc_display_name": "Latest Conformance Report",
        "arc_attachment_identity": "blobs/e2a1d16c-03cd-45a1-8cd0-690831df1273",
        "arc_hash_value": "8a1eef8ab0ad431b7e2a900fc15ad8216f010fd8e4bf739604cec39fb1f94049",
        "arc_hash_alg": "SHA-256"
      }]
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