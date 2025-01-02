---
title: "Integrating with n8n"
description: "Integrating DataTrails Authentication and Workflows with n8n"
lead: "Integrating DataTrails Authentication and Workflows with n8n"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "integrations"
weight: 10
toc: true
aliases:
---
[n8n](https://n8n.io/) is a workflow automation platform with visual editing capabilities.

Integrating DataTrails with n8n is easy, utilizing OAuth2 credentials and the [DataTrails API Reference](/developers/api-reference/) documentation.

## Authentication & Credentials

DataTrails uses an OAuth2 provider, making it easy to integrate client credentials into n8n.

1. Create a new [DataTrails Access Token](/developers/developer-patterns/getting-access-tokens-using-app-registrations/), saving the `Client_ID` and `Client_Secret`
1. Create a new [n8n Credential](https://docs.n8n.io/credentials/), clicking the [+] button on the workflow designer.
1. Choose "OAuth2 API" from the app services list
   {{< img src="credentials-auth-type.png" alt="Credential Flow" caption="" class="border-0" >}}
1. Name the credential for reference within the workflow
   {{< img src="credentials-connection.png" alt="Credential Configuration" caption="" class="border-0" >}}
1. **Grant Type**: select "Client Credentials"
1. **Access Token URL**: set to:
   ```http
   https://app.datatrails.ai/archivist/iam/v1/appidp/token
   ```
1. **Client ID**: set to the DataTrails `Client_ID` from step 1
1. **Client Secret**: set to the DataTrails `Client_Secret` from step 1
1. **Save** the credential configuration and close the dialog

## Executing DataTrails APIs

To execute a DataTrails API:

1. Add a new n8n node
   {{< img src="http-node.png" alt="HTTP Node" caption="<em>Add an HTTP node</em>" class="border-0" >}}
1. Select the HTTP node
1. **Authentication**: select "Generic Credential Type"
   {{< img src="http-node-configuration.png" alt="HTTP Node Configuration" caption="<em>HTTP Node Configuration</em>" class="border-0" >}}
1. **Generic Auth Type**: select "OAuth2 API"
1. **OAuth2 API**: select the named credential from the previous step
1. **URL**: configure using the [DataTrails API Reference](/developers/api-reference/) documentation
1. **Query Parameters**: configure per the API docs

### More Info:

- [DataTrails API Reference](/developers/api-reference/)
- [n8n Documentation](https://docs.n8n.io/)
- [vCon Templates](/developers/templates/vcons)
