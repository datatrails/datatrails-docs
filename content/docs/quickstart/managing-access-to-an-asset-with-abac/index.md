---
title: "Managing Access to an Asset With ABAC"
description: ""
lead: ""
date: 2021-05-18T15:33:03+01:00
lastmod: 2021-05-18T15:33:03+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 6
toc: true
---

{{< caution >}}
**Caution:** You will only have access to the `Access Policies` screen if you are a Root User in your Organization.
{{< /caution >}}

Attribute Based Access Control (ABAC) policies can be used to control access to Assets, their Attributes and Events within a single Organization. 

Specifically, ABAC policies are created by Root Users to then share information with Non-Root Users in the same Tenancy.

ABAC policies can be granular, with users allowed to see only single Attributes at a time if wished. 

It is possible to control policies based on types of Assets, their Location, and whether Users can read or write any information in an Asset.

By default, all Non-Root Users will not see any existing Assets and Events unless a Root User explicitly creates an ABAC policy to allow it.

## Creating an ABAC Policy

Consider the Shipping Container Asset we created. There may be many people within an organization who need access to specific Attributes of the container.

We shall create a policy for someone who needs to share some standard dimensions of the Shipping Container, inspect the cargo and create `Inspect` Events.

1. Navigate to the `Access Policies` section on the Sidebar of the RKVST Dashboard.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Here you will see any existing policies and can select `Add Policy`.

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When adding a Policy you will see this form:

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can apply policy filters to the correct Assets.

In this case, we shall apply the policy to any Asset in the `UK Factory` Location created earlier, as well as the type of Asset (`Shipping Container`).

{{< img src="PolicyABACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Next, we select the `Permissions` Tab to set Users' Asset and Event attribute access policy.

{{< img src="PolicyABACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In this example, the `User` actor implies an ABAC policy, identified by email. Type the relevant email address and hit Enter; you may also see a dropdown list of users within your tenancy.

{{< img src="PolicyABACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. Once all relevant details are complete, then add the Permission Group to the policy. You may add multiple permission groups per policy if you wish. 

Note we have included RKVST-sigificant attributes: `arc_display_name`, `arc_description`, and `arc_home_location_identity`.

`arc_*` attributes have special significance in RKVST; in this case respectively allowing visibility to the Name, Description, and Location of the Asset. Other `arc_*` attributes are also available.

{{< img src="PolicyABACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete, select `Create Policy` and check the Asset is appropriately shared.

{{< img src="PolicyABACSubmit.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}

Bill should only be allowed to see the Asset's Name, Location, Length, and Weight Attributes.

{{< img src="PolicyABACBillView.png" alt="Rectangle" caption="<em>Bill's view as a Non-Root User</em>" class="border-0" >}}

For comparison with our Root User, Jill:

{{< img src="PolicyABACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

We can see that Bill can only view the Attributes as specified in the policy. He can also see the Event where we updated the Location. 

Our Root User Jill, can see every detail associated with the Asset.
