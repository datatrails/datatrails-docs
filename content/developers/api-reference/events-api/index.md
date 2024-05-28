---
title: "Events API"
description: "Events API Reference"
lead: "Events API Reference"
date: 2021-06-09T11:48:40+01:00
lastmod: 2021-06-09T11:48:40+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 107
toc: true
aliases: 
  - /docs/api-reference/events-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## Events API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

{{< note >}}
**Note:** You will need to create an Asset and wait for it to reach COMMITTED state before attempting to record an Event against that Asset. If you do not do this the API call will respond with an error.

One solution is to make a GET API call against the Asset ID and check that the confirmation_status field is COMMITTED, CONFIRMED of UNEQUIVOCAL before making the call to record the Event.

Another is to parse the Event API call for **400 Bad Request** errors (optionally also check for **429 Too Many Requests** errors) and then retry the call after a few seconds.
{{< /note >}}

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
**Note:** `RecordEvidence` is the primary, default behavior for creating Events.
{{< /note >}}

Add the request to the Asset record by POSTing it to the resource:

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events
```

The response is:

```json
{
  "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "asset_identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
  "confirmation_status": "COMMITTED",
  "block_number": 12,
  "transaction_index": 5,
  "transaction_id": "0x07569"
}
```

### Document Profile Event Creation

There are two [Document Profile Events](/developers/developer-patterns/document-profile/) that are available as part of the document lifecycle. These are to `publish` a new version and to `withdraw` the document from use.

#### Publish

Define the Event parameters and store in `/path/to/jsonfile`:

```json
{
    "behaviour": "RecordEvidence",
    "operation": "Record",
    "asset_attributes": {
        "document_hash_value":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "document_hash_alg":"sha256",
        "document_status": "Published",
        "document_version":"2"
    },
    "event_attributes": {
        "arc_description":"Publish version 2 of Test Document",
        "arc_display_type":"Publish",
        "document_version_authors": [
                        {
                "display_name": "George",
                "email": "george@rainbow.tv"
            },
            {
                "display_name": "Zippy",
                "email": "zippy@rainbow.tv"
            },
            {
                "display_name": "Bungle",
                "email": "bungle@rainbow.tv"
            }
        ]
    }
}
```

Add the request to the Asset record by POSTing it to the resource:

```bash
curl -v -X POST \
    -H "@datatrails-bearer.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events
```

The response is:

```json
{
    "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "asset_identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "event_attributes": {
        "document_version_authors": [
            {
                "display_name": "George",
                "email": "george@rainbow.tv"
            },
            {
                "display_name": "Zippy",
                "email": "zippy@rainbow.tv"
            },
            {
                "display_name": "Bungle",
                "email": "bungle@rainbow.tv"
            }
        ],
        "arc_description": "Publish version 2 of Test Document",
        "arc_display_type": "Publish"
    },
    "asset_attributes": {
        "document_status": "Published",
        "document_version": "2",
        "document_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "document_hash_alg": "sha256"
    },
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "timestamp_declared": "2023-09-27T12:55:16Z",
    "timestamp_accepted": "2023-09-27T12:55:16Z",
    "timestamp_committed": "1970-01-01T00:00:00Z",
    "principal_declared": {
        "issuer": "https://app.datatrails.ai/appidpv1",
        "subject": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "display_name": "CustomIntegration",
        "email": ""
    },
    "principal_accepted": {
        "issuer": "https://app.datatrails.ai/appidpv1",
        "subject": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "display_name": "CustomIntegration",
        "email": ""
    },
    "confirmation_status": "PENDING",
    "transaction_id": "",
    "block_number": 0,
    "transaction_index": 0,
    "from": "",
    "tenant_identity": ""
}
```
#### Withdraw

Define the Event parameters and store in `/path/to/jsonfile`:

```json
{
    "behaviour": "RecordEvidence",
    "operation": "Record",
    "asset_attributes": {
        "document_status":"Withdrawn"
    },
    "event_attributes": {
        "arc_description":"Withdraw the Test Document",
        "arc_display_type":"Withdraw"
    }
}
```

Add the request to the Asset record by POSTing it to the resource:

```bash
curl -v -X POST \
    -H "@datatrails-bearer.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events
