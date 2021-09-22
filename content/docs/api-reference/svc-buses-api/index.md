---
title: "Service Bus API"
description: "Service Bus API Reference"
lead: "Service Bus API Reference"
date: 2021-06-09T14:22:12+01:00
lastmod: 2021-06-09T14:22:12+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 111
toc: true
---

## Service Bus API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-client-secret) and store in a file in a secure local directory with 0600 permissions.

Set the URL (for example):

```bash
export URL=https://app.rkvst.io 
```

### Service Bus Sources Creation

The `svcbussources` endpoint allows subscribing to an Azure Service Bus Queue and receiving events when a device changes state. 

The state changes are then recorded in the RKVST system.

{{< warning >}}
**Warning:** The connection string used is for the servicebus and not for the `servicebus` queue.
{{< /warning >}}

Define the svcbussource parameters and store in `/path/to/jsonfile`:

```json
{
    "display_name": "RKVST",
    "connection_string": "Endpoint=sb://rkvst-dev.servicebus.windows.net/;SharedAccessKeyName=rkvst-listener;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "queue_name": "rkvst-listener"
}
```

Post to the endpoint:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    $URL/archivist/v1/svcbussources
```

The response is:

```json
{
    "identity": "svcbussources/08838336-c357-460d-902a-3aba9528dd22",
    "display_name": "RKVST",
    "queue_name": "rkvst-listener"
}
```

### Service Bus Sources Deletion

The `svcbussources` endpoint allows subscribing to the Azure Service Bus Queue and receiving events when a device changes state. 

The state changes are recorded in the RKVST system.

Delete the endpoint:

```bash
curl -v -X DELETE \
    -H "@$BEARER_TOKEN_FILE" \
    $URL/archivist/v1/svcbussources/08838336-c357-460d-902a-3aba9528dd22
```

The response is:

```json
{
    "identity": "svcbussources/08838336-c357-460d-902a-3aba9528dd22",
    "display_name": "RKVST",

}
```

## Service Bus OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/svcbussourcesv1.swagger.json" >}}