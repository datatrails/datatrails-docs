---
title: "Identity and Access Management"
description: "RKVST IAM Concepts"
lead: "Setting Up Your RKVST Tenancy"
date: 2021-06-14T10:57:58+01:00
lastmod: 2021-06-14T10:57:58+01:00
draft: false
images: []
menu: 
  docs:
    parent: "overview"
weight: 5
toc: true
---

## Tenancies and Accounts

Each RKVST tenancy represents an organization, and each RKVST account represents an individual user. There may be multiple accounts within a tenancy if there are several members within an organization.

### How do I add users to my organization?

RKVST Invites make it easy to add accounts to your tenancy. 

As a [root user](https://docs.rkvst.com/docs/overview/core-concepts/#tenancies), create an invite and send it to the email address of the user you wish to add. 

When the invitee signs up for their RKVST account using the invited email address, they will be automatically added to your tenancy. 

{{< tabs name="invite_user_IAM" >}}
{{{< tab name="UI" >}}
On the Sidebar, select `Manage RKVST`.
{{< img src="ManageRKVST.png" alt="Rectangle" caption="<em>Select 'Manage RKVST'</em>" class="border-0" >}}

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
    -d '{"message": "personalised message", "email": "john.doe@example.com"}' \
    "https://app.rkvst.io/archivist/iam/v1/invites"
```

See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
{{< /tab >}}
{{< /tabs >}}

### Can I name my tenancy? 

There are two ways to name your RKVST tenancy. The first way is to add a `Tenant Display Name`. This name will be displayed only within your own tenancy. The display name makes it easy to identify which tencancy you're currently working in and to switch between tenancies if you are part of multiple. 

The second way to set your tenancy name is to [get your domain verified](../../beyond-the-basics/verified-domain) by the RKVST team. Your verified domain name will be visible to the people you share information with and will be publicly available if you create a Public Asset.