---
title: "Events API (preview)"
description: "Events API Reference (preview)"
lead: "Events API Reference"
date: 2025-01-09T11:48:40+01:00
lastmod: 2025-01-09T11:48:40+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 113
toc: true
aliases: 
  - /docs/api-reference/events-api/
---
DataTrails provides two mechanisms for persisting provenance metadata:

1. [Asset based Events](/developers/api-reference/asset-events-api): where a series of Events are grounded to a specific Asset.
1. [Asset-free Events](/developers/api-reference/events-api) (preview) : where events can be correlated across pre-defined Trails.

The Asset-free Events implementation is the future focus of the DataTrails platform providing the capabilities of Asset based events, with broader flexibility, performance and scalability.
Asset-free Events are currently in preview, inviting early developer feedback.

The transition to Asset-free Events involves removing the dependency to anchoring Events in an Asset and shifting from mutable Asset Attributes to immutable Event Attributes.
To minimize the impact, prior to switching to Asset-free Events, it is recommended to use Event Attributes, rather than Asset Attributes.

{{< note >}}
**Note:** For more information on Assets and Asset creation, visit [Core Concepts](/platform/overview/core-concepts/#assets) and the [Creating an Asset](/platform/overview/creating-an-asset/) guide.
{{< /note >}}

## Events API Examples

### Event Creation

- Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.
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
    "identity": "events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "attributes": {
      "inspector": "Clouseau",
      "arc_display_type": "Safety Conformance",
      "Safety Rating": "90"
    },
    "trails": [
      "Safety Conformance",
      "Clouseau"
    ],
    "origin_tenant": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "created_by": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "created_at": 1736421833577,
    "confirmation_status": "STORED",
    "merklelog_commit": {
      "index": "0",
      "idtimestamp": ""
    }
  }
  ```

### DataTrails Reserved Attributes

### DataTrails Reserved Attributes

The DataTrails platform has reserved attributes starting with `arc_` to perform specific capabilities.
See [Reserved Attributes](/glossary/reserved-attributes/) for more info.

### Event Primary Image

Events can use the [Blobs API](/developers/api-reference/blobs-api/) to associate a primary image in the DataTrails Application.

#### Primary Image Variables

- To associate an existing Blob, set the `BLOB_ID`, `BLOB_HASH` value and `BLOB_FILE` from the [Blobs API](/developers/api-reference/blobs-api/):

  ```bash
  BLOB_ID=<blob-id>
  BLOB_FILE=<file.ext>
  BLOB_HASH=<hash-value>
  ```

  Example:

  BLOB_ID=blobs/b1234567-890b  
  BLOB_FILE=conformance.pdf  
  BLOB_HASH=h1234567h  

- Associate a Blob as the Event Primary Image:

  ```json
  cat > /tmp/event.json <<EOF
  {
    "trails": ["Safety Conformance", "Clouseau"],
    "attributes": {
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
      https://app.datatrails.ai/archivist/v1/events \
      | jq
  ```

### Adding Attachments

To associate an Attachment with an Event, see the [Attachments API](/developers/api-reference/attachments-api/)

### Event Record Retrieval

Event records in DataTrails are assigned UUIDs at creation time and referred to in all future API calls by a their unique identity in the format: `events/<event-id>`

## Fetch Events by Identity

- Replace the `<event-id>` below, using the event-id from the created event above.  
  `"identity": "events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`:  
  Note, "`events/`" must be included as it's part of the resource name:

  ```bash
  EVENT_ID=<event-id>
  ```

- Query the /events API to retrieve the recorded event:

  ```bash
  curl -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v1/$EVENT_ID" | jq
  ```

## Filtering and Paging Events

- To fetch multiple events, use a search document, posting to the `/events/search` endpoint  
  Search document has following form:

  ```bash
  cat > /tmp/search.json <<EOF
  {
    "filter": "",
    "top": 20,
    "skip": 0
  }
  EOF
  ```

  where:  
  `filter` = attribute name/value pairs  
  `top` = number of results to return (max. 50) and  
  `skip` = how many results to skip over before returning set of results

  {{< note >}}
  **Note:** The current preview does not support filtering of Events.
  Filtering across event attributes and trails are coming in a future preview.
  {{< /note >}}

  - Post `search.json` to the `/search` endpoint:

    ```bash
    curl -X POST \
        -H "@$HOME/.datatrails/bearer-token.txt" \
        -d "@/tmp/search.json" \
        "https://app.datatrails.ai/archivist/v1/events/search" \
        | jq
    ```

  - The response will include a list of events matching above criteria:

    ```json
    {
      "events": [
        {
          "identity": "events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "attributes": {
            "inspector": "Clouseau",
            "arc_display_type": "Safety Conformance",
            "Safety Rating": "90"
          },
          "trails": [
            "Safety Conformance",
            "Clouseau"
          ],
          "origin_tenant": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "created_by": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "created_at": 1736421833577,
          "confirmation_status": "STORED",
          "merklelog_commit": {
            "index": "0",
            "idtimestamp": ""
          }
        },
        {
          "identity": "events/yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
          "attributes": {
            "inspector": "Clouseau",
            "arc_display_type": "Safety Conformance",
            "Safety Rating": "99"
          },
          "trails": [
            "Safety Conformance",
            "Clouseau"
          ],
          "origin_tenant": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "created_by": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "created_at": 1736421873579,
          "confirmation_status": "STORED",
          "merklelog_commit": {
            "index": "0",
            "idtimestamp": ""
          }
        }
      ]
    }
    ```

  ### Fetch Paged Results

  Use `top` and `skip` alongside `x-total-count` response header to navigate results.
  If sum of `skip` and number of results in response is less than the count of all results (`x-total-count` in the response header) there are more results to retrieve.
  To get the next set of results, re-issue the `/search` request with `skip` increased by number of results in current response.

  If `x-total-count` response header has value greater than 2 (as indicated by value of `top` in `search.json`) modify `search.json` to the following:

  ```bash
  cat > /tmp/search.json <<EOF
  {
    "filter": "",
    "top": 2,
    "skip": 2
  EOF
  ```

  - Post to the `/events/search/` endpoint to retrieve another page of results, repeating this process until `skip` + number or results in the response is equal to `x-total-count`.

    ```bash
    curl -X POST \
        -H "@$HOME/.datatrails/bearer-token.txt" \
        -d /tmp/search.json \
        "https://app.datatrails.ai/archivist/v1/events/search" \
        | jq
    ```

## Integrity Protecting Content

Integrity protected content can be hashed within an Event using the [Attachments API](/developers/api-reference/attachments-api/).

## Events OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/events.swagger.json" >}}
