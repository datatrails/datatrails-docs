---
title: "Microsoft IoTHub API"
description: "Microsoft IoTHub API Reference"
lead: "Microsoft IoTHub API Reference"
date: 2021-06-09T14:00:29+01:00
lastmod: 2021-06-09T14:00:29+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 109
toc: true
---

## Microsoft IoTHub API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Set the URL (for example):

```bash
export URL=https://app.rkvst.io 
```

### IoTHub GDR Creation

The `iothubgdr` endpoint allows to import all devices from selected Azure IoT Hub into RKVST.

Define the `iothubgdr` parameters and store in `/path/to/jsonfile`:

```json
{
    "display_name": "RKVST",
    "secret": "Endpoint=sb://iothub-ns-test-org-1-1637462-0dd952fad8.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx;EntityPath=test-org-1",
    "arc_home_location_identity": "locations/47b575c0-ff0f-11e9-8f0b-362b9e155667"
}
```

And post to the endpoint:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v2/iothubgdr
```

You should see the following responses:

```json
{
    "identity": "iothubgdr/08838336-c357-460d-902a-3aba9528dd22",
    "done": false,
    "timestamp_accepted": "2019-11-07T15:31:49Z",
    "timestamp_finished": null,
    "result": {
        "display_name": "RKVST",
        "number_assets_imported": 0,
        "arc_home_location_identity": "locations/47b575c0-ff0f-11e9-8f0b-362b9e155667",
        "status": "STATUS_PENDING"
    }
}
```

Or in case of error:

```json
{
    "identity": "iothubgdr/08838336-c357-460d-902a-3aba9528dd22",
    "done": true,
    "timestamp_accepted": "2019-11-07T15:31:49Z",
    "timestamp_finished": "2019-11-07T15:31:55Z",
    "error": {
        "display_name": "RKVST",
        "number_assets_imported": 0,
        "arc_home_location_identity": "locations/47b575c0-ff0f-11e9-8f0b-362b9e155667",
        "error_message": "invalid secret provided"
    }
}
```

### IoTHub GDR Management

The `iothubgdr` endpoint allows to query and manage recent imports.

#### Listing All Imports

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    $URL/archivist/v2/iothubgdr
```

This call will respond with a list containing all known imports. Individual items in list are identical to create Responses

#### Listing Specific Imports

To get specific import details you need the identity of the import, for example:

```bash
iothubgdr/47b58286-ff0f-11e9-8f0b-362b9e155667
```
Which can be used in the following request following request:

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    $URL/archivist/v2/iothubgdr/47b58286-ff0f-11e9-8f0b-362b9e155667
```

#### Cancel IoTHub GDR Import Job

To cancel running import issue the following request:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    $URL/archivist/v2/iothubgdr/47b58286-ff0f-11e9-8f0b-362b9e155667:cancel
```

The response status should be set to `STATUS_CANCELLED`.

#### Delete an Import

To delete an import issue the following request:

```bash
curl -v -X DELETE \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    $URL/archivist/v2/iothubgdr/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The import will be deleted from tracked imports but the underlying job will not stop. To stop the job cancel it before deleting.

Response to successful deletion is empty `{}`.

## Microsoft IoTHub OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/iothubgdrv2.swagger.json" >}}
