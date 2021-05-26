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

   The Root User is typically the account which has signed in first.
```

``` 
💡 To use OBAC you will need an external organization to share with. 
   
   If you are evaluating RKVST the following may not be immediately relevant 
   but is still important to understand.
```

ABAC and OBAC have a lot in common, they both apply the same controls but to two different classes of Actor.

Where the two differ is that OBAC is for sharing only with the Root Users of an External Organization, the External Root Users will then apply ABAC to share access to their own Non-Root Users themselves.

The External Root Users will only have access to the information you have chosen to share, it is their responsibility to assign further controls to that information within their organization.

Adding External Organisations
-----------------------------

In order to share Assets and their details with another Organization or Tenant we must first import them as Subjects

Creating an OBAC Policy
-----------------------

In much the same way as ABAC policies many of the steps for OBAC creation use the same filters, controls and forms.

In fact you can actually mix-and-match ABAC and OBAC in the same policy if you so wish.

1. Navigate to the 'Manage Policies' section on the Sidebar of the RKVST Dashboard

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Here you should be able to see any existing policies and you should also be able to select 'Add Policy'

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a Policy the following form will appear

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can begin applying the filters you wish to apply so that your policy affects the right assets, in this case we're going to apply the policy to any assets in the 'UK Factory' Location we created earlier

.. image:: PolicyFilter.png

5. Next if we select the 'Permissions' Tab we should be able to set which Organizations can read and write which asset attributes, as well as which events they can see or not

.. image:: PolicyABACform.png

6. In our case we want the 'Organization' actor to imply OBAC then we can type into the box the name of the Organization and we should have a drop-down search prepopulated

.. image: PolicyOBACcreate.png

7. Once complete we can submit the policy and check the asset has been shared appropriately, when Mandy checks her account she should only be able to see the Asset's weight attribute

.. image:: PolicyOBACMandyview.png

For comparison with our Root User Jill:

.. image:: PolicyOBACJillview

We can see that Mandy is able to view the Weight Attribute as specified in the policy where as Jill can see everything on the Asset.

ABAC and OBAC Policy making is an extensive topic, there are many fine grained controls you can put in. To find out more about them, head over to the IAM Policies Section.
