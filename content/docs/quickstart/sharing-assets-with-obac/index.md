---
title: "Sharing Assets With OBAC"
description: ""
lead: ""
date: 2021-05-18T15:33:31+01:00
lastmod: 2021-05-18T15:33:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 6
toc: true
---


{{< caution >}}
**Caution:** You will only have access to the "Manage Policies" screen if you 
   are a Root User in your organization.
{{< /caution >}}

{{< warning >}}
**Warning:** To use OBAC you will need to share with an external organization.
{{< /warning >}}

ABAC and OBAC have a lot in common; they apply the same controls with two different classes of Actor.

Where they differ is that OBAC shares only with Root Users of an External Organization; an External Root User must then apply ABAC to establish appropriate access for their own organization's Non-Root Users.

Adding External Organizations
-----------------------------

In order to share Assets and their details with another Organization or Tenant we must first import the organizational Subject ID

Creating an OBAC Policy
-----------------------

OBAC creation uses many of the same steps, filters, controls, and forms as ABAC Policies.

It is possible to mix-and-match ABAC and OBAC in the same policy if you so wish.

1. Navigate to the 'Manage Policies' section on the Sidebar of the RKVST Dashboard

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Here you will see any existing policies and select 'Add Policy'

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a Policy the following form will appear

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can begin applying filters to your Policy for the right assets, in this case we're going to set Policy for any Assets in the 'UK Factory' Location we created earlier

{{< img src="PolicyOBACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Next we select the 'Permissions' Tab to set which Organizations can read and write certain Asset attributes, as well as Events visibility

{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In our case we want the 'Organization' actor to imply OBAC then we can type into the box the name of the Organization and we should have a drop-down search prepopulated

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. Once we have completed all of the relevant details we then add the Permisson Group to the policy, you may add multiple permission groups per policy if you wish, note we have included the values `arc_display_name` and `arc_display_type`; `arc_` values are special value in RKVST, in this case they refer to the Name and Description of the Asset which will not be visible otherwise 

{{< img src="PolicyOBACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete we submit the policy and check the Asset is shared appropriately; Mandy should only be able to see the Asset's weight attribute

{{< img src="PolicyOBACMandyView.png" alt="Rectangle" caption="<em>Mandy's view as a Root User of the External Organization</em>" class="border-0" >}}

For comparison with our Root User, Jill:

{{< img src="PolicyOBACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

We can see that Mandy is able to view the Weight Attribute as specified in the policy whereas Jill can see every Asset Attribute.

If Mandy wished to then share what she could see as a Root User within her organization to Non-Root Users, it is her responsibility to create an ABAC Policy as she would any other asset.

ABAC and OBAC Policy setting is an extensive topic, there are many possible fine-grained controls. To find out more, head over to the IAM Policies Section.
