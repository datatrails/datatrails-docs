---
title: "Getting Access Tokens using a Custom Integration"
description: "Getting Access Tokens using a Custom Integration"
lead: "Creating Access Tokens for RKVST"
date: 2021-06-16T11:12:25+01:00
lastmod: 2021-06-16T11:12:25+01:00
draft: false
images: []
menu: 
  developers:
    parent: "developer-patterns"
weight: 31
toc: true
aliases:
  - ../setup-and-administration/getting-access-tokens-using-app-registrations
  - /docs/rkvst-basics/getting-access-tokens-using-app-registrations/
---

Non-interactive access to the RKVST platform is managed by creating `Integrations` with either a Custom Integration or one of our built-in Integrations. This is done using either the `Settings` Menu in the UI or by using the App Registrations API directly.
{{< note >}}
**Note:** App Registration is the previous name for an Integration.
{{< /note >}}
 
`Integrations` have a `CLIENT_ID` and `SECRET` that can then be used to authenticate to RKVST IAM endpoints to issue a token (JWT) for accessing the rest of the RKVST API.

This authentication flow uses the industry-standard OIDC 'Client Credentials' Flow. 

## Creating a Custom Integration

{{< warning >}}
**Warning:** You may only create and manage App Registrations with an **Administrator** level account.
{{< /warning >}}

When enabling non-interactive access to RKVST, you ***must*** create your first Integration in the **RKVST UI**.

### Using the RKVST UI to create an Integration (First-Time Setup)

1. As an Administrator, open the `Settings` interface.

{{< img src="Settings.png" alt="Rectangle" caption="<em>Settings</em>" class="border-0" >}}

2. Navigate to the `Integrations` tab.

{{< img src="IntegrationsTab.png" alt="Rectangle" caption="<em>Navigate to Integrations</em>" class="border-0" >}}

3. Click the `Custom` box and the following form should appear:

{{< img src="CreateCustomForm.png" alt="Rectangle" caption="<em>Custom Integration Webform</em>" class="border-0" >}}

3. Enter any display name you'd like, then click `Confirm`.

