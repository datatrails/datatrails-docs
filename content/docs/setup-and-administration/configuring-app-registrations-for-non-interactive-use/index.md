---
title: "Configuring App Registrations for Non-Interactive Use"
description: "Creating App Registrations for RKVST"
lead: "Creating App Registrations for RKVST"
date: 2021-06-16T11:12:25+01:00
lastmod: 2021-06-16T11:12:25+01:00
draft: false
images: []
menu: 
  docs:
    parent: "setup-and-administration"
weight: 12
toc: true
---

Non-interactive access to the RKVST platform is managed by creating `Applications` with App Registrations, using either the Manage RKVST Menu in the UI or by using the App Registrations API directly.

`Applications` have a `CLIENT ID` and `SECRET` that can then be used to authenticate to RKVST IAM Endpoints to issue a token (JWT) for accessing the rest of the RKVST API.

This authentication flow uses the industry-standard OIDC 'Client Credentials' Flow. 

## Creating an App Registration

{{< warning >}}
**Warning:** You may only create `App Registrations` with a **Root User**.
{{< /warning >}}

When enabling non-interactive access to RKVST, you **must** create your first `App Registration` in the RKVST UI.

### Using the RKVST UI (Required for First-Time Setup)

1. As a Root User visit the APP REGISTRATIONS tab in the `Manage RKVST` Interface
2. Click CREATE APP REGISTRATION.
3. Enter any display name you like.

  Optional - using the ADD CUSTOM CLAIM button Add any extra claims you require in your access token.

4. Click CREATE APP REGISTRATION. The response will include the CLIENTID and SECRET required by the archivist token endpoint.

{{< caution >}}
**Caution:** You **must** take note of the `SECRET` at this point - it can **not** be viewed again later.
{{< /caution >}}

5. Now you have created your App Registration, follow the steps further below to [test generating a token](./#getting-a-token-with-your-app-registration) and [ensure you can access the RKVST API](./#testing-your-access).

{{< note >}}
**Note:** By default, newly created Applications will always have a Non-Root User permission to the API. To give an Application Root User priviliges so it can be used to administrate RKVST, including adding and managing new App Registrations, please refer to our [Tenancies API](../../api-reference/tenancies-api)
{{< /note >}}

### Using the App Registrations API

The following assumes you already have at least one `App Registration` that has already been configured with Root User permissions and that you are comfortable generating tokens and using the RKVST API.

If you do not yet have an App Registration configured please follow [the first-time setup guide](./#using-the-rkvst-ui-(required-for-first-time-setup)) to get started.

1. Define your new Application JSON and save it to a file locally. e.g.

```json
{
    "display_name": "TrafficLight101",
    "custom_claims": {
      "serial_number": "TL1000000101",
      "has_cyclist_light": "true"
    }
}
```

2. Generate a token using your pre-existing `App Registration` details

```bash
RESPONSE=$(curl \
    https://app.rkvst.io/archivist/iam/v1/appidp/token \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${CLIENTID}" \
    --data-urlencode "client_secret=${SECRET}")

TOKEN=$(echo -n $RESPONSE | jq .access_token | tr -d '"')
```

and save it locally to a bearer_token file.

3. Submit your new Application JSON to the App Registration API Endpoint 

```bash
curl -X POST \
     -H "@$BEARER_TOKEN_FILE" \
     -H "Content-Type: application/json" \
     -d "@/path/to/jsonfile" \
     $URL/archivist/iam/v1/applications
```

You should see a response with details about the App Registration's `CLIENT ID` and `SECRET`:

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
**Caution:** You **must** take note of the `SECRET` at this point - it can **not** be viewed again later.
{{< /caution >}}

4. You should now have a newly configured App Registration and have recorded its `CLIENT_ID` and its `SECRET` so that it can be used to [generate a token](./#getting-a-token-with-your-app-registration) and [access the RKVST API](./#testing-your-access).

For more details check out our [App Registrations API Reference](../../api-reference/app-registrations-api) which not only contains more detailed usage examples but also has the full OpenAPI Reference.

## Getting a Token With Your App Registration

Having completed the steps at [Creating an App Registration](./#creating-an-app-registration), and having taken note of the `CLIENT ID` and the `SECRET`, a token can be obtained with the following command.

Replace `${CLIENTID}` with the application id, and `${SECRET}` with your secret from the application registration.

```bash
$ RESPONSE=$(curl \
    https://app.rkvst.io/archivist/iam/v1/appidp/token \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${CLIENTID}" \
    --data-urlencode "client_secret=${SECRET}")

$ TOKEN=$(echo -n $RESPONSE | jq .access_token | tr -d '"')
```

### Testing Your Access

To confirm access token configuration, use the shell command (above) to obtain
an access token. The response is json structured data. The token is found in
the `access_token` field. It is a base64 encoded [JSON Web Token](https://jwt.io/introduction/).

The header and payload of the `TOKEN` can be examined with the following commands.

```shell
# Header
echo -n $TOKEN | cut -d '.' -f 1 | base64 -D

# Payload
echo -n $TOKEN | cut -d '.' -f 2 | base64 -D
```

{{< note >}}
**Note:** Decoding tokens with an online service exposes your RKVST until you delete the test secret.
{{< /note >}}

