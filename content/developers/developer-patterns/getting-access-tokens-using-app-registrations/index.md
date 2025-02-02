---
title: "Creating Access Tokens Using a Custom Integration"
description: "Creating Access Tokens Using a Custom Integration"
lead: "Creating Access Tokens for DataTrails"
date: 2021-06-16T11:12:25+01:00
lastmod: 2023-09-27T11:12:25+01:00
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

Non-interactive access to the DataTrails platform is managed by creating `Integrations` with either a Custom Integration or one of the built-in Integrations. This is done from the `Integrations` page in the DataTrails UI (reachable
from the `Settings` page or the `Integrations` shortcut in the sidebar.) You can also do this via 
the App Registrations REST API.

{{< note >}}
**Note:** App Registration is the internal name for a Custom Integration.
{{< /note >}}

`Custom Integrations` have a `CLIENT_ID` and a `SECRET`, these are used to authenticate with DataTrails IAM endpoints using [JSON Web Tokens](https://jwt.io/introduction/) (JWT).

DataTrails authentication uses the industry-standard OIDC Client Credentials Flow.

The high level steps are:

1. Create an Integration in the UI
1. Define access permissions for the Integration in the UI
1. Request an Access Token using the API
1. Use the Access Token to make a REST API call to your tenancy.

## Creating a Custom Integration

If you have already saved a `CLIENT_ID` and a `SECRET`, with the correct [permissions applied](#grant-permissions-to-custom-integration), skip to [Getting a Token With the Custom Integration](#getting-a-token-with-the-custom-integration)

{{< note >}}
**Note:** Creating App Registrations requires **Owner** privileges.  
If `Settings` or `Integrations` does not appear in the navigation, see your DataTrails Administrator for access.
{{< /note >}}

### Using the DataTrails App to Create an Integration (First-Time Setup)

1. As an Administrator, open the <a href="https://app.datatrails.ai/" target="_blank">DataTrails App</a>
1. Navigate to `Integrations` on the sidebar
1. This opens the `Integrations` tab
1. Click the `Custom` box to create a Custom Integration
  {{< img src="IntegrationsTab.png" alt="Rectangle" caption="<em>Navigate to Settings, then Integration</em>" class="border-0" >}}
1. Enter a `Display Name` to help you identify this Custom Integration in future
  {{< img src="Confirm.png" alt="Rectangle" caption="<em>Completed Web Registration</em>" class="border-0" >}}
  {{< note >}}
  **Note:** Optionally add any `Custom claims` at this step by clicking the `+ Add` button.<br>In this context, claims are pieces of information that are asserted in a JSON Web Token (JWT). *Registered* claims are name/value pairs that are defined by the JWT standard, *Custom* claims are not defined and can have any name/value combination.

  Ensure the `Name` *does not start* with `jit_` or `arc_` (DataTrails reserved names) or use any other well-known reserved claims.
  
  See [here](https://auth0.com/docs/security/tokens/json-web-tokens/json-web-token-claims#reserved-claims) for more information on JWT Claims
  {{< /note >}}  
1. If this Custom Integration should have administrator privileges, assign it the `Owner` role by 
   checking that option. If you do this, ensure the client credentials are securely protected.
1. Once complete, click `Confirm` to complete the custom integration
1. You will then be presented with the `CLIENT_ID` and `SECRET` required by the archivist token endpoint
{{< img src="RecordClientIDandSecret.png" alt="Rectangle" caption="<em>Record your Client ID and Secret</em>" class="border-0" >}}
{{< caution >}}
**Caution:** Save the `CLIENT_ID` and `SECRET` to a password manager or secret management service as the `SECRET` can **not** be viewed again. A new `SECRET` can be regenerated in the Integration configuration screen but this replaces and invalidates the previous `SECRET`.
{{< /caution >}}  

### Grant Access Permissions to your Custom Integration

In this section we will give your Custom Integration permission to access the Assets, their attributes, and Events that have been recorded in your tenancy.

Integrations are secured by default, with no read or write permissions within your DataTrails Tenancy. This is is important because the alternative would be to allow read/write access to all Assets and Events by default which opens the risk that an application could be maliciously altered to make changes that would not be permitted by the Tenancy Administrator.

The steps below show how to create and assign an Access Policy to control the ability to create and read DataTrails information.<br>For convenience we will grant full access rights to the customer integration in this example. Please see [this article](/platform/administration/sharing-access-inside-your-tenant/) for information on setting up more finely controlled access.

1. Navigate to `Access Policies` on the sidebar
  {{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}
1. Click `CREATE POLICY`, setting the `Name` and `Asset Types`=`*` for all types
  {{< note >}}
  **Note:** Asset types can be filtered as needed. List existing `Asset Types` by typing at least two characters of a known type
  {{< /note >}}
  {{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Create Access Policy Form</em>" class="border-0" >}}
1. Click `Permissions` to set a scope for the policy
1. Set Actors to the `CLIENT_ID` of the Custom Integration
   - `User`
   - `Subject Identifier`
   - Paste the `CLIENT_ID` from the previous step
  {{< img src="PolicyPermissionActor.png" alt="Rectangle" caption="<em>Filter on User by Subject Identifier using the CLIENT_ID</em>" class="border-0" >}}
1. Set **Attribute Access** and **Event Visibility** to `All`
  {{< note >}}
  **Note:** Each policy can be configured with multiple access rights
  {{< /note >}}
  {{< img src="PolicyPermissionAccess.png" alt="Rectangle" caption="<em>Set Attribute Access and Event Visibility</em>" class="border-0" >}}
1. Click the `ADD PERMISSION GROUP` to save the configuration of this policy
1. Click the `CREATE POLICY` to complete the creation of this policy

## Getting a Token With the Custom Integration

Having completed the steps to create a [custom integration](./#creating-a-custom-integration) and [grant access permissions](./#grant-access-permissions-to-your-custom-integration), and having taken note of the `CLIENT_ID` and the `SECRET`, a token can be obtained with the following command.

{{< note >}}
**Note:** To make things easy we will use local variables and files to store the credentials and token but you can use any method that you wish.
{{< /note >}}

1. Save the `CLIENT_ID` and `SECRET` saved from above, to local variables
  {{< note >}}
  **Note:** Remember that you can regenerate the secret but this will invalidate the previous credentials which may be being used by other applications.
  Also note the environment variables below have been namespaced for DataTrails, as you may have `CLIENT_ID` and `SECRET`s for other services.
  {{< /note >}}

   ```bash
   export DATATRAILS_CLIENT_ID=your_id
   export DATATRAILS_CLIENT_SECRET=your_secret
   ```

1. Generate a token using your pre-existing `Custom Integration` details, saving to a `RESPONSE` variable

    ```bash
    RESPONSE=$(curl \
        https://app.datatrails.ai/archivist/iam/v1/appidp/token \
        --data-urlencode "grant_type=client_credentials" \
        --data-urlencode "client_id=${DATATRAILS_CLIENT_ID}" \
        --data-urlencode "client_secret=${DATATRAILS_CLIENT_SECRET}")

    # Save the base64 encoded `JWT` using `jq` to find `.access_token`
    TOKEN=$(echo -n $RESPONSE | jq -r .access_token)

    # Create a Bearer Token file for reference by `curl`
    # in an `./datatrails/` directory
    mkdir -p $HOME/.datatrails
    chmod 0700 $HOME/.datatrails
    
    # Create the Bearer Token
    echo Authorization: Bearer $TOKEN > $HOME/.datatrails/bearer-token.txt
    cat $HOME/.datatrails/bearer-token.txt
    ```

## Testing Token Creation

You can test access to the DataTrails API using any of the standard API calls. GETing `Assets` is a simple test.

If successful, you will see a list of the assets the Integration has access to in the tenancy.
{{< note >}}
**Note:** This may be an empty response if no assets are being shared with the Integration because an Access Policy has not been created for it; this is an expected *secure by default* behavior.
{{< /note >}}

Otherwise, check the [Assets OpenAPI Reference](../../api-reference/assets-api/#assets-openapi-reference) for more detailed information on the response codes you may expect if authentication fails and what they mean.

### View Existing Assets

To test the creation of the Custom integration and the configuration of the bearer token file (`bearer-token.txt`), query the assets API

```bash
curl -X GET -H "@$HOME/.datatrails/bearer-token.txt" \
    https://app.datatrails.ai/archivist/v2/assets | jq
```

If you have existing assets, the output will be similar to:

```json
{
  "assets": [
    {
      "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "behaviours": [
        "AssetCreator",
        "RecordEvidence",
        "Builtin"
      ],
      "attributes": {
        "length": "40'",
        "weight": "20000-lbs",
        "width": "8'",
        "arc_description": "A shipping container being tracked",
        "arc_display_name": "New Shipping Container #1",
        "arc_display_type": "Shipping Container",
        "arc_home_location_identity": "locations/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "height": "8'"
      },
      "confirmation_status": "COMMITTED",
      "tracked": "TRACKED",
      "owner": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "at_time": "2023-09-22T03:39:46Z",
      "storage_integrity": "TENANT_STORAGE",
      "chain_id": "8275868384",
      "public": false,
      "tenant_identity": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  ],
  "next_page_token": ""
}
```

If the output is an empty structure, you may either not have any assets, or misconfigured the [Access Policy](#grant-permissions-to-custom-integration).

```json
{
  "assets": [],
  "next_page_token": ""
}
```

In the <a href="https://app.datatrails.ai/" target="_blank">DataTrails App</a>, Navigate to `Assets` confirm existing assets. If assets exist, confirm the `DATATRAILS_CLIENT_ID`, `DATATRAILS_CLIENT_SECRET` and `Access Policy` are configured and referenced properly.

## Troubleshooting Token Generation

The header and payload of the `TOKEN` may be examined with the following commands. This is useful when investigating if tokens contain the correct custom claims or tokens that may appear malformed.

{{< warning >}}
**Warning:** Decoding tokens with an online service exposes details about your DataTrails token credentials. Remember to regenerate the credentials when troubleshooting is complete.
{{< /warning >}}

1. View the Header

    ```bash
    echo -n $TOKEN | cut -d '.' -f 1 | base64 -d | jq
    ```

    Generates output similar to:

    ```json
    {
      "alg": "RS256",
      "typ": "at+jwt",
      "kid": "devidp"
    }
    ```

1. View the Payload

    ```bash
    echo -n $TOKEN | cut -d '.' -f 2 | base64 -d | jq
    ```

    Generates output similar to:

    ```json
    {
      "jit_tenant_id": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "name": "my-token",
      "jit_tier": "FREE",
      "jti": "CCIH_QsZsM6FKzwBR6L5Z",
      "sub": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "iat": 1695254038,
      "exp": 1695257698,
      "client_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "iss": "https://app.datatrails.ai/appidpv1",
      "aud": "https://app.datatrails.ai/archivist"
    }
    ```
