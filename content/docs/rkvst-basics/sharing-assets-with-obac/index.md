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
    parent: "rkvst-basics"
weight: 36
toc: true
aliases:
  - ../quickstart/sharing-assets-with-obac
---

{{< caution >}}
**Caution:** You will only have access to the `Access Policies` screen if you are an Administrator in your organization.
{{< /caution >}}

{{< warning >}}
**Warning:** To use OBAC you will need to share with an external organization.
{{< /warning >}}

Organization-Based Access Control (OBAC) policies have a lot in common with Attribute-Based Access Control (ABAC) policies; they apply the same controls with two different classes of actor.

Where they differ is that OBAC shares only with Administrators of an external organization. The external Administrator must then apply ABAC to establish appropriate access for their own organization's Non-Administrators.

## Adding External Organizations to Allow Sharing

In order to share Assets and their details with another organization or Tenancy, we must first import the ID of the external organization.

### Finding Your Own ID

1. As an Administrator, navigate to `Access Policies`.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and your Organization's ID will be contained within the `Self` box.

This string is the one you should share with a 3rd Party who wants to share their data with you.

{{< img src="PolicyOBACSubjectSelf.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

### Importing another Organization's ID

1. Use the organization's ID to create a new Subject.

{{< tabs name="import_subject_obac" >}}
{{{< tab name="UI" >}}
As an Administrator, navigate to `Access Policies`.
{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
In order to import a Subject using the base64 string, it will need to be decoded to access the `wallet_pub_key` and `tessera_pub_key` used in the next step. 
```bash
echo $SUBJECT_STRING | base64 -d
```
{{< /tab >}}}
{{< /tabs >}}

2. Select the Subjects Tab and then `Import Subject`.

{{< tabs name="import_subject_id_obac" >}}
{{{< tab name="UI" >}}
Select the Subjects Tab and then `Import Subject`.
{{< img src="PolicyOBACSubjectImport.png" alt="Rectangle" caption="<em>Importing a Subject</em>" class="border-0" >}}

You will be presented with a form; the `Subject String` is the ID of the organization you wish to share Asset evidence with. The `Name` is a friendly name for you to label the imported organization.

{{< img src="PolicyOBACSubjectAdd.png" alt="Rectangle" caption="<em>Adding the Subject</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
To add users to the access policy using JSON, you will first need to retrieve their subject IDs using the [IAM Subjects API](https://docs.rkvst.com/docs/api-reference/iam-subjects-api/).

Save the following to a JSON file with your desired subject information. 
```json
{
    "display_name": "Friendly Name",
    "wallet_pub_key": ["key1"],
    "tessera_pub_key": ["key2"]
}
```
Execute the file, which will return the subject identity in the form `subjects/<subject-id>` to be used in your Access Policy. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/subjects
```
{{< /tab >}}}
{{< /tabs >}}

{{< note >}}
**Note:** To accept a subject import request, both organizations must have imported the other's Subject ID. This acknowledges that the organizations wish to share with each other. Once both organizations have accepted, there will be a blue symbol next to their subject name. 
{{< /note >}}

## Creating an OBAC Policy

OBAC creation uses many of the same steps, filters, controls, and forms as ABAC Policies.

It is possible to mix-and-match ABAC and OBAC Permission Groups in the same policy if you so wish.

1. Create your Access Policy. 

{{< tabs name="access_policies_obac" >}}
{{{< tab name="UI" >}}
Navigate to the `Access Policies` section on the sidebar of the RKVST dashboard.
{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Create an empty file, in later steps we will add the correct JSON.
```json
{

}
```
{{< /tab >}}}
{{< /tabs >}}

2. You may wish to view your existing policies before creating a new one. 

{{< tabs name="existing_policies_obac" >}}
{{{< tab name="UI" >}}
Here you will see any existing policies and can select `Add Policy`.
{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
You may view your existing policies before creating your new policy by executing the following curl command. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/access_policies
```
{{< /tab >}}}
{{< /tabs >}}

3. Set the asset filters for your policy. 

{{< tabs name="asset_filters_obac" >}}
{{{< tab name="UI" >}}
When adding a policy, you will see this form:
{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

Here you can apply policy filters to the correct Assets. In this case, we shall apply the policy to any Asset in the `UK Factory` location created earlier, as well as the type of Asset (`Shipping Container`).

{{< img src="PolicyOBACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Filters can use `and` or `or` to categorize assets. You may also use filters on attribute values, such as `=` and `!=` for equal and not equal, respectively. These can be used for specific attribute values, or to check if the value exists at all. For example, to filter for Assets not associated with a location, you could use:

```json
"attributes.arc_home_location_identity!=*"
```

The `*` is a wildcard that could represent any value. This will match not only on string values, but list and map values as well. 

Following our Shipping Container example, this is how we would set our Asset filters:
```json
{
    "display_name": "Mandy Inspect Policy",
    "filters": [
        { "or": [
            "attributes.arc_home_location_identity=locations/<location-id>"
        ]},
        { "or": [
            "attributes.arc_display_type=Shipping Container"
        ]}
    ]
}
```

[See here for instructions on finding your location ID.](https://docs.rkvst.com/docs/rkvst-basics/grouping-assets-by-location/)
{{< /tab >}}}
{{< /tabs >}}

4. Next, enter the desired `Permissions` to set Users' Asset and Event attribute access. 

{{< tabs name="permissions_obac" >}}
{{{< tab name="UI" >}}
We select the `Permissions` tab to set users' Asset and Event attribute access policy.
{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

In our case, we want the `Organization` actor, which implies OBAC. Type the friendly name of the organization you wish to share with into the box and there should be a prepopulated drop-down search.

{{< note >}} **Note:** You will need to have imported another Organization's ID before you can specify a policy to share information with that 0rganization. 
{{< /note >}}

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
To add an organization to the access policy, you will first need to retrieve their Subject IDs using the [IAM Subjects API](https://docs.rkvst.com/docs/api-reference/iam-subjects-api/).

Save the following to a JSON file with your desired subject information. 
```json
{
    "display_name": "Friendly name",
    "wallet_pub_key": ["key1"],
    "tessera_pub_key": ["key2"]
}
```
Execute the file, which will return the subject identity in the form `subjects/<subject-id>` to be used in your access policy. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/subjects
```
{{< /tab >}}}
{{< /tabs >}}

5. Once all relevant details are complete, add the permission group to the policy. You may add multiple permission groups per policy if you wish. 

{{< tabs name="complete_policy_obac" >}}
{{{< tab name="UI" >}}
Enter desired permissions and select `Add Permission Group`. 
{{< img src="PolicyOBACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="JSON" >}}
Add the desired permissions and the Subject ID found in the previous step. 
```json
{
    "display_name": "Mandy Inspect Policy",
    "filters": [
        { "or": [
            "attributes.arc_home_location_identity=locations/<location-id>"
        ]},
        { "or": [
            "attributes.arc_display_type=Shipping Container"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": ["Weight", "arc_display_name", "arc_display_type"],
            "subjects": [
                "subjects/<subject-id>"
            ]
        }
    ]
}
```
{{< /tab >}}}
{{< /tabs >}}

Note we have included RKVST-sigificant attributes: `arc_display_name` and `arc_display_type`.

`arc_*` attributes have special significance in RKVST. In this case, respectively, allowing visibility to the Name and Type of the Asset. Other `arc_*` attributes are also available.

6. Once complete, finish creating the Access Policy.

{{< tabs name="finish_policy_obac" >}}
{{{< tab name="UI" >}}
Select `Create Policy`.
{{< img src="PolicyOBACPermissions.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="JSON" >}}
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/access_policies

```
{{< /tab >}}}
{{< /tabs >}}

7. Once complete, check the Asset is shared appropriately; Mandy should only be able to see the Name and Type of Asset as well as the Asset's custom `Weight` attribute.

{{< img src="PolicyOBACMandyView.png" alt="Rectangle" caption="<em>Mandy's view as an Administrator of the External Organization</em>" class="border-0" >}}

By comparison, our Administrator, Jill, can see the full details of the Asset:

{{< img src="PolicyOBACJillView.png" alt="Rectangle" caption="<em>Jill's view as an Administrator</em>" class="border-0" >}}

8. If Mandy wishes to share what she can to Non-Administrators within her organization, it is her responsibility to create an ABAC Policy as she would any other Asset she has access to.

There are many possible fine-grained controls and as such ABAC and OBAC Policy Creation is an extensive topic. To find out more, head over to the [IAM Policies API Reference](../../api-reference/iam-policies-api/).