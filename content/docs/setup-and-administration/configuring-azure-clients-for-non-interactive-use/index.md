---
title: "Configuring Azure Clients for Non-Interactive Use"
description: ""
lead: ""
date: 2021-06-16T11:12:25+01:00
lastmod: 2021-06-16T11:12:25+01:00
draft: false
images: []
menu: 
  docs:
    parent: "setup-and-administration"
weight: 4
toc: true
---

To enable non-interactive access to Jitsuin RKVST APIs:

* Create an Application Registration in your Azure Active Directory.
* Grant an API access permission for the registration referring to the Jitsuin RKVST API
* Create a Client Secret

{{< note >}}
**Note:** Certificate based assertion of identity is fully supported. See `client_assertion_type` and `client_assertion` in the official [Azure Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-oauth2-client-creds-grant-flow>).
{{< /note >}}

## Create an Application Registration

{{< img src="api-app-new-registration.png" alt="Rectangle" caption="<em>Adding a New App Registration</em>" class="border-0" >}}

* Choose any name you like.
* Account type should be: `Accounts in this Organizational Directory Only`
* `Redirect URI` - leave blank.

{{< img src="api-app-new-registration-name-and-account-type.png" alt="Rectangle" caption="<em>Adding a New App Registration</em>" class="border-0" >}}

The [Microsoft Quickstart Register App](https://docs.microsoft.com/bs-latn-ba/azure/active-directory/develop/quickstart-register-app) guide covers the general process.

## Add an API Permission to the Application registration

Your app registration must be granted access to the Jitsuin RKVST API.

{{< img src="api-app-permissions-apis-my-org-uses.png" alt="Rectangle" caption="<em>Adding an App Permission from 'APIs my Organization uses'</em>" class="border-0" >}}

`Application Permissions` will enable access to the Jitsuin RKVST API using client secrets or certificates.

{{< img src="api-app-permissions-request-apis.png" alt="Rectangle" caption="<em>Selecting 'App Permissions'</em>" class="border-0" >}}

The [Microsoft Quickstart Configure Web App Access](https://docs.microsoft.com/bs-latn-ba/azure/active-directory/develop/quickstart-configure-app-access-web-apis) guide covers the general process; For non-interactive use see `Application Permissions`.

## Enable the desired Jitsuin RKVST roles

{{< img src="api-app-permissions-roles.png" alt="Rectangle" caption="<em>Assigning the Permission Roles</em>" class="border-0" >}}

## Grant Administrator consent for the new Application Registration

{{< img src="api-app-permissions-grant-consent.png" alt="Rectangle" caption="<em>Granting Consent</em>" class="border-0" >}}

If successful you should see the following:

{{< img src="api-app-permissions-grant-consent-success.png" alt="Rectangle" caption="<em>Success!</em>" class="border-0" >}}

## Add a Client Secret to the Application Registration

{{< img src="api-app-certificates-and-secrets-2.png" alt="Rectangle" caption="<em>Adding a Client Secret or Certificate</em>" class="border-0" >}}

Take note of the client secret and the application object id (`UUID`).

{{< note >}}
**Note:** If you need to have different secrets for different Jitsuin RKVST roles create an application registration for each distinct set of roles.
{{< /note >}}

