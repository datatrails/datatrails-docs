---
title: "Identity and Access Management"
description: "RKVST IAM Concepts"
lead: "Setting Up Your RKVST Tenancy"
date: 2021-06-14T10:57:58+01:00
lastmod: 2021-06-14T10:57:58+01:00
draft: false
images: []
menu: 
  platform:
    parent: "administration"
weight: 41
toc: true
aliases: 
  - /docs/overview/identity-and-access-management/
---

## Tenancies and Accounts

Each RKVST Tenancy represents an organization, and each RKVST account represents an individual user. There may be multiple accounts within a Tenancy if there are several members within an organization. Additionally, an indivudual user can be part of multiple Tenancies. 

### How do I add users to my organization?

RKVST Invites make it easy to add accounts to your tenancy. 

As an [administrator](/platform/overview/core-concepts/#tenancies), create an invite and send it to the email address of the user you wish to add. 

When the invitee signs up for their RKVST account using the invited email address, they will be automatically added to your Tenancy. 

{{< tabs name="invite_user_IAM" >}}
{{{< tab name="UI" >}}
On the Sidebar, select `Settings`.
{{< img src="Settings.png" alt="Rectangle" caption="<em>Select 'Settings'</em>" class="border-0" >}}

Choose the `USERS` tab, then click `INVITE NEW USER`.
{{< img src="InviteButton.png" alt="Rectangle" caption="<em>Invite New User</em>" class="border-0" >}}

Fill in the desired email and custom message. To finish, select `SEND INVITE`. 
{{< img src="InviteForm.png" alt="Rectangle" caption="<em>Enter Desired Details</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
This action is not yet available in the YAML Runner. Check out our UI or curl command options!
{{< /tab >}}
{{< tab name="CURL" >}}
Fill in your desired details and run the command to send the invite. 
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d '{"message": "Join my RKVST tenancy!", "email": "user@rkvst.com"}' \
    "https://app.rkvst.io/archivist/iam/v1/invites"
```

See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.
{{< /tab >}}
{{< /tabs >}}

### Can I name my tenancy? 

#### Tenant Display Name

There are two ways to name your RKVST Tenancy. The first way is to add a `Tenant Display Name`. This name will be displayed only within your own Tenancy, and will not be visible to outside organizations. The display name makes it easy to identify which Tencancy you're currently working in and to switch between Tenancies if you are part of multiple Tenancies.

To set your `Tenant Display Name`: 

1. On the Sidebar, select `Settings`.
{{< img src="Settings.png" alt="Rectangle" caption="<em>Select 'Settings'</em>" class="border-0" >}}

2. Add your desired name, then click `CHANGE DISPLAY NAME`.
{{< img src="TenantDisplay.png" alt="Rectangle" caption="<em>Change Display Name</em>" class="border-0" >}}

#### Verified Domain 

The second way to set your tenancy name is to [get your domain verified](/platform/administration/verified-domain/) by the RKVST team. Your verified domain name will be visible to the people you share information with and will be publicly available if you create a Public Asset.

## Enterprise Single Sign-On

[Enterprise customers](https://www.rkvst.com/pricing/) may use their preferred Identity Provider (IDP) to sign-on to RKVST. Before doing so, you must have a [Verified Domain](/platform/administration/verified-domain/).

1. Navigate to `Settings` on the sidebar and select `Tenancy`.

Enter your SSO configuration, then select `SAVE ENTERPRISE SSO CONFIG`. Saving your configuration may take a moment.

{{< img src="ESSOForm.png" alt="Rectangle" caption="<em>Configure SSO</em>" class="border-0" >}}

{{< note >}}
**NOTE:** To retrieve the necessary data for the configuration form, your IDP must be configured to be compatible with RKVST. Enter the information below.

**Login URI:**
```
https://app.rkvst.io/login
```

**Callback URL:**
```
https://b2carchivistprod3.b2clogin.com/b2carchivistprod3.onmicrosoft.com/oauth2/authresp
```

{{< /note >}}

<br/>

2. Now that your details are saved, return to the RKVST sign-in screen. Select the `Single Sign-On` option. 

{{< img src="SSOLogInButton.png" alt="Rectangle" caption="<em>Single Sign-On</em>" class="border-0" >}}

3. Enter your [Verified Domain Name](/platform/overview/identity-and-access-management/#verified-domain). 

{{< img src="DomainName.png" alt="Rectangle" caption="<em>Verified Domain</em>" class="border-0" >}}

You will be sent to the identity provider you configured earlier to log-in, then redirected back to RKVST.