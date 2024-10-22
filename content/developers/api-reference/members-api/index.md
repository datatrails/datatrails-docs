---
title: "Members API"
description: "Members API Reference"
lead: "Members API Reference"
date: 2021-06-09T13:29:57+01:00
lastmod: 2021-06-09T13:29:57+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 114
toc: true
aliases: 
  - /docs/api-reference/members-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}

## Members API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### Listing members of your tenant

To fetch the list of members, simply `GET` the `/members` resource

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/iam/v1/members
```

By default this doesn't show members that are deactivated. You can filter the list to include 
deactivated users:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/iam/v1/members?member_state=MEMBER_STATE_BOTH
```

### Promoting a member of your tenant

You can manage the roles of a user (i.e. promoting or demoting them by way of the 'OWNER' role) by
PATCHing their record. With the identity of a member in your tenant to hand, submit this request
to set their roles to a list containing only 'OWNER'. To demote the member, simply send an empty
list.

```bash
curl -v -X PATCH \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "{'roles': ['OWNER']}" \
    https://app.datatrails.ai/archivist/iam/v1/{member_identity}
```

### Deactivating a member of your tenant

When a user should no longer have access to your tenant, you can deactivate them progamatically 
using the following API call:

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    https://app.datatrails.ai/archivist/iam/v1/{member_identity}:deactivate
```

and then re-activate them like so:

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    https://app.datatrails.ai/archivist/iam/v1/{member_identity}:activate
```

## Members OpenAPI Docs

Coming soon ...

<!-- {{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/membersv1.swagger.json" >}}<br>

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/membershipsv1.swagger.json" >}} -->
