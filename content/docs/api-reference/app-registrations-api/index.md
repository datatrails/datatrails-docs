---
title: "App Registrations API"
description: "App Registrations API Reference"
lead: "App Registrations API Reference"
date: 2021-06-09T11:39:03+01:00
lastmod: 2021-06-09T11:39:03+01:00
draft: false
images: []
menu: 
  docs:
    parent: "api-reference"
weight: 101
toc: true
---

## App Registrations API Examples

The App Registrations API enables you to create and manage application identities with access to your RKVST tenant. 

It supports the OpenID Connect Client Credentials Flow, which means that for each application you register, a `CLIENT_ID` and `SECRET` are generated and returned. 

Each App Registration is created with non-root privileges by default; you must create an [ABAC policy](../iam-policies-api/) to permit specific access to that App Registration. It is also possible to give these credentials Root User Access, but it is considered best practice to create specific ABAC policies, preserving Principle of Least Privilege, instead.

These can be used to request an access token from `https://app.rkvst.io/archivist/iam/v1/appidp/token`, used for application authentication to RKVST.

### Creating an Application

Create a JSON file with the parameters of your new application. Below is an example:

```json
{
    "display_name": "TrafficLight101",
    "custom_claims": {
      "serial_number": "TL1000000101",
      "has_cyclist_light": "true"
    }
}
```

Once you have created your file, you can then submit it to the RKVST API:

```bash
curl -X POST \
     -H "@$BEARER_TOKEN_FILE" \
     -H "Content-Type: application/json" \
     -d "@/path/to/jsonfile" \
     https://app.rkvst.io/archivist/iam/v1/applications
```

An example response is shown below. 

The client secret ***must*** be taken note of at this point, as it will be redacted in any attempt to retrieve the application (shown as an empty string.)

```json
{
    "identity": "applications/d1fb6c87-faa9-4d56-b2fd-a5b70a9af065",
    "display_name": "TrafficLight101",
    "client_id": "d1fb6c87-faa9-4d56-b2fd-a5b70a9af065",
    "tenant_id": "tenant/53e6bed7-6f4c-4a37-8c4f-cf889f2b1aa6",
    "credentials": [
        {
            "secret":"a0c09972b6ac912a4d67815fef88093c81a99b49977d35ecf6d162631aa29173",
            "valid_from": "2021-09-21T16:43:19Z",
            "valid_until": "2022-09-21T16:43:19Z"
        }
    ],
    "custom_claims": {
        "serial_number": "TL1000000101",
        "has_cyclist_light": "true"
    }
}
```

{{< caution >}}
**Caution:** The expiry date refers to the secret only, any tokens generated with this secret will not automatically become invalid when the secret expires or is rotated. Each token has a TTL of 1 hour. 
{{< /caution >}}

#### Authenticating with your Application

Now that you've created an application, you get a token.

Replace `${CLIENT_ID}` with the application id, and `${SECRET}` with your secret from the application registration.

```bash
curl https://app.rkvst.io/archivist/iam/v1/appidp/token \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${CLIENT_ID}" \
    --data-urlencode "client_secret=${SECRET}"
```

The token is found in the `.access_token` field and it is a base64 encoded [JSON Web Token](https://jwt.io/introduction/).

A common method to extract the token is to use `jq`, where `$RESPONSE` is the output your curl command:

```bash
TOKEN=$(echo -n $RESPONSE | jq -r .access_token)
```

You should then save the token to a local `bearer_token` file with `0600` permissions in the following format:

```bash
Authorization: Bearer $TOKEN
```

Where `$TOKEN` is the extracted token value.

You can then use this bearer token to interact with other RKVST services.

### Listing Applications

All of the applications created for your RKVST tenancy can be viewed using the following command.

```bash
curl -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/applications
```

### Viewing Applications

The following example shows how to view the details of a single application.

```bash
export IDENTITY="applications/d1fb6c87-faa9-4d56-b2fd-a5b70a9af065"

curl -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/${IDENTITY}
```
### Updating Applications

You may edit the display name and/or the custom claims of an Application.

Create a JSON file containing the details you wish to update, partial updating of Applications is also supported. Below is an example:

```json
{
    "custom_claims": {
      "has_cyclist_light": "false"
    }
}
```

Once you've created your file, submit it to the RKVST API:

```bash
export IDENTITY="applications/d1fb6c87-faa9-4d56-b2fd-a5b70a9af065"

curl -X PATCH \
     -H "@$BEARER_TOKEN_FILE" \
     -H "Content-Type: application/json" \
     -d "@/path/to/json"
     https://app.rkvst.io/archivist/iam/v1/${IDENTITY}
```

Example response:

```json
{
    "identity": "applications/d1fb6c87-faa9-4d56-b2fd-a5b70a9af065",
    "display_name": "TrafficLight101",
    "client_id": "d1fb6c87-faa9-4d56-b2fd-a5b70a9af065",
    "tenant_id": "tenant/53e6bed7-6f4c-4a37-8c4f-cf889f2b1aa6",
    "credentials": [
        {
            "secret": "",
            "valid_from": "2021-09-21T16:43:19Z",
            "valid_until": "2022-09-21T16:43:19Z"
        }
    ],
    "custom_claims": {
        "has_cyclist_light": "false"
    }
}
```
### Regenerating Application Secrets

It is possible to regenerate the secret for an existing application. 

The expected response will be the same as for [creation](./#creating-an-application), but the credential entry will have been updated with a new secret, along with new expiry dates. 

Once again, you ***must*** take note of the secret at this point, as it will not be recoverable.

```bash
export IDENTITY="applications/d1fb6c87-faa9-4d56-b2fd-a5b70a9af065"

curl -X POST \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/${IDENTITY}:regenerate-secret
```

{{< caution >}}
**Caution:** The expiry date refers to the secret only, any tokens generated with this secret will not automatically become invalid when the secret expires or is rotated. Each token has a TTL of 1 hour. 
{{< /caution >}}

### Deleting Applications
The following example shows how to delete an application.

```bash
export IDENTITY="applications/d1fb6c87-faa9-4d56-b2fd-a5b70a9af065"

curl -X DELETE \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/iam/v1/${IDENTITY}
```

## App Registrations OpenAPI Docs

{{< openapi url="https://raw.githubusercontent.com/jitsuin-inc/archivist-docs/master/doc/openapi/appregistrationsv1.swagger.json" >}}
