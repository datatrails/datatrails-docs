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

Non-interactive access to the RKVST platform is managed through `App Registrations` in the `Manage RKVST` Interface.

`App Registrations` are Machine Auth Profiles with `CLIENT ID`s and `SECRET`s that can then be used to generate JWT Tokens for authenticating to the RKVST API Endpoints.

To enable non-interactive access to RKVST you **must** create your first `App Registration` in the RKVST UI as a `Root User`.

## Creating an App Registration

### Using the RKVST UI (Required for First-Time Setup)

1. As a `Root User` visit the APP REGISTRATIONS tab on the Manage RKVST page in the RKVST UI.
2. Click CREATE APP REGISTRATION.
3. Enter any display name you like.
  a. Optional - using the ADD CUSTOM CLAIM button Add any extra claims you require in your access token.
4. Click CREATE APP REGISTRATION. The response will include the CLIENTID and SECRET required by the archivist token endpoint.

{{< caution >}}
**Caution:** You **must** take note of the secret at this point - it can not be viewed again.
{{< /caution > }}

### Using the App Registrations API

1. Define your Application json and save it to local path e.g.



```bash
curl -X POST \
     -H "@$BEARER_TOKEN_FILE" \
     -H "Content-Type: application/json" \
     -d "@/path/to/jsonfile" \
     $URL/archivist/iam/v1/applications
```

## Getting a token with your App Registration

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

### Using your token

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

##