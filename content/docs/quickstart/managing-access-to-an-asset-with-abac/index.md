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
weight: 5
toc: true
---

``` 
💡 You will only have access to the 'Manage Policies' screen if you are a 
Root User in your organization. 
    
The Root User is typically the account which has signed in first. 
```

Attribute Based Access Control can be used to control access to Assets, their attributes and events within an organisation. Specifically, ABAC policies are created by Root Users to then share information with Non-Root Users in the same Tenancy.

ABAC policies can be extremely granular, with users being allowed to see only single attributes at a time if wished. It is also possible to control which types of Assets that policies can be applied to, the location and whether Users can either read or write any of the information in an Asset.

By default all non-root Users are on a standard DENY ALL policy, which means they will be unable to see any existing assets and corresponding events unless a Root User explicitly allows them to.

Creating an ABAC Policy
-----------------------

Consider the Shipping Container Asset we have created so far, internally in the Organisation there may be many people who need access to specific attributes of the container.

If we consider a usecase where someone internally needs to understand the cargo and some standard dimensions of the Shipping Container for inspection we can create a policy that specifically shares those qualities.

We may also need to give permission for that user to create Inspect events.

1. Navigate to the 'Manage Policies' section on the Sidebar of the RKVST Dashboard

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Here you should be able to see any existing policies and you should also be able to select 'Add Policy'

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a Policy the following form will appear

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can begin applying the filters you wish to apply so that your policy affects the right assets, in this case we're going to apply the policy to any assets in the 'UK Factory' Location we created earlier, as well as the type of Asset ('Shipping Container')

{{< img src="PolicyABACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Next if we select the 'Permissions' Tab we should be able to set which Users can read and write which asset attributes, as well as which events they can see or not

{{< img src="PolicyABACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In our case we want the 'User' actor to imply ABAC and we want them identified by email, then we can type the email address into the box and hit Enter, you may also see a dropdown list of users within your tenancy

{{< img src="PolicyABACUSers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. Once we have completed all of the relevant details we then add the Permisson Group to the policy, you may add multiple permission groups per policy if you wish, note we have included the values `arc_display_name`, `arc_description` and `arc_home_location_identity`; `arc_` values are special value in RKVST, in this case they refer to the Name and Description of the Asset which will not be visible otherwise 

{{< img src="PolicyABACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete we can select 'Create Policy' and check the asset has been shared appropriately

{{< img src="PolicyABACSubmit.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}

When Bill checks his account he should only be able to see the Asset's Length and Weight Attributes as well as the name of the asset and it's location

{{< img src="PolicyABACBillView.png" alt="Rectangle" caption="<em>Bill's view as a Non-Root User</em>" class="border-0" >}}

For comparison with our Root User Jill:

{{< img src="PolicyABACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

We can see that Bill is only able to view the Attributes as specified in the policy, he can also see the event where we updated the Location as well. Jill, however, as a Root User can see every detail associated with the Asset.
