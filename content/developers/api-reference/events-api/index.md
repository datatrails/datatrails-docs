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

{{< note >}}
**Note:** If you are looking for a simple way to test DataTrails APIs you might prefer the [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI.

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

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

### Event Record Retrieval

Event records in DataTrails are assigned UUIDs at creation time and referred to in all future API calls by a their unique identity in the format: `events/<event-id>`



#### Fetch Events by Identity

- Replace the `<event-id>` below, using the event-id from the created event above: `"identity": "events/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`:

  ```bash
  EVENT_ID=<event-id>
  ```

- Query the /events API to retrieve the recorded event:

  ```bash
  curl -X GET \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      "https://app.datatrails.ai/archivist/v1/events/$EVENT_ID" | jq
  ```



#### Fetch Multiple Events

- To fetch multiple events use a search document and post it to Events Search endpoint
  Search document has following form:

  ```json
  {
    "filter": "",
    "top": 10,
    "skip": 0,
  }
  ```

{{< note >}}
**Note:** The current preview does not support filtering of  Events.
Filtering across event attributes and trails are coming in a future preview.
{{< /note >}}

  where top indicates number of results to return (max. 50) and skip indicates how many results to skip over before retruning set of results.

  Response will be a list of events matching above criteria:

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
    ],
  }
  ```
  
  Use `top` and `skip` alongside `x-total-count` response header to navigate results. If sum of `skip` and number of results in response is less than the count of all results (this will be returned in `x-total-count` response header) there is more results to retrieve, to get next set of results sumply re-issue `/search` request with skip increased by number of results in current response.

- To fetch all Event records, simply create search document and save to a file `search.json`:

  ```json
  {
    "filter": "",
    "top": 10,
    "skip": 0,
  }
  ```

  and `POST` it to Search endpoint:

  ```bash
  curl -X POST \
      -H "@$HOME/.datatrails/bearer-token.txt" \
      -d @$HOME/search.json \
      "https://app.datatrails.ai/archivist/v1/events/search" \
      | jq
  ```

  if `x-total-count` response header has value greater than 10 (as indicated by value of `top` in `search.json`) modify `serch.json` to to following:

  ```json
  {
    "filter": "",
    "top": 10,
    "skip": 10,
  }
  ```

  and `POST` to the same nedpoint again to retrieve second page of results, and repeat this process until `skip` + numer or results in response is equal `x-total-count`.


## Events OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/events.swagger.json" >}}

## Integrity Protecting Content

Integrity protected content can be hashed within an Event using the [Attachments API](/developers/api-reference/attachments-api/).