```

The response is:

```json
{
    "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "asset_identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "event_attributes": {
        "arc_description": "Withdraw the Test Document",
        "arc_display_type": "Withdraw"
    },
    "asset_attributes": {
        "document_status": "Withdrawn"
    },
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "timestamp_declared": "2023-09-27T13:08:32Z",
    "timestamp_accepted": "2023-09-27T13:08:32Z",
    "timestamp_committed": "1970-01-01T00:00:00Z",
    "principal_declared": {
        "issuer": "https://app.datatrails.ai/appidpv1",
        "subject": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "display_name": "CustomIntegration",
        "email": ""
    },
    "principal_accepted": {
        "issuer": "https://app.datatrails.ai/appidpv1",
        "subject": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "display_name": "CustomIntegration",
        "email": ""
    },
    "confirmation_status": "PENDING",
    "transaction_id": "",
    "block_number": 0,
    "transaction_index": 0,
    "from": "",
    "tenant_identity": ""
}
```

### Adding Attachments

The following assumes that an attachment has already been uploaded to DataTrails using the [Blob API](../blobs-api).

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
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report",
    },
    "arc_primary_image": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "photo.jpg",
      "arc_display_name": "arc_primary_image",
    },
  },
  "asset_attributes": {
    "latest_conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events
```

You should see the response:

```json
{
  "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "asset_identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "Safety Conformance",
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report",
    },
    "arc_primary_image": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report",
    },
  },
  "asset_attributes": {
    "latest_conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
  "confirmation_status": "COMMITTED",
  "block_number": 12,
  "transaction_index": 5,
  "transaction_id": "0x07569"
}
```

### Event Record Retrieval

Event records in DataTrails are tokenized at creation time and referred to in all future API calls by a permanent unique identity of the form:

```bash
assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

If you do not know the Event’s identity you can fetch Event records using other information you do know.

#### Fetch All Events

To fetch all Event records, simply `GET` the Events resources:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events"
```

#### Fetch Events for a Specific Asset

If you know the unique identity of the Asset record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events"
```

#### Fetch Specific Events by Identity

If you know the unique identity of the Asset and Event record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivst/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

#### Fetch Event by Type

To fetch all Events of a specific type, `GET` the Events resource and filter on `arc_display_type`:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events?event_attributes.arc_display_type=Software%20Package%20Release"
```

#### Fetch Event by Asset Attribute

To fetch all Events of a specific Asset attribute, `GET` the Events resource and filter on `asset_attributes` at the Asset level:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events?asset_attributes.document_status=Published"
```

#### Fetch Events by Filtering for Presence of a Field

To fetch all Events with a field set to any value, `GET` the Events resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events?event_attributes.arc_display_type=*"
```

Returns all Events which have `arc_display_type` that is not empty.

#### Fetch Events Which are Missing a Field

To fetch all Events with a field which is not set to any value, `GET` the Events resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events?event_attributes.arc_display_type!=*"
```

Returns all Events which do not have `arc_display_type` or in which `arc_display_type` is empty.

#### Fetch Events by Minimum Confirmation Status

To fetch all Events with a specified confirmation status or higher, `GET` the Events resource and filter on `minimum_trust`.
For example:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events?minimum_trust=COMMITTED"
```

Returns all Events which have a `confirmation_status` level of COMMITTED, CONFIRMED or UNEQUIVOCAL. 

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets/-/events?minimum_trust=CONFIRMED"
```

Returns all Events which have a `confirmation_status` level of CONFIRMED or UNEQUIVOCAL. 

## Events OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/assetsv2.swagger.json" >}}
