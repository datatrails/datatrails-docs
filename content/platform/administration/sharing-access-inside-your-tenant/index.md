---
title: "Managing Internal Access to Your Tenant"
description: "Sharing Access to Audit Trails within your Tenant"
lead: "Sharing Access to Audit Trails within your Tenant"
date: 2021-05-18T15:33:03+01:00
lastmod: 2021-05-18T15:33:03+01:00
draft: false
images: []
menu:
  platform:
    parent: "administration"
weight: 43
toc: true
aliases:
  - ../quickstart/managing-access-to-an-asset-with-abac
  - /docs/rkvst-basics/managing-access-to-an-asset-with-abac/
  - /platform/administration/managing-access-to-an-asset-with-abac/
---

{{< caution >}}
**Caution:** You will only have access to the `Access Policies` screen if you are an Administrator in your organization.
{{< /caution >}}

Attribute-Based Access Control (ABAC) policies can be used to control access to Assets, their attributes, and Events within a single organization.

Specifically, ABAC policies are created by Administrators to share information with Non-Administrators in the same Tenancy.

ABAC policies can be granular, with users only allowed to see single attributes at a time.

It is possible to control policies based on types of Assets, their location, and whether Users can read or write any information in an Asset.

By default, no Non-Administrators will see any existing Assets and Events unless an Administrator explicitly creates an ABAC policy to allow it.

