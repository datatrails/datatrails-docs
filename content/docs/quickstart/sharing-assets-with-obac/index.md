---
title: "Sharing Assets With OBAC"
description: "Sharing Access outside your Tenant"
lead: "Sharing Access outside your Tenant"
date: 2021-05-18T15:33:31+01:00
lastmod: 2021-05-18T15:33:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 25
toc: true
---

{{< caution >}}
**Caution:** You will only have access to the `Access Policies` screen if you are a Root User in your organization.
{{< /caution >}}

{{< warning >}}
**Warning:** To use OBAC, you will need to share with an external organization.
{{< /warning >}}

Organization-Based Access Control (OBAC) policies have a lot in common with Attribute-Based Access Control (ABAC) policies; they apply the same controls with two different classes of Actor.

Where they differ is that OBAC shares only with Root Users of an External Organization; the External Root User must then apply ABAC to establish appropriate access for their own organization's Non-Root Users.

## Adding External Organizations to Allow Sharing

In order to share Assets and their details with another Organization or Tenant, we must first import the ID of the External Organization.


### Finding Your Own ID

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and your Organization's ID will be contained within the `Self` box.

This string is the one you should share with a 3rd Party who wants to share their data with you.

{{< img src="PolicyOBACSubjectSelf.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

### Importing another Organization's ID

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Import Subject.

{{< tabs name="add_subject_OBAC" >}}
{{{< tab name="UI" >}}
Select the Subjects Tab and then `Import Subject`.
{{< img src="PolicyOBACSubjectImport.png" alt="Rectangle" caption="<em>Importing a Subject</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}

{{< note >}}
**Note:** Note: By default, newly created Applications will always have a Non-Root User permission to the API. You must add the Application as a Root User to elevate it’s permissions.

You can add an App Registration as a Root User using the Manage RKVST screen, where the issuer will be `https://app.rkvst.io/appidpv1` and the subject will be your App Registration’s `CLIENT_ID`.
{{< /note >}}

The RKVST YAML runner is executed as a series of steps, each step representing a single operation with an `action`.

In order to create an subject, we use the action `SUBJECTS_CREATE_FROM_B64`.
 
```yaml
---
steps:
  - step:
      action: SUBJECTS_CREATE_FROM_B64
```
{{< /tab >}}}
{{< /tabs >}}



3. Add the `Subject String` and `Name`/`subject_label`. `Subject String` is the ID of the Organization with which you wish to share Asset evidence. The `Name` is a friendly name for you to label the imported organization.

{{< tabs name="add_subject_string_OBAC" >}}
{{{< tab name="UI" >}}
You will be presented with a form to input your `Subject String` and `Name`. 
{{< img src="PolicyOBACSubjectAdd.png" alt="Rectangle" caption="<em>Adding the Subject</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
`subject_label` is not required, but must be present to reference the subject in later actions. 

```yaml
---
steps:
  - step:
      action: SUBJECTS_CREATE_FROM_B64
      description: Import a subjects entity.
      print_response: true
      subject_label: Example Subject
    display_name: Example Subject
    subject_string: >-
      eyJpZGVudGl0eSI6ICJzdWJqZWN0cy8wMDAwMDAwMC0wMDAwLTAwMDAtMDA
      wMC0wMDAwMDAwMDAwMDAiLCAiZGlzcGxheV9uYW1lIjogIlNlbGYiLCAid2
      FsbGV0X3B1Yl9rZXkiOiBbIjA0YzExNzNiZjc4NDRiZjFjNjA3Yjc5YzE4Z
      GIwOTFiOTU1OGZmZTU4MWJmMTMyYjhjZjNiMzc2NTcyMzBmYTMyMWEwODgw
      YjU0YTc5YTg4YjI4YmM3MTBlZGU2ZGNmM2Q4MjcyYzUyMTBiZmQ0MWVhODM
      xODhlMzg1ZDEyYzE4OWMiXSwgIndhbGxldF9hZGRyZXNzIjogWyIweDk5Rm
      E0QUFCMEFGMkI1M2YxNTgwODNEOGYyNDRiYjQ1MjMzODgxOTciXSwgInRlc
      3NlcmFfcHViX2tleSI6IFsiZWZkZzlKMFFoU0IyZzRJeEtjYVhnSm1OS2J6
      cHhzMDNGRllJaVlZdWVraz0iXSwgInRlbmFudCI6ICIiLCAiY29uZmlybWF
      0aW9uX3N0YXR1cyI6ICJDT05GSVJNQVRJT05fU1RBVFVTX1VOU1BFQ0lGSU
      VEIn0=
```
{{< /tab >}}}
{{< /tabs >}}



## Creating an OBAC Policy

OBAC creation uses many of the same steps, filters, controls, and forms as ABAC Policies.

It is possible to mix-and-match ABAC and OBAC Permission Groups in the same policy if you so wish.

1. Navigate to the `Access Policies` section on the Sidebar of the RKVST Dashboard.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Here you will see any existing policies, select `Add Policy`.

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a policy the following form will appear:

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can begin applying filters to your Policy for the right assets. In this case, we're going to filter for any Assets in the `UK Factory` Location created earlier.

{{< img src="PolicyOBACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Next, we select the `Permissions` Tab to set which Organizations can read and write certain Asset attributes, as well as Event visibility.

{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In our case, we want the `Organization` actor, which implies OBAC. Type the Friendly Name of the Organization we wish to share with into the box and we should see a prepopulated drop-down search.

{{< note >}} **Note:** You will need to have imported another Organization's ID before you can specify a policy to share information with that Organization. {{< /note >}}

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. When the relevant controls are in place, we then add the Permission Group to the policy.

Note we have included RKVST-significant atributes: `arc_display_name` and `arc_display_type` which brings visibility to the Name and Type of Asset being shared. 

{{< img src="PolicyOBACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete, submit the policy and check the Asset is shared appropriately; Mandy should only be able to see the Name and Type of Asset as well as the Asset's custom `Weight` attribute.

{{< img src="PolicyOBACMandyView.png" alt="Rectangle" caption="<em>Mandy's view as a Root User of the External Organization</em>" class="border-0" >}}

By comparison, our Root User, Jill, can see the full details of the Asset:

{{< img src="PolicyOBACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

9. If Mandy wishes to share what she can to Non-Root Users within her organization, it is her responsibility to create an ABAC Policy as she would any other Asset she has access to.

There are many possible fine-grained controls and as such ABAC and OBAC Policy Creation is an extensive topic. To find out more, head over to the [IAM Policies API Reference](../../api-reference/iam-policies-api/).
