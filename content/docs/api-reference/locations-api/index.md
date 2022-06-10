---
title: "Locations API"
description: "Locations API Reference"
lead: "Locations API Reference"
date: 2021-06-09T11:56:23+01:00
lastmod: 2021-06-09T11:56:23+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 111
toc: true
---

## Locations API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Location Creation

Define the location parameters and store in `/path/to/jsonfile`:

```json
{
   "display_name": "Macclesfield, Cheshire",
   "description": "Manufacturing site, North West England, Macclesfield, Cheshire",
   "latitude": 53.2546799,
   "longitude": -2.1213956,
   "attributes": {
       "director": "John Smith",
       "address": "Unit 6A, Synsation Park, Maccelsfield",
       "Facility Type": "Manufacture",
       "support_email": "support@macclesfield.com",
       "support_phone": "123 456 789"
    }
}
```

Create the location to POSTing to the locations resource:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/v2/locations
```

The response is:

```json
{
    "identity": "locations/08838336-c357-460d-902a-3aba9528dd22",
    "display_name": "Macclesfield, Cheshire",
    "description": "Manufacturing site, North West England, Macclesfield, Cheshire",
    "latitude": 53.2546799,
    "longitude": -2.1213956,
    "attributes": {
        "director": "John Smith",
        "address": "Bridgewater, Somerset",
        "Facility Type": "Manufacture",
        "support_email": "support@macclesfield.com",
        "support_phone": "123 456 789"
    }
}
```

### Location Retrieval


#### Fetch All Locations
To fetch all locations, simply `GET` the locations resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/locations
```

#### Fetch Specific Location by Identity

If you know the unique identity of the location record, simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/locations/08838336-c357-460d-902a-3aba9528dd22
```

#### Fetch Location by Name

To fetch all locations with a specific name, `GET` the assets resource and filter on `display_name`:

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    https://app.rkvst.io/archivist/v2/locations?display_name=Macclesfield%2C%20Cheshire
```

Each of these calls returns a list of matching asset records in the form:

```json
{
    "locations": [
        {
            "identity": "locations/08838336-c357-460d-902a-3aba9528dd22",
            "display_name": "Macclesfield, Cheshire",
            "description": "Manufacturing site, North West England, Macclesfield, Cheshire",
            "latitude": "53.2546799",
            "longitude": "-2.1213956,14.54",
            "attributes": {
                "director": "John Smith",
                "address": "Bridgewater, Somerset",
                "Facility Type": "Manufacture",
                "support_email": "support@macclesfield.com",
                "support_phone": "123 456 789"
            }
        }
    ]
}
```

## Locations OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/locationsv2.swagger.json" >}}
