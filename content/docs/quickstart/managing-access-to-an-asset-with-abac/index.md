---
title: "Managing Access to an Asset With ABAC"
description: "Sharing Access within your Tenant"
lead: "Sharing Access within your Tenant"
date: 2021-05-18T15:33:03+01:00
lastmod: 2021-05-18T15:33:03+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 24
toc: true
---

{{< caution >}}
**Caution:** You will only have access to the `Access Policies` screen if you are a Root User in your Organization.
{{< /caution >}}

Attribute-Based Access Control (ABAC) policies can be used to control access to Assets, their Attributes, and Events within a single Organization. 

Specifically, ABAC policies are created by Root Users to share information with Non-Root Users in the same Tenancy.

ABAC policies can be granular, with users allowed to see only single Attributes at a time, if wished. 

It is possible to control policies based on types of Assets, their Location, and whether Users can read or write any information in an Asset.

By default, no Non-Root Users will see any existing Assets and Events unless a Root User explicitly creates an ABAC policy to allow it.

## Creating an ABAC Policy

Consider the Shipping Container Asset we created. There may be many people within an organization who need access to specific Attributes of the container.

We shall create a policy for someone who needs to share some standard dimensions of the Shipping Container, inspect the cargo, and create `Inspect` Events.

1. Create your Access Policy. 

{{< tabs name="access_policies_abac" >}}
{{{< tab name="UI" >}}
Navigate to the `Access Policies` section on the Sidebar of the RKVST Dashboard.
{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
In order to create an Access Policy using JSON format, create a file to store the details. We will execute a command to run the file in a later step. 
{{< /tab >}}}
{{< /tabs >}}

2. You may wish to view your existing policies before creating a new one. 

{{< tabs name="existing_policies_abac" >}}
{{{< tab name="UI" >}}
Here you will see any existing policies and can select `Add Policy`.
{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
You may view your existing policies before moving on to create your new policy by executing the following curl command. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.
```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/access_policies
```
{{< /tab >}}}
{{< /tabs >}}

3. Set the asset filters for your policy. 

{{< tabs name="asset_filters_abac" >}}
{{{< tab name="UI" >}}
When adding a Policy, you will see this form:
{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

Here you can apply policy filters to the correct Assets. In this case, we shall apply the policy to any Asset in the `UK Factory` Location created earlier, as well as the type of Asset (`Shipping Container`).

{{< img src="PolicyABACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Filters can use `and` or `or` to categorize assets.
```json
{
    "display_name": "Bill Inspect Policy",
    "filters": [
        { "or": [
            "attributes.arc_home_location_identity=UK Factory"
        ]},
        { "or": [
            "attributes.arc_display_type=Shipping Container"
        ]}
    ]
}
```
{{< /tab >}}}
{{< /tabs >}}

4. Next, enter the desired `Permissions` to set Users' Asset and Event attribute access. 

{{< tabs name="permissions_abac" >}}
{{{< tab name="UI" >}}
We select the `Permissions` Tab to set Users' Asset and Event attribute access policy.
{{< img src="PolicyABACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

In this example, the `User` actor implies an ABAC policy, identified by email. Type the relevant email address and hit Enter; you may also see a dropdown list of users within your tenancy.

{{< img src="PolicyABACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
In order to import a Subject using the base64 string, it will need to be decoded to access the `wallet_pub_key` and `tessera_pub_key` used in the next step. 
 ```bash
 echo $SUBJECT_STRING | base64 -d
 ```

To add users to the access policy using JSON, you will then need to retrieve their subject IDs using the [IAM Subjects API](https://docs.rkvst.com/docs/api-reference/iam-subjects-api/). Save the following to a JSON file with your desired subject information. 
```json
{
    "display_name": "Friendly Name",
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

5. Once all relevant details are complete, add the Permission Group to the policy. You may add multiple permission groups per policy if you wish. 
{{< tabs name="complete_policy_abac" >}}
{{{< tab name="UI" >}}
Enter desired permissions and select `Add Permission Group`. 
{{< img src="PolicyABACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}   

{{< /tab >}}
{{< tab name="JSON" >}}
Add the desired permissions and the subject ID found in the previous step. 
```json
{
    "display_name": "Bill Inspect Policy",
    "filters": [
        { "or": [
            "attributes.arc_home_location_identity=UK Factory"
        ]},
        { "or": [
            "attributes.arc_display_type=Shipping Container"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": ["arc_display_name", "arc_description", "arc_home_location_identity", "Length", "Weight"],
            "subjects": [
                "subjects/<subject-id>"
            ]
        }
    ]
}
```
{{< /tab >}}}
{{< /tabs >}}
    

Note we have included RKVST-sigificant attributes: `arc_display_name`, `arc_description`, and `arc_home_location_identity`.

`arc_*` attributes have special significance in RKVST; in this case, respectively, allowing visibility to the Name, Description, and Location of the Asset. Other `arc_*` attributes are also available.

6. Once complete, finish creating the Access Policy.

{{< tabs name="execute_policy_abac" >}}
{{{< tab name="UI" >}}
Select `Create Policy`.
{{< img src="PolicyABACSubmit.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}
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

7. Check the Asset is appropriately shared.

Bill should only be allowed to see the Asset's Name, Location, Length, and Weight Attributes.

{{< img src="PolicyABACBillView.png" alt="Rectangle" caption="<em>Bill's view as a Non-Root User</em>" class="border-0" >}}

For comparison with our Root User, Jill:

{{< img src="PolicyABACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

We can see that Bill can only view the Attributes specified in the policy. He can also see the Event where we updated the Location. 

Our Root User Jill, can see every detail associated with the Asset.
