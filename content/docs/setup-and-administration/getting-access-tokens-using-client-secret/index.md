---
title: "Getting Access Tokens Using Client Secret"
description: "Generating Tokens for RKVST"
lead: "Generating Tokens for RKVST"
date: 2021-06-16T11:13:48+01:00
lastmod: 2021-06-16T11:13:48+01:00
draft: false
images: []
menu: 
  docs:
    parent: "setup-and-administration"
weight: 13
toc: true
---

Having completed the steps at [App Registration](../configuring-appregistrations-for-non-interactive-use/), and taken note of the `CLIENT ID` and the `SECRET`, a token can be obtained with the following command.

Replace `${CLIENTID}` with the application id, and `${SECRET}` with your secret from the application registration; `${FQDN}` is the FQDN of the RKVST SaaS.

```bash
$ RESPONSE=$(curl \
    https://${FQDN}/iam/v1/appidp/token \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${CLIENTID}" \
    --data-urlencode "client_secret=${SECRET}")

$ TOKEN=$(echo -n $RESPONSE | jq .access_token | tr -d '"')
```

## Testing Access
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
