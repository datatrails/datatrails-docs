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
weight: 101
toc: true
---

## Asset API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Set the URL (for example):

```bash
export URL=https://synsation.1234-5678.nodes.archivist.jitsuin.io 
```

### Asset Record Creation

Define the asset parameters and store in `/path/to/jsonfile`:

```json
{
    "behaviours": ["RecordEvidence", "Attachments"],
    "attributes": {
        "arc_firmware_version": "1.0",
        "arc_serial_number": "vtl-x4-07",
        "arc_display_name": "tcl.ppj.003",
        "arc_description": "Traffic flow control light at A603 North East",
        "arc_home_location_identity": "locations/115340cf-f39e-4d43-a2ee-8017d672c6c6",
        "arc_display_type": "Traffic light with violation camera",
        "some_custom_attribute": "value",
        "arc_attachments": [
            {
                "arc_display_name": "arc_primary_image",
                "arc_attachment_identity": "blobs/87b1a84c-1c6f-442b-923e-a97516f4d275",
                "arc_hash_alg": "SHA256",
                "arc_hash_value": "246c316e2cd6971ce5c83a3e61f9880fa6e2f14ae2976ee03500eb282fd03a60"
            }
        ]
    }
}
```

Create the asset:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v2/assets
```

The response is:

```json
{
    "identity": "assets/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "behaviours": [
        "RecordEvidence",
        "Attachments"
    ],
    "attributes": {
        "arc_serial_number": "vtl-x4-07",
        "arc_display_name": "tcl.ppj.003",
        "arc_description": "Traffic flow control light at A603 North East",
        "arc_home_location_identity": "locations/115340cf-f39e-4d43-a2ee-8017d672c6c6",
        "arc_display_type": "Traffic light with violation camera",
        "arc_firmware_version": "1.0",
        "some_custom_attribute": "value",
        "arc_attachments": [
            {
                "arc_display_name": "arc_primary_image",
                "arc_attachment_identity": "blobs/87b1a84c-1c6f-442b-923e-a97516f4d275",
                "arc_hash_alg": "SHA256",
                "arc_hash_value": "246c316e2cd6971ce5c83a3e61f9880fa6e2f14ae2976ee03500eb282fd03a60"
            }
        ]
    },
    "confirmation_status": "PENDING",
    "tracked": "TRACKED"
}
```

### Asset Record Retrieval

Asset records in Jitsuin Archivist are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
assets/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the asset’s identity you can fetch asset records using other information you do know.

#### Fetch All Assets

To fetch all asset records, simply `GET` the assets resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets
```

#### Fetch Specific Asset by Identity

If you know the unique identity of the Asset Record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch Specific Asset at Given Point in Time by Identity

If you know the unique identity of an Asset Record and want to show its state at any given point in the past, simply `GET` with following query parameter

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets/6a951b62-0a26-4c22-a886-1082297b063b?at_time=2021-01-13T12:34:21Z
```

This will return the Asset Record with the values it had on `2021-01-13T12:34:21Z`

#### Fetch Assets by Name

To fetch all assets with a specific name, GET the assets resource and filter on `arc_display_name`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets?attributes.arc_display_name=tcl.ccj.003
```

#### Fetch Assets by Type

To fetch all assets of a specific type, `GET` the assets resource and filter on `arc_display_type`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets?attributes.arc_display_type=Traffic%20light
```

#### Fetch Assets by Filtering for Presence of a Field

To fetch all assets with a field set to any value, `GET` the assets resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets?attributes.arc_display_name=*
```

Returns all assets which have `arc_display_name` that is not empty.

#### Fetch Assets Which are Missing a Field

To fetch all assets with a field which is not set to any value, `GET` the assets resource and filter on most available fields. For example:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     $URL/archivist/v2/assets?attributes.arc_display_name!=*
```

Returns all assets which do not have `arc_display_name` or in which `arc_display_name` is empty.


## Asset OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/assetsv2.swagger.json" >}}
