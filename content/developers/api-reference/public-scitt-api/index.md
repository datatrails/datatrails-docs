---
title: "Public SCITT API (beta)"
description: "Public SCITT API (beta) Reference"
lead: "Public SCITT API (beta) Reference"
date: 2023-11-07T11:56:23+01:00
lastmod: 2023-11-07T11:56:23+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 112
toc: true
aliases: 
  - /docs/api-reference/public-scitt-api/
---
{{< note >}}
The public SCITT API is currently in beta.
{{< /note >}}

{{< note >}}
This page is primarily intended for developers who will be writing applications that will use RKVST for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/rkvst-official/workspace/rkvst-public-official/overview) or the [Developers](https://app.rkvst.io) section of the web UI. 

{{< /note >}}
## Public SCITT API Examples

The Public SCITT API is based on the draft SCITT architecture: https://github.com/ietf-wg-scitt/draft-ietf-scitt-architecture/blob/main/draft-ietf-scitt-architecture.md

While all RKVST events created by the Public SCITT API are public, in order to access the API an authorization token is needed.

To create the authorization token follow these instructions: [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Creating a Signed Statement

A statement is 'any serializable information about an Artifact.' https://github.com/ietf-wg-scitt/draft-ietf-scitt-architecture/blob/main/draft-ietf-scitt-architecture.md 

RKVST currently supports statements whose content-type is json and whose values are comprised of:
* string
* list of strings
* dictionary of strings

The statement is wrapped in a Cose_Sign1 envelope: https://www.rfc-editor.org/rfc/rfc8152.html#page-18

The Cose_Sign1 envelope protected header must include the following:

* Decentralised IDentifer (DID) Header: 391
* Feed Header: 392
* KID Header: 4

The DID header must correspond to a valid didweb identifier: https://w3c-ccg.github.io/did-method-web/

The KID header must correspond to the signing key used to sign the Cose_sign1 message

The Feed Header is 'a logical collection of Statements about the same Artifact.' https://github.com/ietf-wg-scitt/draft-ietf-scitt-architecture/blob/main/draft-ietf-scitt-architecture.

The Public half of the signing key must be available in the DID document, found at the address of the didweb identifier in the DID header.

{{< note >}}
RKVST verifies the Cose_Sign1 message signature using the DID header and KID header.
{{< /note >}}

### Registering a Signed Statement

Create a signed statement (see Creating a Signed Statement), base64 encode it and add it to the json body as follows:

```json
{
    "statement":"0oRYYqUBJgRHdGVzdGRpZANwYXBwbGljYXRpb24vanNvbhkBh3gvZGlkOndlYjphcHAuc29hay5zdGFnZS5qaXRzdWluLmlvOnN0YXRpYzpkaWR3ZWIZAYhsc3BlZWRvc2F1cnVzoFhheyJnbyBrYXJ0IjogInNwZWVkb3NhdXJ1cyIsICJ2YWx1ZSI6ICIzMDAwIiwgImV4Y2hhbmdlZCBmb3IiOiAiMTUwMCIsICJvd25lciI6ICJ0aGUtc3BlZWR5LWRpbm8ifVhAyqPxKGXFZMf1++5zZzgI9W7MSaL2u0afMnFMSUZdSFYYP2jofQapMc2LvD6vrDjR4CfNenLD1x3OJKO1wwm1SA=="
}
```

```bash
curl -v -X POST \
  -H "@$HOME/.rkvst/bearer-token.txt" \
  -H "Content-Type: application/json" \
  -d "@/path/to/jsonfile" \
  https://app.rkvst.io/archivist/v1/publicscitt/entries
```

```json
{
    "operationID": "assets_1b0a0829-98ca-4fef-a969-82288ee210b0_events_303d8f72-4c8b-474e-9333-27f958e1be96",
    "status": "running"
}
```

### Retrieving Operation Status

Registering a statement can take upto a couple of minutes, therefore to check on its status use the `operationID` returned in Registering a Signed Statement.


```bash
curl -v \
    -H "@$HOME/.rkvst/bearer-token.txt" \
    -H "Content-Type: application/json" \
    https://app.rkvst.io/archivist/v1/publicscitt/operations/assets_1b0a0829-98ca-4fef-a969-82288ee210b0_events_303d8f72-4c8b-474e-9333-27f958e1be96
```

```json
{
    "operationID": "assets_1b0a0829-98ca-4fef-a969-82288ee210b0_events_303d8f72-4c8b-474e-9333-27f958e1be96",
    "status": "succeeded",
    "entryID": "assets_1b0a0829-98ca-4fef-a969-82288ee210b0_events_303d8f72-4c8b-474e-9333-27f958e1be96"
}
```

### Retrieving Signed Statement

Once the statement has been registered, a counter signed statement can be retrieved using the `entryID` in Retrieving Operation Status.

{{< note >}}
The counter signed statement is returned in base64.

The counter signed statement is a Cose_Sign1 message.

The original signed statement is the payload of the counter signed statement, as a Cose_Sign1 message in CBOR. https://www.rfc-editor.org/rfc/rfc8949.html
{{< /note >}}

```bash
curl -v \
    -H "@$HOME/.rkvst/bearer-token.txt" \
    -H "Content-Type: application/json" \
    https://app.rkvst.io/archivist/v1/publicscitt/entries/assets_1b0a0829-98ca-4fef-a969-82288ee210b0_events_303d8f72-4c8b-474e-9333-27f958e1be96
```

```json
{
    "signedStatement": "0oRYaqMBOCIEWDZzY2l0dC1jb3VudGVyLXNpZ25pbmcvZDhiMjllNmQwZTdlNDM3NTgxZGVhZTI5ZDAzNzM5MGEZAYd4KGRpZDp3ZWI6YXBwLnJrdnN0LmlvOmFyY2hpdmlzdDp2MTpkaWR3ZWKgWQEM0oRYYqUBJgRHdGVzdGRpZANwYXBwbGljYXRpb24vanNvbhkBh3gvZGlkOndlYjphcHAuc29hay5zdGFnZS5qaXRzdWluLmlvOnN0YXRpYzpkaWR3ZWIZAYhsc3BlZWRvc2F1cnVzoFhheyJnbyBrYXJ0IjogInNwZWVkb3NhdXJ1cyIsICJ2YWx1ZSI6ICIzMDAwIiwgImV4Y2hhbmdlZCBmb3IiOiAiMTUwMCIsICJvd25lciI6ICJ0aGUtc3BlZWR5LWRpbm8ifVhAyqPxKGXFZMf1++5zZzgI9W7MSaL2u0afMnFMSUZdSFYYP2jofQapMc2LvD6vrDjR4CfNenLD1x3OJKO1wwm1SFhg1fIFTTCrcngIe0pRgzi9lDi4JSw+ds+sh65y0ooYPktjsHheLYSWhfW/d9/t9x8aaln52AEOvCNXeFk+4+NomhI4Cztyh11807piNKorElhlaAuJtojZjD0vz4Bs098F"
}
```

### Retrieving Receipt

Once the statement has been registered, a receipt can be retrieved using the `entryID` in Retrieving Operation Status.

{{< note >}}
The receipt is returned in base64.

The receipt is a Cose_Sign1 message.

The receipt proof is the payload of the receipt.
{{< /note >}}

```bash
curl -v \
    -H "@$HOME/.rkvst/bearer-token.txt" \
    -H "Content-Type: application/json" \
    https://app.rkvst.io/archivist/v1/publicscitt/entries/assets_1b0a0829-98ca-4fef-a969-82288ee210b0_events_303d8f72-4c8b-474e-9333-27f958e1be96/receipt
```

```json
{
    "receipt": "0oRYbqQBOCIEWDZzY2l0dC1jb3VudGVyLXNpZ25pbmcvZDhiMjllNmQwZTdlNDM3NTgxZGVhZTI5ZDAzNzM5MGEZAYYAGQGHeChkaWQ6d2ViOmFwcC5ya3ZzdC5pbzphcmNoaXZpc3Q6djE6ZGlkd2VioFmiX3siYXBwbGljYXRpb25fcGFyYW1ldGVycyI6eyJhcHBfaWQiOiIiLCJhcHBfY29udGVudF9yZWYiOiIiLCJlbGVtZW50X21hbmlmZXN0IjpbInNpbXBsZWhhc2giXSwibW9ub3RvbmljX3ZlcnNpb24iOjB9LCJibG9jayI6IjB..."
}
```

### Verifying the Receipt

A receipt can be verified offline using the 'rkvst-receipt-scitt' script. https://pypi.org/project/rkvst-receipt-scitt/

## Public SCITT OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/dev/jgough/8732-scitt-dev-docs/doc/openapi/publicscittv1.swagger.json" >}}
