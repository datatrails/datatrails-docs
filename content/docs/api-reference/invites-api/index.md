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

Invites can be used by a Root User to invite someone into the secure boundary of their tenancy to internally access their assets and events. 

By default invited users will have no permissons, so need to be given access to manage specific assets and events using [ABAC policies](../../quickstart/managing-access-to-an-asset-with-abac/index.md) defined by a Root User.

For sharing assets and events to other organizations and tenancies externally check out our tutorial on [OBAC policies](../../quickstart/sharing-assets-with-obac/index.md) or the [IAM Policies API Reference](../iam-policies-api/index.md).

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### TITLE HERE


## Invites OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/invitesv1.swagger.json" >}}