{{< note >}}
 You can optionally add any Custom Claims at this step. You must ensure they do not start with `jit_` or use any of the [well-known reserved claims](https://auth0.com/docs/security/tokens/json-web-tokens/json-web-token-claims#reserved-claims). The Custom Claims can be used in an [Attribute-Based Access Control (ABAC) policy](/platform/administration/managing-access-to-an-asset-with-abac) to grant permissions. 
{{< /note >}}

{{< img src="Confirm.png" alt="Rectangle" caption="<em>Completed Web Registration</em>" class="border-0" >}}

4.  You will then be presented with the `CLIENT_ID` and `SECRET` required by the archivist token endpoint.

{{< caution >}}
**Caution:** You **must** take note of the `SECRET` at this point - it can **not** be viewed again later and you will have to generate a new one.
{{< /caution >}}

{{< img src="RecordClientIDandSecret.png" alt="Rectangle" caption="<em>Record your Client ID and Secret</em>" class="border-0" >}}

5. Now that you have created your Custom Integration, follow the steps below to [test generating a token](./#getting-a-token-with-your-app-registration) and [ensure you can access the RKVST API](./#testing-your-access).

{{< note >}}
**Note:** By default, newly created Integrations will always have a Non-Administrator permission to the API, you must add the Integration as an Administrator to elevate it's permissions.

You can add a Custom Integration as an Administrator using the `Settings` screen, where the issuer will be `https://app.rkvst.io/appidpv1` and the subject will be your Integration's `CLIENT_ID`.
{{< /note >}}

### Using the App Registrations API to create an Integration

{{< note >}}
**Note:** App Registration is the previous name for an Integration.
{{< /note >}}

The following assumes you have at least one `Custom Integration` that has already been configured with Administrator permissions and that you are comfortable generating tokens and using the RKVST API.

If you do not yet have an Integration configured please follow the [first-time setup guide](./#using-the-rkvst-ui-to-create-an-app-registration-first-time-setup) to get started.

1. Define your new Integration JSON and save it to a file locally.

```json
{
    "display_name": "TrafficLight101",
    "custom_claims": {
      "serial_number": "TL1000000101",
      "has_cyclist_light": "true"
    }
}
```

2. Generate a token using your pre-existing `Custom Integration` details.

```bash
curl https://app.rkvst.io/archivist/iam/v1/appidp/token \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${CLIENT_ID}" \
    --data-urlencode "client_secret=${SECRET}"
```

The token is found in the `.access_token` field as a base64 encoded [JSON Web Token](https://jwt.io/introduction/).

A common method to extract the token is to use `jq`, where `$RESPONSE` is the output of your curl command:

```bash
TOKEN=$(echo -n $RESPONSE | jq -r .access_token)
```

You should then save the token to a local `bearer_token` file with `0600` permissions in the following format:

```bash
Authorization: Bearer $TOKEN
```

Where `$TOKEN` is the extracted token value.

3. Submit your new Application JSON to the App Registration API endpoint. 

```bash
curl -X POST \
     -H "@$BEARER_TOKEN_FILE" \
     -H "Content-Type: application/json" \
     -d "@/path/to/jsonfile" \
     https://app.rkvst.io/archivist/iam/v1/applications
```

You should see a response with details about the Integration's `CLIENT_ID` and `SECRET`:

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
**Caution:** You **must** take note of the `SECRET` at this point - it can **not** be viewed again later and you will have to generate a new one.
{{< /caution >}}

4. You should now have a newly configured Integration and recorded its `CLIENT_ID` and `SECRET`. It can be used to [generate a token](./#getting-a-token-with-your-app-registration) and [access the RKVST API](./#testing-your-access).

For further details on using this API check out our [App Registrations API Reference](../../api-reference/app-registrations-api) which contains more detailed usage examples and has the full OpenAPI Reference.

## Getting a Token With Your Integration

Having completed the steps at [Creating a Custom Integration](./#creating-a-custom-integration), and having taken note of the `CLIENT_ID` and the `SECRET`, a token can be obtained with the following command.

Replace `$CLIENT_ID` with the Application ID, and `$SECRET` with your secret from the Integration.

```bash
curl https://app.rkvst.io/archivist/iam/v1/appidp/token \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${CLIENT_ID}" \
    --data-urlencode "client_secret=${SECRET}"
```

The token is found in the `.access_token` field and it is a base64 encoded [JSON Web Token](https://jwt.io/introduction/).

A common method to extract the token is to use `jq`, where `$RESPONSE` is the output returned from your curl command:

```bash
TOKEN=$(echo -n $RESPONSE | jq -r .access_token)
```

You should then save the token to a local `bearer_token` file with `0600` permissions in the following format:

```bash
Authorization: Bearer $TOKEN
```

Where `$TOKEN` is the extracted token value.

### Testing Your Access

You can test access to the RKVST API using any of our standard calls. Doing a GET Assets is a very simple test.

For example:

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v2/assets
```

If successful, you should then see a list of the assets your Integration has access to in the tenancy. Note this may be an empty response if no assets are being shared with the user; this is an expected behaviour.

Otherwise, check the [Assets OpenAPI Reference](../../api-reference/assets-api/#assets-openapi-reference) for more detailed information on the response codes you may expect if authentication fails and what they mean.

### Troubleshooting Token Generation

The header and payload of the `TOKEN` may be examined with the following commands:

```shell
# Header
echo -n $TOKEN | cut -d '.' -f 1 | base64 -D

# Payload
echo -n $TOKEN | cut -d '.' -f 2 | base64 -D
```

This is useful when investigating if tokens contain the correct custom claims or tokens that may appear malformed.

{{< note >}}
**Note:** Decoding tokens with an online service exposes details about your RKVST until you delete the test secret.
{{< /note >}}