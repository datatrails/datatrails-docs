---
title: "Invites API"
description: "Invites API Reference"
lead: "Invites API Reference"
date: 2021-06-09T11:56:23+01:00
lastmod: 2021-06-09T11:56:23+01:00
draft: false
images: []
menu:
  developers:
    parent: "api-reference"
weight: 111
toc: true
aliases: 
  - /docs/api-reference/invites-api/
---
{{< note >}}
This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-official/workspace/datatrails-public-official/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## Invites API Examples

Invites can be used to invite a new user into a Tenancy to access Assets and Events.

For example, inviting a new member of the organization into their organization's tenancy.

By default, invited users will have no permissions and need to be given access to manage specific Assets and Events using [ABAC policies](/platform/administration/managing-access-to-an-asset-with-abac/) defined by an Administrator.

For sharing Assets and Events to other organizations and tenancies externally, check out our tutorial on [OBAC policies](/platform/administration/sharing-assets-with-obac/) or the [IAM Policies API Reference](../iam-policies-api/).

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

{{< note >}}
See [here](/platform/administration/identity-and-access-management/#how-do-i-add-users-to-my-organization) for additional instructions on inviting users to your Tenancy.
{{< /note >}}

### Invite Creation

To create an invite you need at least the invitee's email address. Once created, it will be considered pending and once accepted the invite itself will be deleted.

It is possible to add an optional custom message:

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d '{"message": "personalized message", "email": "john.doe@example.com"}' \
    "https://app.datatrails.ai/archivist/iam/v1/invites"
```

The response is:

```json
{
  "identity": "invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb",
  "message": "personalized message",
  "email": "john.doe@example.com",
  "expiry_time": "2022-06-17T11:30:43Z"
}
```

### Invite Retrieval

If you know the unique identity of a pending invite, `GET` the resource:

```bash
curl -v -X GET \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    "https://app.datatrails.ai/archivist/iam/v1/invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb"
```

The response is:

```json
{
  "identity": "invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb",
  "message": "personalized message",
  "email": "john.doe@example.com",
  "expiry_time": "2022-06-17T11:30:43Z"
}
```

### Retrieve All Invites

To fetch all pending invites, simply `GET` the `/invites` resource:

```bash
curl -v -X GET \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    "https://app.datatrails.ai/archivist/iam/v1/invites"
```

The response is:

```json
{
  "invites": [
    {
      "identity": "invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb",
      "message": "personalized message",
      "email": "john.doe@example.com",
      "expiry_time": "2022-06-17T11:30:43Z"
    },
    {
      "identity": "invites/f4e4b1b5-8186-4feb-9072-9999f89d4619",
      "message": "another personalized message",
      "email": "jane.doe@example.com",
      "expiry_time": "2022-06-17T11:30:26Z"
    },
  ],
  "next_page_token": ""
}
```

### Invite Deletion

To delete a pending invite, issue the following request:

```bash
curl -v -X DELETE \
    -H "@$HOME/.datatrails/bearer-token.txt" \`
    -H "Content-type: application/json" \
    "https://app.datatrails.ai/archivist/iam/v1/invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb"
```

The response will be empty.

## Invites OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/archivist-docs-old/master/doc/openapi/invitesv1.swagger.json" >}}
