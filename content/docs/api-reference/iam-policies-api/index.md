---
title: "IAM Policies API"
description: "IAM Policies API Reference"
lead: "IAM Policies API Reference"
date: 2021-06-09T12:02:15+01:00
lastmod: 2021-06-09T12:02:15+01:00
draft: false
images: []
menu:
  docs:
    parent: "api-reference"
weight: 108
toc: true
---

## IAM Policies API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

An [ABAC](https://docs.rkvst.com/docs/quickstart/managing-access-to-an-asset-with-abac/) policy is used to share permissions with non-root users within your tenancy. A non-root user could be a user who has been added using the [Invites API](../invites-api/) or could be an App Registration used for client credentials, which are created as non-root by default.

To create an ABAC Policy, you should use the `user_attributes` keyword. Specify `email` for invited users, and `subject`, using the client-id of your credentials, for App Registrations. 

You may also set permissions based on the Custom Claims of an [App Registration](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) using JSON Web Tokens (JWTs). To do so, you must include the prefix `jwt_` followed by the desired claim as one of the `user_attributes` in the policy. For example, the key `jwt_app_reg_role` to match on claim `app_reg_role`.

An [OBAC](https://docs.rkvst.com/docs/quickstart/sharing-assets-with-obac/) policy is used to share with the root users of an external organization.

To begin sharing with OBAC you must first import your collaborator's Organization ID using either the [IAM Subjects API](../iam-subjects-api/) or the instructions in the [basics section](../../quickstart/sharing-assets-with-obac/#importing-another-organizations-ids).

This will return a `subjects/<UUID>` object you would then specify with the `subjects` keyword to make it an OBAC policy.

{{< note >}}
**Note:** To accept a subject import request, both organizations must have imported the other's Subject ID. This acknowledges that the organizations wish to share with each other.
{{< /note >}}

As both ABAC and OBAC use the same filter syntax it is possible to have a mix of internal and external sharing within a single policy.

{{< note >}}
Learn more about [ABAC](https://docs.rkvst.com/docs/rkvst-basics/managing-access-to-an-asset-with-abac/) and [OBAC](https://docs.rkvst.com/docs/rkvst-basics/sharing-assets-with-obac/) policies in our RKVST Basics guides.
{{< /note >}}

### IAM Policy Creation

The following example shows how you can mix the `user_attributes` keyword for ABAC and `subjects` keyword for OBAC.

Define the access_policies parameters and store in `/path/to/jsonfile`:

```json
{
    "display_name": "Friendly name of the policy",
    "description": "Description of the policy",
    "filters": [
        { "or": [
            "attributes.arc_home_location_identity=locations/5ea815f0-4de1-4a84-9377-701e880fe8ae",
            "attributes.arc_home_location_identity=locations/27eed70b-9e2b-4db1-b8c4-e36505350dcc"
        ]},
        { "or": [
            "attributes.arc_display_type=Valve",
            "attributes.arc_display_type=Pump"
        ]},
        { "or": [
            "attributes.ext_vendor_name=SynsationIndustries"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": [ "toner_colour", "toner_type" ],
            "asset_attributes_write":["toner_colour"],
            "behaviours": [ "Attachments", "RecordEvidence" ],
            "event_arc_display_type_read": ["toner_type", "toner_colour"],
            "event_arc_display_type_write": ["toner_replacement"],
            "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
            "subjects": [
                "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
            ],
            "user_attributes": [
                {"or": ["group:maintainers", "group:supervisors"]}
            ]
        }
    ]
}
```
Create the access policy:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/access_policies
```

The response is:

```json
{
    "identity": "access_policies/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "display_name": "Friendly name of the policy",
    "description": "Description of the policy",
    "filters": [
        {"or": [
            "attributes.arc_home_location_identity=locations/5ea815f0-4de1-4a84-9377-701e880fe8ae",
            "attributes.arc_home_location_identity=locations/27eed70b-9e2b-4db1-b8c4-e36505350dcc"
        ]},
        {"or": [
            "attributes.arc_display_type=Valve",
            "attributes.arc_display_type=Pump"
        ]},
        {"or": [
            "attributes.ext_vendor_name=SynsationIndustries"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": [ "toner_colour", "toner_type" ],
            "asset_attributes_write":["toner_colour"],
            "behaviours": [ "Attachments", "RecordEvidence" ],
            "event_arc_display_type_read": ["toner_type", "toner_colour"],
            "event_arc_display_type_write": ["toner_replacement"],
            "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
            "subjects": [
                "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
            ],
            "user_attributes": [
                {"or": ["group:maintainers", "group:supervisors"]}
            ]
        }
    ]
}
```

### IAM Policy Retrieval

IAM access policy records in RKVST are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
access_policies/12345678-90ab-cdef-1234-567890abcdef
```
If you do not know the `access_policy` identity you can fetch IAM access policy records using other information you do know, such as the `access_policy` name.

#### Fetch all IAM access_policies (v1)

To fetch all IAM `access_policies` records, simply `GET` the `iam/access_policies` resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/access_policies
```

#### Fetch specific IAM access Policy by identity (v1)

If you know the unique identity of the IAM access policy Record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/access_policies/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch IAM Access Policies by name (v1)

To fetch all IAM `access_policies` with a specific name, `GET` the `iam/access_policies` resource and filter on `display_name`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/iam/v1/access_policies?display_name=Some%20description"
```
Each of these calls returns a list of matching IAM access_policies records in the form:

```json
{
    "access_policies": [
        {
            "identity": "access_policies/6a951b62-0a26-4c22-a886-1082297b063b",
            "display_name": "Name to display",
            "description": "Description of the policy",
            "filters": [
                {"or": [
                    "attributes.arc_home_location_identity=locations/5ea815f0-4de1-4a84-9377-701e880fe8ae",
                    "attributes.arc_home_location_identity=locations/27eed70b-9e2b-4db1-b8c4-e36505350dcc"
                ]},
                {"or": [
                    "attributes.arc_display_type=Valve",
                    "attributes.arc_display_type=Pump"
                ]},
                {"or": [
                    "attributes.ext_vendor_name=SynsationIndustries"
                ]}
            ],
            "access_permissions": [
                {
                    "asset_attributes_read": [ "toner_colour", "toner_type" ],
                    "asset_attributes_write":["toner_colour"],
                    "behaviours": [ "Attachments", "RecordEvidence" ],
                    "event_arc_display_type_read": ["toner_type", "toner_colour"],
                    "event_arc_display_type_write": ["toner_replacement"],
                    "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
                    "subjects": [
                        "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                        "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
                    ],
                    "user_attributes": [
                        {"or": ["group:maintainers", "group:supervisors"]}
                    ]
                }
            ]
        },
        {
            "identity": "access_policies/12345678-0a26-4c22-a886-1082297b063b",
            "display_name": "Some other description",
            "filters": [
                {"or": ["attributes.arc_display_type=door_access_reader"]}
            ],
            "access_permissions": [
                {
                    "asset_attributes_read": [ "toner_colour", "toner_type" ],
                    "asset_attributes_write":["toner_colour"],
                    "behaviours": [ "Attachments", "RecordEvidence" ],
                    "event_arc_display_type_read": ["toner_type", "toner_colour"],
                    "event_arc_display_type_write": ["toner_replacement"],
                    "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
                    "subjects": [
                        "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                        "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
                    ],
                    "user_attributes": [
                        {"or": ["group:maintainers", "group:supervisors"]}
                    ]
                }
            ]
        }
    ]
}
```
### IAM Policy Deletion

To delete an IAM access policy, issue following request:

```bash
curl -v -X DELETE \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    https://app.rkvst.io/archivist/iam/v1/access_policies/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The response is:

```json
{}
```

### IAM Policy Update

Define the `access_policies` parameters to be changed and store in `/path/to/jsonfile`:

```json
{
   "filters": [
        {"or": [
            "attributes.arc_home_location_identity=locations/5ea815f0-4de1-4a84-9377-701e880fe8ae",
            "attributes.arc_home_location_identity=locations/27eed70b-9e2b-4db1-b8c4-e36505350dcc"
        ]},
        {"or": [
            "attributes.arc_display_type=Valve",
            "attributes.arc_display_type=Pump"
        ]},
        {"or": [
            "attributes.ext_vendor_name=SynsationIndustries"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": [ "toner_colour", "toner_type" ],
            "asset_attributes_write":["toner_colour"],
            "behaviours": [ "Attachments", "RecordEvidence" ],
            "event_arc_display_type_read": ["toner_type", "toner_colour"],
            "event_arc_display_type_write": ["toner_replacement"],
            "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
            "subjects": [
                "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
            ],
            "user_attributes": [
                {"or": ["group:maintainers", "group:supervisors"]}
            ]
        }
    ]
}
```

Update the access policy:

```bash
curl -v -X PATCH \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/access_policies/47b58286-ff0f-11e9-8f0b-362b9e155667
```
The response is:

```json
{
    "identity": "access_policies/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "display_name": "Friendly name of the policy",
    "description": "Description of the policy",
    "filters": [
        {"or": [
            "attributes.arc_home_location_identity=locations/5ea815f0-4de1-4a84-9377-701e880fe8ae",
            "attributes.arc_home_location_identity=locations/27eed70b-9e2b-4db1-b8c4-e36505350dcc"
        ]},
        {"or": [
            "attributes.arc_display_type=Valve",
            "attributes.arc_display_type=Pump"
        ]},
        {"or": [
            "attributes.ext_vendor_name=SynsationIndustries"
        ]}
    ],
    "access_permissions": [
        {
            "asset_attributes_read": [ "toner_colour", "toner_type" ],
            "asset_attributes_write":["toner_colour"],
            "behaviours": [ "Attachments","RecordEvidence" ],
            "event_arc_display_type_read": ["toner_type", "toner_colour"],
            "event_arc_display_type_write": ["toner_replacement"],
            "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
            "subjects": [
                "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
            ],
            "user_attributes": [
                {"or": ["group:maintainers", "group:supervisors"]}
            ]
        }
    ]
}
```

### Matching Assets with IAM Policies

IAM access policy records in RKVST are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
access_policies/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the `access_policy` identity you can fetch IAM access policy records using other information you do know, such as the `access_policy` name.

#### Fetch all Assets Matching Specific IAM access_policy (v1)

If you know the unique identity of the IAM access policy Record simply GET the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/access_policies/6a951b62-0a26-4c22-a886-1082297b063b/assets
```

Each of these calls returns a list of matching Asset records in the form:

```json
{
    "assets": [
        {
        "identity": "assets/6a951b62-0a26-4c22-a886-1082297b063b",
        "behaviours": [
            "RecordEvidence",
            "Attachments"
        ],
        "attributes": {
            "arc_display_type": "Pump",
            "arc_firmware_version": "1.0",
            "arc_home_location_identity": "locations/866790d8-4ed6-4cc9-8f60-07672609b331",
            "arc_serial_number": "vtl-x4-07",
            "arc_description": "Pump at A603 North East",
            "arc_display_name": "tcl.ccj.003",
            "some_custom_attribute": "value",
            "primary_image": {
                "arc_attribute_type": "arc_attachment",
                "arc_blob_hash_value": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b",
                "arc_blob_identity": "blobs/1754b920-cf20-4d7e-9d36-9ed7d479744d",
                "arc_blob_hash_alg": "SHA256",
                "arc_file_name": "somepic.jpeg",
                "arc_display_name": "arc_primary_image",
            },
        },
        "confirmation_status": "CONFIRMED",
        "tracked": "TRACKED"
        }
    ]
}
```

#### Fetch all IAM access_policies Matching Specific Asset (v1)

If you know the unique identity of the Asset Record simply GET matching policies:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/assets/6a951b62-0a26-4c22-a886-1082297b063b/access_policies
```

Each of these calls returns a list of matching IAM `access_policies` records in the form:

```json
{
    "access_policies": [
        {
            "identity": "access_policies/6a951b62-0a26-4c22-a886-1082297b063b",
            "display_name": "Some description",
            "filters": [
                { "or": [
                    "attributes.arc_home_location_identity=locations/5ea815f0-4de1-4a84-9377-701e880fe8ae",
                    "attributes.arc_home_location_identity=locations/27eed70b-9e2b-4db1-b8c4-e36505350dcc",
                ]},
                { "or": [
                    "attributes.arc_display_type=Valve",
                    "attributes.arc_display_type=Pump"
                ]},
                { "or": [
                    "attributes.ext_vendor_name=SynsationIndustries"
                ]}
            ],
            "access_permissions": [
                {
                    "subjects": [
                        "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                        "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
                    ],
                    "behaviours": [  "Attachments", "RecordEvidence"  ],
                    "include_attributes": [ "arc_display_name", "arc_display_type", "arc_firmware_version" ],
                    "user_attributes": [
                        {"or": ["group:maintainers", "group:supervisors"]}
                    ]
                }
            ]
        },
        {
            "identity": "access_policies/12345678-0a26-4c22-a886-1082297b063b",
            "display_name": "Some other description",
            "filters": [
                { "or": ["attributes.arc_display_type=door_access_reader"]}
            ],
            "access_permissions": [
                {
                    "subjects": [
                        "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
                        "subjects/a24306e5-dc06-41ba-a7d6-2b6b3e1df48d"
                    ],
                    "behaviours": [ "Attachments", "RecordEvidence" ],
                    "include_attributes": [ "arc_display_name", "arc_display_type" ],
                    "user_attributes": [
                        {"or": ["group:maintainers", "group:supervisors"]}
                    ]
                }
            ]
        }
    ]
}
```

## IAM Policies OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/rkvst/archivist-docs/master/doc/openapi/accesspoliciesv1.swagger.json" >}}
