---
title: "Assets API"
description: "Assets API Reference"
lead: "Assets API Reference"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 102
toc: true
aliases: 
  - /docs/api-reference/assets-api/
---

{{< note >}}
For more information on Assets and Asset creation, visit our [Core Concepts](/platform/overview/core-concepts/#assets) and [Creating an Asset](/platform/overview/creating-an-asset/) guide.
{{< /note >}}

## Asset API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Asset Record Creation

Define the asset parameters and store in `/path/to/jsonfile`:

```json
{
  "attributes": {
    "picture_from_yesterday": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "somepic.jpeg",
      "arc_display_name": "Picture from yesterday",
    },
    "arc_firmware_version": "3.2.1",
    "arc_home_location_identity": "locations/42054f10-9952-4c10-a082-9fd0d10295ae"
  },
  "behaviours": [
    "RecordEvidence"
  ],
  "proof_mechanism": "SIMPLE_HASH",
  "public": false
}
```

Create the Asset:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/assets
```

The response is:

```json
{
  "at_time": "2019-11-27T14:44:19Z",
  "attributes": {
    "picture_from_yesterday": {
      "arc_attribute_type": "arc_attachment",
      "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
      "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
      "arc_blob_hash_alg": "SHA256",
      "arc_file_name": "somepic.jpeg",
      "arc_display_name": "Picture from yesterday",
    },
    "arc_firmware_version": "3.2.1",
    "arc_home_location_identity": "locations/42054f10-9952-4c10-a082-9fd0d10295ae"
  },
  "behaviours": [
    "RecordEvidence"
  ],
  "confirmation_status": "PENDING",
  "identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f",
  "owner": "0x601f5A7D3e6dcB55e87bf2F17bC8A27AaCD3511",
  "proof_mechanism": "SIMPLE_HASH",
  "public": false,
  "tenant_identity": "tenant/8e0b600c-8234-43e4-860c-e95bdcd695a9",
  "tracked": "TRACKED"
}
```
#### Creating a Public Asset

{{< warning >}}
**Warning**: Assets can only be made public at Asset creation and cannot be made private afterwards.
{{< /warning >}}

In most cases it is appropriate to create a standard Asset. These Assets can only be shared externally using Access Policies as described in [Sharing Assets with OBAC](/platform/administration/sharing-assets-with-obac/) or the [IAM Policies API Reference](../iam-policies-api/).

However, it is also possible to create a Public Asset which can be shared with a read-only public url; similar to the link sharing you may have seen in file sharing services like Google Drive or DropBox.

Public Assets can be used for Public Attestation, where you may wish to publicly assert data you have published.

For example, the vulnerability reports against an OpenSource software package, or perhaps the maintenance records for a public building.

Creating a Public Asset just requires flipping the `public` value in the above request to `true`. From then on, **only** the creating Tenancy may update the Asset and Events on a Public Asset through their private, signed-in interface.

All Public Assets are then given a read-only public URL that can be retrieved using [Fetch a Public Asset's URL](./#fetch-a-public-assets-url), any Events added to that Public Asset will also get their own unique Public URL that can be retrieved with [Fetch a Public Asset's Event URL](./#fetch-a-public-assets-event-url).

This link can be shared with anyone to give them read-only access to the Asset or Event without the need to sign in.

To interact with the unauthenticated Public Interface for a Public Asset see the [Public Assets API Reference](../public-assets-api/). To update the Assets and Events as the creating Tenant on a Public Asset's authenticated Private Interface, you would still use the standard Assets and Events API as normal.
### Asset Record Retrieval

Asset records in RKVST are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
assets/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the Asset’s identity you can fetch Asset records using other information you do know.

#### Fetch All Assets

To fetch all Asset records, simply `GET` the Assets resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets
```

#### Fetch Specific Asset by Identity

If you know the unique identity of the Asset record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch Specific Asset at Given Point in Time by Identity

If you know the unique identity of an Asset record and want to show its state at any given point in the past, simply `GET` with the following query parameter:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets/6a951b62-0a26-4c22-a886-1082297b063b?at_time=2021-01-13T12:34:21Z"
```

This will return the Asset record with the values it had on `2021-01-13T12:34:21Z`.

#### Fetch Assets by Name

To fetch all Assets with a specific name, GET the Assets resource and filter on `arc_display_name`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name=tcl.ccj.003"
```

#### Fetch Assets by Type

To fetch all Assets of a specific type, `GET` the Assets resource and filter on `arc_display_type`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_type=Traffic%20light"
```

#### Fetch Assets by Proof Mechanism

To fetch all Assets that use a specific Proof Mechanism, `GET` the Assets resource and filter on `proof_mechanism`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets?attributes.proof_mechanism=simple_hash"
```
#### Fetch Events Ordered for SIMPLEHASHV1 Schema

To fetch Simple Hash Events in the order needed for the [SIMPLEHASHV1 schema](https://github.com/rkvst/rkvst-simplehash-python), `GET` the Assets resource, specifying a specific Asset ID or using `assets/-/events` to fetch Events for all Assets:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets/-/events?order_by=SIMPLEHASHV1"
```

#### Fetch Assets by Filtering for Presence of a Field

To fetch all Assets with a field set to any value, `GET` the Assets resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name=*"
```

Returns all Assets which have `arc_display_name` that is not empty.

#### Fetch Assets Which are Missing a Field

To fetch all Assets with a field which is not set to any value, `GET` the Assets resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name!=*"
```

Returns all Assets which do not have `arc_display_name` or in which `arc_display_name` is empty.

#### Fetch a Public Asset's URL

Fetch the Public URL of a Public Asset:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/86b61c4b-030e-4c07-9400-463612e6cee4:publicurl
```

```json
{
  "publicurl":"https://app.rkvst.io/archivist/publicassets/86b61c4b-030e-4c07-9400-463612e6cee4"
}
```

#### Fetch a Public Asset's Event URL

Fetch the Public URL of an Event on a Public Asset:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/86b61c4b-030e-4c07-9400-463612e6cee4/events/7da272ad-19d5-4106-b4af-2980a84c2721:publicurl
```

```json
{
  "publicurl":"https://app.rkvst.io/archivist/publicassets/86b61c4b-030e-4c07-9400-463612e6cee4/events/7da272ad-19d5-4106-b4af-2980a84c2721"
}
```

### Tracking and Untracking Assets

While deleting Assets is not possible, it is possible to hide them from default searches so that old or obsolete records don't crowd out the tenant estate or show up in partner tenancies when they shouldn't. 

#### Untracking an Asset

Untracking is actually an Event in the Asset lifecycle, so it is necessary to know the Asset identity and POST to it directly. Here we assume we are working with an Asset with identity `assets/add30235-1424-4fda-840a-d5ef82c4c96f`.

Define the Event parameters and store in `/path/to/jsonfile`:

```json
{
  "operation": "StopTracking",
  "behaviour": "Builtin"
}
```

Untrack the Asset:

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
  "identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/a5e68a57-c5c2-42db-b2a6-e361ba2a7b4a",
  "asset_identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f",
  "event_attributes": {},
  "asset_attributes": {},
  "operation": "StopTracking",
  "behaviour": "Builtin",
  "timestamp_declared": "2023-02-23T19:55:44Z",
  "timestamp_accepted": "2023-02-23T19:55:44Z",
  "timestamp_committed": "1970-01-01T00:00:00Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  },
  "principal_accepted": {
    "issuer": "job.idp.server/1234",
    "subject": "bob@job"
  },
  "confirmation_status": "PENDING",
  "transaction_id": "",
  "block_number": 0,
  "transaction_index": 0,
  "from": "",
  "tenant_identity": ""
}
```

#### (Re-)Tracking an Asset

It is possible to reverse an untracking Event by tracking the Asset again, assuming you know the Asset identity. Here we assume we are working with an Asset with identity `assets/add30235-1424-4fda-840a-d5ef82c4c96f`.

Define the Event parameters and store in `/path/to/jsonfile`:

```json
{
  "operation": "StartTracking",
  "behaviour": "Builtin"
}
```

Track the Asset:

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
  "identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f/events/a5e68a57-c5c2-42db-b2a6-e361ba2a7b4a",
  "asset_identity": "assets/add30235-1424-4fda-840a-d5ef82c4c96f",
  "event_attributes": {},
  "asset_attributes": {},
  "operation": "StartTracking",
  "behaviour": "Builtin",
  "timestamp_declared": "2023-02-23T19:55:44Z",
  "timestamp_accepted": "2023-02-23T19:55:44Z",
  "timestamp_committed": "1970-01-01T00:00:00Z",
  "principal_declared": {
    "issuer": "idp.synsation.io/1234",
    "subject": "phil.b",
    "email": "phil.b@synsation.io"
  },
  "principal_accepted": {
    "issuer": "job.idp.server/1234",
    "subject": "bob@job"
  },
  "confirmation_status": "PENDING",
  "transaction_id": "",
  "block_number": 0,
  "transaction_index": 0,
  "from": "",
  "tenant_identity": ""
}
```

## Asset OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/master/doc/openapi/assetsv2.swagger.json" >}}
