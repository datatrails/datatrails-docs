---
title: "IAM Subjects API"
description: "IAM Subjects API Reference"
lead: "IAM Subjects API Reference"
date: 2021-06-09T12:02:15+01:00
lastmod: 2021-06-09T12:02:15+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 117
toc: true
aliases: 
  - /docs/api-reference/iam-subjects-api/
---
{{< note >}}
**Note:** This page is primarily intended for developers who will be writing applications that will use DataTrails for provenance. 
If you are looking for a simple way to test our API you might prefer our [Postman collection](https://www.postman.com/datatrails-inc/workspace/datatrails-public/overview), the [YAML runner](/developers/yaml-reference/story-runner-components/) or the [Developers](https://app.datatrails.ai) section of the web UI. 

Additional YAML examples can be found in the articles in the [Overview](/platform/overview/introduction/) section.
{{< /note >}}
## IAM Subjects API Examples

Create the [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### IAM Subjects Creation

Define the Subject parameters and store in `/path/to/jsonfile`:

```json
{
    "display_name": "Some description",
    "wallet_pub_key": ["key1"],
    "tessera_pub_key": ["key2"]
}
```
{{< note >}}
**Note:** The values for `wallet_pub_key` and `tessera_pub_key` are found by decoding the Subject string that is provided by the Tenancy Administrator of the other organization. See the JSON tab [here](https://docs.datatrails.ai/platform/administration/sharing-access-outside-your-tenant/) for more detail.
{{< /note >}}

Create the IAM Subject:

```bash
curl -v -X POST \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/iam/v1/subjects
```

The response is:

```json
{
    "identity": "subjects/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "display_name": "Some description",
    "wallet_pub_key": ["key1"],
    "wallet_address": ["address"],
    "tessera_pub_key": ["key2"]
}
```

### IAM Subjects Retrieval

IAM Subject records in DataTrails are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
subjects/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the Subjects’s identity you can fetch IAM Subject records using other information you do know, such as the Subject’s name.

#### Fetch all IAM Subjects (v1)

To fetch all IAM Subjects records, simply `GET` the `/subjects` resource:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/iam/v1/subjects
```

#### Fetch specific IAM Subject by identity (v1)

If you know the unique identity of the IAM Subject record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/iam/v1/subjects/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch IAM Subjects by Name (v1)

To fetch all IAM subjects with a specific name, `GET` the `/subjects` resource and filter on `display_name`:

```bash
curl -g -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/iam/v1/subjects?display_name=Acme"
```

Each of these calls returns a list of matching IAM Subjects records in the form:

```json
{
    "subjects": [
        {
            "identity": "subjects/6a951b62-0a26-4c22-a886-1082297b063b",
            "display_name": "Some description",
            "wallet_pub_key": ["key1"],
            "wallet_address": ["address1"],
            "tessera_pub_key": ["key2"]
        },
        {
            "identity": "subjects/12345678-0a26-4c22-a886-1082297b063b",
            "display_name": "Some other description",
            "wallet_pub_key": ["key5"],
            "wallet_address": ["address5"],
            "tessera_pub_key": ["key7"]
        }
    ]
}
```

### IAM Subject Deletion

To delete an IAM Subject, issue the following request:

```bash
curl -v -X DELETE \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    https://app.datatrails.ai/archivist/iam/v1/subjects/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The response is `{}`.

### IAM Subject Update

Define the Subject parameters to be changed and store in `/path/to/jsonfile`:

```json
{
    "wallet_pub_key": ["key1"],
    "tessera_pub_key": ["key2"]
}
```

Update the IAM Subject:

```bash
curl -v -X PATCH \
    -H "@$HOME/.datatrails/bearer-token.txt" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.datatrails.ai/archivist/iam/v1/subjects/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The response is:

```json
{
    "identity": "subjects/3f5be24f-fd1b-40e2-af35-ec7c14c74d53",
    "display_name": "Some description",
    "wallet_pub_key": ["key1"],
    "wallet_address": ["address1"],
    "tessera_pub_key": ["key3"]
}
```

### IAM Subject Self Entry

There is an immutable entry in the Subjects API called `Self` that contains the keys for the hosting organization of the DataTrails Tenant.

This entry cannot be deleted or updated.

This special identity is:

```bash
subjects/00000000-0000-0000-0000-000000000000
```

#### Fetch Self IAM Subject by Identity (v1)

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/iam/v1/subjects/00000000-0000-0000-0000-000000000000
```

The response is:

```json
[
    {
        "identity": "subjects/00000000-0000-0000-0000-000000000000",
        "display_name": "Some description",
        "wallet_pub_key": ["key1"],
        "wallet_address": ["address1"],
        "tessera_pub_key": ["key3"]
    }
]
```

## IAM Subjects OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/datatrails/datatrails-openapi/master/doc/subjectsv1.swagger.json" >}}
