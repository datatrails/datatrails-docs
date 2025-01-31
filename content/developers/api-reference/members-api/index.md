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
weight: 121
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

### Promoting a user to 'OWNER' role in a tenancy

You can manage the roles of a user (i.e. promoting or demoting them with the 'OWNER' role) by
PATCHing their membership record. 
With the identity of the tenant member record corresponding to the user in question, submit this request
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

When a user should no longer have access to your tenant, you can deactivate them programatically 
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

{{< note >}}
User roles are stripped when a user is deactivated, so upon reactivation the user will only have basic user rights. If required once reactivated, follow the steps above to promote this user to 'Owner' role.
{{< /note >}}

## Members OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/membersv1.swagger.json" >}}<br>

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/main/doc/membershipsv1.swagger.json" >}}
