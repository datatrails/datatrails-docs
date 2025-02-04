---
title: "Asset-Events API"
description: "Asset-Events API Reference"
lead: "Asset based Events API Reference"
date: 2021-06-09T11:48:40+01:00
lastmod: 2021-06-09T11:48:40+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 105
toc: true
aliases: 
  - /docs/api-reference/asset-events-api/
---
DataTrails provides two mechanisms for persisting provenance metadata:

1. [Asset based Events](/developers/api-reference/asset-events-api) (this API): where a series of Events are grounded to a specific Asset.
1. [Asset-free Events](/developers/api-reference/events-api) (preview) : where events can be correlated across pre-defined Trails.

The Asset-free Events implementation is the future focus of the DataTrails platform providing the capabilities of Asset based events, with broader flexibility, performance and scalability.
Asset-free Events are currently in preview, inviting early developer feedback.

The transition to Asset-free Events involves removing the dependency to anchoring Events in an Asset and shifting from mutable Asset Attributes to immutable Event Attributes.
To minimize the impact, prior to switching to Asset-free Events, it is recommended to use Event Attributes, rather than Asset Attributes.

{{< note >}}
**Note:** For more information on Assets and Asset creation, visit [Core Concepts](/platform/overview/core-concepts/#assets) and the [Creating an Asset](/platform/overview/creating-an-asset/) guide.
{{< /note >}}

## Asset-Events API Examples

{{< note >}}
**Note:** If you are looking for a simple way to test DataTrails APIs you might prefer the [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI.

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

{{< note >}}
**Note:** You will need to create an Asset first in order to submit Events against it.
The dependency on Assets is being deprecated.
In a future release, Events will be created independently from Assets.
{{< /note >}}

### Asset Reference

- Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.
- Capture the Asset ID by which the events will be associated.  
  (eg: `ASSET_ID=01234567-890-1234-5678-901234567890`)  
  Find the ASSET_ID with [Fetch All Assets](/developers/api-reference/assets-api/#fetch-all-assets)

  ```bash
  ASSET_ID=<asset-id>
  ```

{{< note >}}
**Note:** DataTrails will be transitioning to an event centric design, removing the need to create and reference Assets to hold collections of Events.
{{< /note >}}

### Event Creation

- Define the Event parameters:

  ```bash
  cat > /tmp/event.json <<EOF
  {
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "event_attributes": {
      "arc_display_type": "Safety Conformance",
      "Safety Rating": "90",
      "inspector": "Clouseau"
    }
  }
  EOF
  ```

{{< note >}}
**Note:** `RecordEvidence` is the primary, default behavior for creating Events.
{{< /note >}}

- Add the request to the Asset record by POSTing it to the resource:

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
    "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "asset_identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "event_attributes": {
      "inspector": "Clouseau",
      "arc_display_type": "Safety Conformance",
      "Safety Rating": "90"
    },
    "asset_attributes": {},
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "timestamp_declared": "2024-09-04T23:45:20Z",
    "timestamp_accepted": "2024-09-04T23:45:20Z",
    "timestamp_committed": "1970-01-01T00:00:00Z",
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

- To query the events jump to [Fetch Specific Events by Identity](#fetch-events-for-a-specific-asset)

### DataTrails Reserved Attributes

The DataTrails platform as reserved attributes starting with `arc_`.
Asset-Events have the following reserved attributes:

- **`arc_display_type`**: The value used to display in the DataTrails Application.
- **`arc_primary_image`**: A attribute containing a dictionary of references to a Blob, used to display in the DataTrails Application.
- **`arc_attribute_type`**: When set within a nested attribute, the value of `"arc_attachment"` identifies a reference to a [DataTrails Blob](/developers/api-reference/blobs-api/)
- **`arc_display_name"`**: When set to `"arc_primary_image"`, the blob is displayed in the DataTrails application.
- **`arc_blob_hash_value`**: When `arc_attribute_type` = `"arc_attachment"`, the value must equal the hash value within the associated `arc_blob_identity`.
- **`arc_blob_identity`**: A reference to a [Blob](/developers/api-reference/blobs-api/)
- **`arc_blob_hash_alg`**: The algorithm of the `arc_blob_hash_value` (eg: "SHA256")
- **`arc_file_name`**: When `arc_attribute_type` = `"arc_attachment"`, the file name of the blob.

### Event Primary Image

Asset-Events can use the [Blobs API](/developers/api-reference/blobs-api/) to associate a primary image in the DataTrails Application.

#### Primary Image Variables

- To associate an existing Blob, set the `BLOB_ID`, `BLOB_HASH` value and `BLOB_FILE` from the [Blobs API](/developers/api-reference/blobs-api/):

  {{< note >}}
  NOTE: The `ASSET_ID` dependency will be removed with [Non-asset based Events (preview)](/developers/api-reference/events-api/)
  {{< /note >}}

  ```bash
  ASSET_ID=<asset-id>
  BLOB_ID=<blob-id>
  BLOB_FILE=<file.ext>
  BLOB_HASH=<hash-value>
  ```

  Example:

  ASSET_ID=assets/a1234567-8901  
  BLOB_ID=blobs/b1234567-8901  
  BLOB_FILE=conformance.pdf  
  BLOB_HASH=h1234567  

- Associate a Blob as the Event Primary Image:

  ```json
  cat > /tmp/event.json <<EOF
  {
    "operation": "Record",
    "behaviour": "RecordEvidence",
    "event_attributes": {
      "arc_primary_image": {
        "arc_attribute_type": "arc_attachment",
        "arc_display_name": "arc_primary_image",
        "arc_blob_hash_value": "$BLOB_HASH",
        "arc_blob_identity": "$BLOB_ID",
        "arc_blob_hash_alg": "SHA256",
        "arc_file_name": "$BLOB_FILE"
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

### Adding Attachments

To associate an Attachment with an Asset-Event, see the [Attachments API](/developers/api-reference/attachments-api/)

### Document Profile Event Creation

There are two [Document Profile Events](/developers/developer-patterns/document-profile/) that are available as part of the document lifecycle. These are to `publish` a new version and to `withdraw` the document from use.

#### Publish

- Define the Event parameters:

  ```json
  cat > /tmp/event.json <<EOF
  {
    "behaviour": "RecordEvidence",
    "operation": "Record",
    "asset_attributes": {
      "document_hash_value":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
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
  EOF
  ```

- Add the request to the Asset record by POSTing it to the resource:

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
      "identity": "assets/xxxxxxxx/events/xxxxxxxx-xxxx",
      "asset_identity": "assets/xxxxxxxx-xxxx",
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
        "document_hash_value": "xxxxxxxxxxxxxxxxxxxxx",
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

- Define the Event parameters:

  ```json
  cat > /tmp/event.json <<EOF
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
  EOF
  ```

- Add the request to the Asset record by POSTing it to the resource:

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

### Event Record Retrieval

Event records in DataTrails are tokenized at creation time and referred to in all future API calls by a permanent unique identity of the form:

```bash
assets/$ASSET_ID/events/$EVENT_ID
```

If you do not know the Event’s identity you can fetch Event records using other information you do know.

#### Fetch All Events

- To fetch all Event records, simply `GET` the Events resources:

  ```bash
  curl -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?page_size=5" \
      | jq
  ```

#### Fetch Events for a Specific Asset

- If you know the unique identity of the Asset record simply `GET` the resource:

  ```bash
  curl -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/$ASSET_ID/events?page_size=5" \
      | jq
  ```

#### Fetch Specific Events by Identity

- If you know the unique identity of the Asset and Event record simply `GET` the resource:

  ```bash
  curl -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivst/v2/assets/$ASSET_ID/events/$EVENT_ID" \
      | jq
  ```

#### Fetch Event by Type

- To fetch all Events of a specific type, `GET` the Events resource and filter on `arc_display_type`:

  ```bash
  curl -g -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?event_attributes.arc_display_type=Software%20Package%20Release&page_size=5" \
      | jq
  ```

#### Fetch Event by Asset Attribute

- To fetch all Events of a specific Asset attribute, `GET` the Events resource and filter on `asset_attributes` at the Asset level:

  ```bash
  curl -g -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?asset_attributes.document_status=Published&page_size=5" \
      | jq
  ```

#### Fetch Events by Filtering for Presence of a Field

- To fetch all Events with a field set to any value, `GET` the Events resource and filter on most available fields. For example:

  ```bash
  curl -g -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?event_attributes.arc_display_type=*&page_size=5" \
      | jq
  ```

  Returns all Events which have `arc_display_type` that is not empty.

#### Fetch Events Which are Missing a Field

- To fetch all Events with a field which is not set to any value, `GET` the Events resource and filter on most available fields. For example:

  ```bash
  curl -g -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?event_attributes.arc_display_type!=*&page_size=5" \
      | jq
  ```

  Returns all Events which do not have `arc_display_type` or in which `arc_display_type` is empty.

#### Fetch Events by Minimum Confirmation Status

- To fetch all Events with a specified confirmation status or higher, `GET` the Events resource and filter on `minimum_trust`.

  ```bash
  curl -g -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?minimum_trust=COMMITTED&page_size=5" \
      | jq
  ```

- To fetch all Events which have a `confirmation_status` level of COMMITTED, CONFIRMED or UNEQUIVOCAL.

  ```bash
  curl -g -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v2/assets/-/events?minimum_trust=CONFIRMED&page_size=5" \
      | jq
  ```

  Returns all Events which have a `confirmation_status` level of CONFIRMED or UNEQUIVOCAL.

## Events OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/assetsv2.swagger.json" >}}
