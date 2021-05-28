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


``` 
💡 You will only have access to the "Manage Policies" screen if you 
   are a Root User in your organization. 

   The first account created by an organization is automatically a Root User.
```

``` 
💡 To use OBAC you will need to share with an external organization.
   
   If you are evaluating RKVST the following may not be immediately relevant 
   but is still important to understand.
```

ABAC and OBAC have a lot in common; they apply the same controls with two different classes of Actor.

Where they differ is OBAC establishes sharing with Root Users of an External Organization; an External Root User will then apply ABAC to establish appropriate access for their own organization Non-Root Users.

Adding External Organisations
-----------------------------

In order to share Assets and their details with another Organization or Tenant we must first import them as Subjects

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

.. image:: PolicyFilter.png

5. Next we select the 'Permissions' Tab to set which Organizations can read and write certain Asset attributes, as well as Events visibility

.. image:: PolicyABACform.png

6. In our case we want the 'Organization' actor to imply OBAC then we can type into the box the name of the Organization and we should have a drop-down search prepopulated

.. image: PolicyOBACcreate.png

7. Once complete we submit the policy and check the Asset is shared appropriately; Mandy should only be able to see the Asset's weight attribute

.. image:: PolicyOBACMandyview.png

For comparison with our Root User, Jill:

.. image:: PolicyOBACJillview

We can see that Mandy is able to view the Weight Attribute as specified in the policy whereas Jill can see every Asset Attribute.

ABAC and OBAC Policy setting is an extensive topic, there are many possible fine-grained controls. To find out more, head over to the IAM Policies Section.
