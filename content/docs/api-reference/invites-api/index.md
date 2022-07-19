---
title: "Invites API"
description: "Invites API Reference"
lead: "Invites API Reference"
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
## Invites API Examples

Invites can be used to invite a new user into a tenancy to access assets and events.

For example, inviting a new member of the organization into their organization's tenancy.

By default invited users will have no permissons, so need to be given access to manage specific assets and events using [ABAC policies](../../rkvst-basics/managing-access-to-an-asset-with-abac/index.md) defined by a Root User.

For sharing assets and events to other organizations and tenancies externally check out our tutorial on [OBAC policies](../../rkvst-basics/sharing-assets-with-obac/index.md) or the [IAM Policies API Reference](../iam-policies-api/index.md).

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.
### Invite Creation

To create an invite you need at least the invitee's email address; once created it will be considered pending, once accepted the invite itself will be deleted.

It is possible to add an optional custom message:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d '{"message": "personalised message", "email": "john.doe@example.com"}' \
    "https://app.rkvst.io/archivist/iam/v1/invites"
```

The response is:

```json
{
  "identity": "invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb",
  "message": "personalised message",
  "email": "john.doe@example.com",
  "expiry_time": "2022-06-17T11:30:43Z"
}
```

### Invite Retrieval

If you know the unique identity of a pending invite, `GET` the resource:

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    "https://app.rkvst.io/archivist/iam/v1/invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb"
```

The response is:

```json
{
  "identity": "invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb",
  "message": "personalised message",
  "email": "john.doe@example.com",
  "expiry_time": "2022-06-17T11:30:43Z"
}
```

### Retrieve All Invites

To fetch all pending invites, simply `GET` the `/invites` resource:

```bash
curl -v -X GET \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    "https://app.rkvst.io/archivist/iam/v1/invites"
```

The response is:

```json
{
  "invites": [
    {
      "identity": "invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb",
      "message": "personalised message",
      "email": "john.doe@example.com",
      "expiry_time": "2022-06-17T11:30:43Z"
    },
    {
      "identity": "invites/f4e4b1b5-8186-4feb-9072-9999f89d4619",
      "message": "another personalised message",
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
    -H "@$BEARER_TOKEN_FILE" \`
    -H "Content-type: application/json" \
    "https://app.rkvst.io/archivist/iam/v1/invites/bbbaeab8-539d-4482-9a98-f1285e7f75cb"
```

The response will be empty.


## Invites OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/invitesv1.swagger.json" >}}