---
title: "Assign Users to RKVST for Interactive Use"
description: ""
lead: ""
date: 2021-06-16T11:11:21+01:00
lastmod: 2021-06-16T11:11:21+01:00
draft: false
images: []
menu: 
  docs:
    parent: "setup-and-administration"
weight: 3
toc: true
---

To enable access for individual users to your Jitsuin RKVST:

* Assign Users to the Jitsuin RKVST Enterprise application.
* Grant assigned users the appropriate Jitsuin RKVST roles.

This Microsoft Guide provides the general details for [assigning users](https://docs.microsoft.com/bs-latn-ba/azure/active-directory/manage-apps/assign-user-or-group-access-portal) and
their roles.

## Locate your Jitsuin RKVST Enterprise Application

Having completed admin consent, locate the enterprise application principals for your Jitsuin RKVST. 

There will be two `Homepage URLs` which match the FQDN for the link you received. 

The URL for the root resource is your API principal, this is where roles are assigned to users and non-interactive clients.

{{< img src="userdocs_aad_enterprise_applications.png" alt="Rectangle" caption="<em>Azure Enterprise Applications</em>" class="border-0" >}}

{{< note >}}
**Note:** The /webgate principal authorizes your Jitsuin RKVST deployment to act on your users behalf. It needs no further configuration.
{{< /note >}}

Select the principal with the Homepage URL matching your link.

{{< img src="userdocs_aad_select_principal.png" alt="Rectangle" caption="<em>Selecting Your Principle</em>" class="border-0" >}}

2. Check that User Assignment is required for your Jitsuin RKVST

{{< warning >}}
The `User Assignment Required` setting must be `yes` in order to restrict access to particular users in your directory. 

If it is set to `no` any user at your organisation will be able to login.
{{< /warning >}}


{{< img src="userdocs_aad_check_user_assignment.png" alt="Rectangle" caption="<em>Verify User Assignment</em>" class="border-0" >}}

3. Add user to the Enterprise Application

{{< img src="userdocs_aad_add_user.png" alt="Rectangle" caption="<em>Adding a User</em>" class="border-0" >}}

4. Select the user for role assignment

{{< img src="userdocs_aad_select_user.png" alt="Rectangle" caption="<em>Selecting a User Role</em>" class="border-0" >}}