{{< note >}}
**Note:** To create an ABAC policy, first [add users to your tenancy](/platform/administration/identity-and-access-management/#how-do-i-add-users-to-my-organization).
{{< /note >}}

## Creating an ABAC Policy
{{< note >}}
**Note:** Access polices are applied to the Asset. This means that when a policy is created or updated an Event will be recorded in the audit trail of matching Assets from the Actor `Archivist Internal`.
{{< /note >}}
Consider the Shipping Container Asset we created. There may be many people within an organization who need access to specific attributes of the container.

We shall create a policy for someone who needs to share some standard dimensions of the Shipping Container, inspect the cargo, and create `Inspect` Events.

1. You may wish to view your existing policies before creating a new one.
{{< tabs name="existing_policies_abac" >}}
{{{< tab name="UI" >}}
Navigate to the `Access Policies` section on the sidebar of the DataTrails dashboard.
Here you will see any existing policies and can select `Create Policy`.
{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Creating a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
You may view your existing policies before creating your new policy by executing the following curl command. See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/iam/v1/access_policies
```

{{< /tab >}}}
{{< /tabs >}}

1. Create your Access Policy.
{{< tabs name="access_policies_abac" >}}
{{{< tab name="UI" >}}
Select `Create Policy`.
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

1. Set the asset filters for your policy
{{< tabs name="asset_filters_abac" >}}
{{{< tab name="UI" >}}
When adding a policy, you will see this form:
{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

Here you can apply policy filters to the correct Assets. In this case, we shall apply the policy to any Asset with the type `Shipping Container`.

{{< img src="PolicyABACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
Filters can use `and` or `or` to categorize Assets. You may also use filters on attribute values, such as `=` and `!=` for equal and not equal, respectively. These can be used for specific attribute values, or to check if the value exists at all. For example, to filter for Assets not associated with a location, you could use:

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
            "attributes.your_custom_attribute=Your Value>"
        ]},
        { "or": [
            "attributes.arc_home_location_identity=locations/<location-id>"
        ]},
        { "or": [
            "attributes.arc_display_type=Shipping Container"
        ]}
    ]
}
```
[See here for instructions on finding your location ID.](/platform/administration/grouping-assets-by-location/)
{{< note >}}
**Note** We will not use the custom attribute any further as we build the example.
{{< /note >}}
{{< /tab >}}}
{{< /tabs >}}

1. Enter the desired `Permissions` to set user's Asset and Event attribute access
{{< tabs name="permissions_abac" >}}
{{{< tab name="UI" >}}
We select the `Permissions` Tab to set Users' Asset and Event attribute access policy.
{{< img src="PolicyABACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

In this example, the `User` actor is identified by email. Type the relevant email address and hit enter; you may also see a dropdown list of users within your tenancy.

{{< img src="PolicyABACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}
There are a few ways you may add a `User` to your Access Policy using JSON. One way is to use the email address associated with their DataTrails account. To do so, add the desired `user_attributes` to the `access_permissions` section.

{{< note >}}
**Note** You may grant access to specific attachments by specifying the corresponding key in the `access_permissions`.
{{< /note >}}

```json
 "access_permissions": [
        {
            "asset_attributes_read": ["arc_display_name", "arc_display_type", "arc_primary_image", "length", "weight"],
            "user_attributes": [
               {"or": ["email=user@email.com"]}
            ]
        }
    ]
```

You may also grant permissions to an [App Registration](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) within your tenancy. App Registrations are non-root by default; best practice is to use ABAC policies to preserve Principle of Least Privilege.  

```json
 "access_permissions": [
        {
            "asset_attributes_read": ["arc_display_name", "arc_display_type", "arc_primary_image", "length", "weight"],
            "user_attributes": [
               {"or": ["subject=<client-id>"]}
            ]
        }
    ]
```

{{< note >}}
**Note:** This is different from adding `subjects` as a key in your `access_permissions`, for example, when adding an external Subject ID to an OBAC policy. The user attribute `subject` refers to the Client ID associated with an App Registration.
{{< /note >}}

Additionally, you may set permissions based on the Custom Claims of an [App Registration](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) using JSON Web Tokens (JWTs). To do so, you must include the prefix `jwt_` followed by the desired claim as one of the `user_attributes` in the policy. For example, the key `jwt_app_reg_role` to match on claim `app_reg_role`.

 ```json
  "access_permissions": [
         {
             "asset_attributes_read": ["arc_display_name", "arc_display_type", "arc_primary_image",, "length", "weight"],
             "user_attributes": [
                {"or": ["jwt_app_reg_role=tracker"]}
             ]
         }
     ]
 ```

{{< /tab >}}}
{{< /tabs >}}

1. Once all relevant details are complete, add the permission group to the policy. You may add multiple permission groups per policy if you wish.<br><br>Here we are restricting Mandy to viewing the `Name`, `Type`, `Image`, `length` and `weight` of Shipping Containers currently located at the UK Factory. She cannot modify the container record and she cannot see the full Audit Trail of Events because she only needs to know that the container does not exceed the maximum length and weight.
{{< tabs name="complete_policy_abac" >}}
{{{< tab name="UI" >}}
Enter desired permissions and select `Add Permission Group`
{{< img src="PolicyABACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="JSON" >}}
Add the desired permissions and the desired `user_attributes`

```json
{
    "display_name": "Mandy Inspect Policy",
    "filters": [
        { "or": [
            "attributes.arc_display_type=Shipping Container"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": ["arc_display_name", "arc_display_type", "arc_primary_image", "length", "weight"],
            "user_attributes": [
                {"or": ["email=mandy@datatrails.ai"]}
            ]
        }
    ]
}
```

{{< /tab >}}}
{{< /tabs >}}<br>
{{< note >}}
**Note:** We have included DataTrails-significant attributes: `arc_display_name`, `arc_display_type` and `arc_primary_image`
`arc_*` attributes have special significance in DataTrails.  
In this case, respectively, allowing visibility to the `Name`, `Type`, and `Image` of the Asset. Other `arc_*` attributes are also available.
{{< /note >}}
1. Once complete, finish creating the Access Policy.
{{< tabs name="execute_policy_abac" >}}
{{{< tab name="UI" >}}
Select `Create Policy`.
{{< img src="PolicyABACSubmit.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="JSON" >}}fo
Use the curl command to run your JSON file! See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/iam/v1/access_policies
```

{{< /tab >}}}
{{< /tabs >}}

1. Check the Asset is appropriately shared  

    Mandy should only be allowed to see the Asset's name, type, image, length, and weight attributes.
{{< img src="PolicyABACMandyView.png" alt="Rectangle" caption="<em>Mandy's view as a Non-Administrator</em>" class="border-0" >}}

    For comparison with our Administrator, Jill who can see everything:
{{< img src="PolicyABACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Administrator</em>" class="border-0" >}}

We can see that Mandy can only view the Attributes specified in the policy.

Our Administrator, Jill, can see every detail associated with the Asset.
