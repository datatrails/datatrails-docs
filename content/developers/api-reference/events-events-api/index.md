---
title: "Events API"
description: "Events API Reference"
lead: "Events API Reference"
date: 2025-01-09T11:48:40+01:00
lastmod: 2025-01-09T11:48:40+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 107
toc: true
aliases: 
  - /docs/api-reference/events-events-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance.
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI.

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

## Events API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Event Creation

- Define the Event parameters and store in `/tmp/event.json`:

  ```bash
  cat > /tmp/event.json <<EOF
  {
    "trails": ["Safety Conformance", "Clouseau"],
    "attributes": {
      "arc_display_type": "Safety Conformance",
      "Safety Rating": "90",
      "inspector": "Clouseau"
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
      https://app.datatrails.ai/archivist/v1/events \
      | jq
  ```

- The response:

  ```json
  {
    "identity": "events/01944ace-7b69-7a93-833d-7f71edd34841",
    "attributes": {
      "inspector": "Clouseau",
      "arc_display_type": "Safety Conformance",
      "Safety Rating": "90"
    },
    "trails": [
      "Safety Conformance",
      "Clouseau"
    ],
    "origin_tenant": "tenant/d20182b2-bf9c-42c5-95ec-5607a6cbc095",
    "created_by": "1321545b-49b1-4a82-8766-029b6c1bcd63",
    "created_at": 1736421833577,
    "confirmation_status": "STORED",
    "merklelog_commit": {
      "index": "0",
      "idtimestamp": ""
    }
  }
  ```

- To query the events jump to [Fetch Specific Events by Identity](#fetch-events-for-a-specific-asset)

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
cat > /tmp/event.json <<EOF
{
  "attributes": {
    "arc_display_type": "Safety Conformance",
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached",
    "conformance_report": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report"
    },
    "arc_primary_image": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "photo.jpg",
      "arc_display_name": "arc_primary_image"
    }
  }
}
EOF
```

Add the request to the Asset Record by POSTing it to the resource:

```bash
curl -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/tmp/event.json" \
    https://app.datatrails.ai/archivist/v1/events
```

The response:

```json
{
  "identity": "events/01944adf-1c85-75f4-a8d4-6d800ee9c578",
  "attributes": {
    "conformance_report": {
      "arc_file_name": "safety_conformance.pdf",
      "arc_display_name": "Conformance Report",
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256"
    },
    "arc_primary_image": {
      "arc_file_name": "photo.jpg",
      "arc_display_name": "arc_primary_image",
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "arc_blob_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "arc_blob_hash_alg": "SHA256"
    },
    "arc_display_type": "Safety Conformance",
    "arc_description": "Safety conformance approved for version 1.6. See attached conformance report",
    "arc_evidence": "DVA Conformance Report attached"
  },
  "trails": [],
  "origin_tenant": "tenant/d20182b2-bf9c-42c5-95ec-5607a6cbc095",
  "created_by": "1321545b-49b1-4a82-8766-029b6c1bcd63",
  "created_at": 1736422923397,
  "confirmation_status": "STORED",
  "merklelog_commit": {
    "index": "0",
    "idtimestamp": ""
  }
}
```

### Event Record Retrieval

Event records in DataTrails are tokenized at creation time and referred to in all future API calls by a permanent unique identity of the form:

```bash
events/$EVENT_ID
```

{{< note >}}
**Note:** Currently we only support fetching specific events by identity.
{{< /note >}}

#### Fetch Specific Events by Identity

If you know the unique identity of the Event record simply `GET` the resource:

```bash
curl -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivst/v1/events/<EVENT_UUID>"
```

## Events OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/events.swagger.json" >}}
