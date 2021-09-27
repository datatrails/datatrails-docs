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
weight: 106
toc: true
---

## Attachments Behaviour

The following operations assume that an attachment has been uploaded to RKVST node using the [Blob API](../blobs-api). 

This attachment uuid is generically referred to as:

```bash
blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Each attachment has an associated hash value and the name of the hash algorithm used.

### Attachments API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Define the event parameters and store in `/path/to/jsonfile`:

```json
{
  "operation": "Attach",
  "behaviour": "Attachments",
  "event_attributes": {
    "arc_append_attachments": [
      {
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "arc_display_name": "an attachment 1",
            "arc_hash_value": "jnwpjocoqsssnundwlqalsqiiqsqp;lpiwpldkndwwlskqaalijopjkokkkojijl",
            "arc_hash_alg": "sha256",
      },
      {
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "arc_display_name": "an attachment 2",
            "arc_hash_value": "042aea10a0f14f2d391373599be69d53a75dde9951fc3d3cd10b6100aa7a9f24",
            "arc_hash_alg": "sha256",
      }
    ]
  },
  "timestamp_declared": "2019-11-27T14:44:19Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  }
}
```

Add the Attachments request to the Asset Record by POSTing it to the resource:

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
  "operation": "Attach",
  "behaviour": "Attachments",
  "event_attributes": {
    "arc_append_attachments": [
      {
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "arc_display_name": "an attachment 1",
            "arc_hash_value": "jnwpjocoqsssnundwlqalsqiiqsqp;lpiwpldkndwwlskqaalijopjkokkkojijl",
            "arc_hash_alg": "sha256",
      },
      {
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "arc_display_name": "an attachment 2",
            "arc_hash_value": "042aea10a0f14f2d391373599be69d53a75dde9951fc3d3cd10b6100aa7a9f24",
            "arc_hash_alg": "sha256",
      }
    ],
  },
  "asset_attributes": {
    "arc_attachments": [
      {
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "arc_display_name": "an attachment 1",
            "arc_hash_value": "jnwpjocoqsssnundwlqalsqiiqsqp;lpiwpldkndwwlskqaalijopjkokkkojijl",
            "arc_hash_alg": "sha256",
      },
      {
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "arc_display_name": "an attachment 2",
            "arc_hash_value": "042aea10a0f14f2d391373599be69d53a75dde9951fc3d3cd10b6100aa7a9f24",
            "arc_hash_alg": "sha256",
      }
    ]
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

### Attachments OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/b-attachmentsv2.swagger.json" >}}

## RecordEvidence Behaviour

`RecordEvidence` is the primary, default behaviour for creating Events.

### RecordEvidence Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Define the event parameters and store in `/path/to/jsonfile`:

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "conformance_report": "blobs/e2a1d16c-03cd-45a1-8cd0-690831df1273"
  },
  "timestamp_declared": "2019-11-27T14:44:19Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  }
}
```
Add the `RecordEvidence` request to the Asset Record by POSTing it to the resource:

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
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "conformance_report": "blobs/e2a1d16c-03cd-45a1-8cd0-690831df1273"
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

### Record Evidence OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/b-recordevidencev2.swagger.json" >}}