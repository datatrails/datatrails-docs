---
title: "IAM Subjects API"
description: "IAM Subjects API Reference"
lead: "IAM Subjects API Reference"
date: 2021-06-09T12:02:15+01:00
lastmod: 2021-06-09T12:02:15+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 109
toc: true
---

## IAM Subjects API Examples

Create the [bearer_token](../../setup-and-administration/getting-access-tokens-using-app-registrations) and store in a file in a secure local directory with 0600 permissions.

### IAM Subjects Creation

Define the subjects parameters and store in `/path/to/jsonfile`:

```json
{
    "display_name": "Some description",
    "wallet_pub_key": ["key1"],
    "tessera_pub_key": ["key2"]
}
```

Create the IAM subject:

```bash
curl -v -X POST \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/subjects
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

IAM subject records in RKVST are tokenized at creation time and referred to in all API calls and smart contracts throughout the system by a unique identity of the form:

```bash
subjects/12345678-90ab-cdef-1234-567890abcdef
```

If you do not know the subjects’s identity you can fetch IAM subject records using other information you do know, such as the subject’s name.

#### Fetch all IAM subjects (v1)

To fetch all IAM subjects records, simply `GET` the `/subjects` resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/subjects
```

#### Fetch specific IAM Subject by identity (v1)

If you know the unique identity of the IAM subject Record simply `GET` the resource:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/subjects/6a951b62-0a26-4c22-a886-1082297b063b
```

#### Fetch IAM Subjects by name (v1)

To fetch all IAM subjects with a specific name, `GET` the `/subjects` resource and filter on `display_name`:

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/subjects?display_name=Acme
```

Each of these calls returns a list of matching IAM subjects records in the form:

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
            "display_name": "Some otherdescription",
            "wallet_pub_key": ["key5"],
            "wallet_address": ["address5"],
            "tessera_pub_key": ["key7"]
        }
    ]
}
```

### IAM Subject Deletion

To delete an IAM subject, issue the following request:

```bash
curl -v -X DELETE \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    https://app.rkvst.io/archivist/iam/v1/subjects/47b58286-ff0f-11e9-8f0b-362b9e155667
```

The response is `{}`.

### IAM Subject Update

Define the subjects parameters to be changed and store in `/path/to/jsonfile`:

```json
{
    "wallet_pub_key": ["key1"],
    "tessera_pub_key": ["key2"]
}
```

Update the IAM Subject:

```bash
curl -v -X PATCH \
    -H "@$BEARER_TOKEN_FILE" \
    -H "Content-type: application/json" \
    -d "@/path/to/jsonfile" \
    https://app.rkvst.io/archivist/iam/v1/subjects/47b58286-ff0f-11e9-8f0b-362b9e155667
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

There is an immutable entry in the subjects API called `Self` that contains the keys for the hosting organisation of the RKVST Tenant.

This entry cannot be deleted or updated.

This special identity is:

```bash
subjects/00000000-0000-0000-0000-000000000000
```

#### Fetch self IAM Subject by identity (v1)

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/subjects/00000000-0000-0000-0000-000000000000
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

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/subjectsv1.swagger.json" >}}