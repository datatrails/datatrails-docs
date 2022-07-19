---
title: "Assets API"
description: "Assets API Reference"
lead: "Assets API Reference"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 102
toc: true
---

## Asset API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Asset Record Creation

Define the asset parameters and store in `/path/to/jsonfile`:

```json
{
  "attributes": {
    "arc_attachments": [
      {
        "arc_attachment_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
        "arc_display_name": "Picture from yesterday",
        "arc_hash_alg": "sha256",
        "arc_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
      }
    ],
    "arc_firmware_version": "3.2.1",
    "arc_home_location_identity": "locations/42054f10-9952-4c10-a082-9fd0d10295ae"
  },
  "behaviours": [
    "RecordEvidence",
    "Attachments"
  ],
  "proof_mechanism": "SIMPLE_HASH",
  "public": false
}
```

Create the asset:

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
    "arc_attachments": [
      {
        "arc_attachment_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
        "arc_display_name": "Picture from yesterday",
        "arc_hash_alg": "sha256",
        "arc_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
      }
    ],
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
**Warning**: Assets can only be made public at Asset Creation and cannot be made private afterwards.
{{< /warning >}}

In most cases it is appropriate to create a standard Asset. These Assets can only be shared externally using Access Policies as described in [Sharing Assets with OBAC](../../rkvst-basics/sharing-assets-with-obac/) or the [IAM Policies API Reference](../iam-policies-api/).

However it is also possible to create a Public Asset which can be shared with a read-only public url; similar to the link sharing you may have seen in file sharing services like Google Drive or DropBox.

Public Assets can be used for Public Attestation, where you may wish to publicly assert data you have published.

For example, the vulnerability reports against an OpenSource software package, or perhaps the maintenance records for a public building.

Creating a Public Asset just requires flipping the `public` value in the above request to `true`, from then on **only** the creating tenancy may update the asset and events on a Public Asset through their private, signed-in interface.

All Public Assets are then given a read-only public URL that can be retrieved using [Fetch a Public Asset's URL](./#fetch-a-public-assets-url), any events added to that Public Asset will also get their own unique Public URL that can be retrieved with [Fetch a Public Asset's Event URL](./#fetch-a-public-assets-event-url).

This link can be shared with anyone to give them read-only access to the asset or event without the need to sign in.

To interact with the unauthenticated Public Interface for a Public Asset see the [Public Assets API Reference](../public-assets-api/). To update the Assets and Events as the creating tenant on a Public Asset's authenticated Private Interface you would still use the standard Assets and Events API as normal.
### Asset Record Retrieval

Asset records in RKVST are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
assets/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the asset’s identity you can fetch asset records using other information you do know.

#### Fetch All Assets

To fetch all asset records, simply `GET` the assets resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets
```

#### Fetch Specific Asset by Identity

If you know the unique identity of the Asset Record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch Specific Asset at Given Point in Time by Identity

If you know the unique identity of an Asset Record and want to show its state at any given point in the past, simply `GET` with following query parameter

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets/6a951b62-0a26-4c22-a886-1082297b063b?at_time=2021-01-13T12:34:21Z
```

This will return the Asset Record with the values it had on `2021-01-13T12:34:21Z`

#### Fetch Assets by Name

To fetch all assets with a specific name, GET the assets resource and filter on `arc_display_name`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name=tcl.ccj.003
```

#### Fetch Assets by Type

To fetch all assets of a specific type, `GET` the assets resource and filter on `arc_display_type`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_type=Traffic%20light
```

#### Fetch Assets by Filtering for Presence of a Field

To fetch all assets with a field set to any value, `GET` the assets resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name=*
```

Returns all assets which have `arc_display_name` that is not empty.

#### Fetch Assets Which are Missing a Field

To fetch all assets with a field which is not set to any value, `GET` the assets resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets?attributes.arc_display_name!=*
```

Returns all assets which do not have `arc_display_name` or in which `arc_display_name` is empty.

#### Fetch a Public Asset's URL

Fetch the Public URL of a Public Asset

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

Fetch the Public URL of an Event on a Public Asset

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


## Asset OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/assetsv2.swagger.json" >}}
