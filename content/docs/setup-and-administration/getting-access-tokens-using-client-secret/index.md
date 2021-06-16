---
title: "Getting Access Tokens Using Client Secret"
description: ""
lead: ""
date: 2021-06-16T11:13:48+01:00
lastmod: 2021-06-16T11:13:48+01:00
draft: false
images: []
menu: 
  docs:
    parent: "setup-and-administration"
weight: 5
toc: true
---

Having completed the steps at [Application Registration](../configuring-azure-clients-for-non-interactive-access/), and taken note of the `Application ID` and the secret, a token can be obtained with the following command. 

Replace `${API_APP_ID}` with the application id, and `${API_APP_SECRET}` with your secret from the application registration; `${FQDN}` is the FQDN for your Jitsuin RKVST. 

`${TENANT}` is your directory id, see [how to locate your Tenant here](..registering-your-azure-active-directory-with-rkvst/#finding-your-tenant-id).

```bash
$ RESPONSE=$(curl \
    https://login.microsoftonline.com/${TENANT}/oauth2/token\
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=${API_APP_ID}" \
    --data-urlencode "client_secret=${API_APP_SECRET}" \
    --data-urlencode "resource=https://${FQDN}")

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


The following python script demonstrates how to safely obtain and verify a token.

6. Run the script like this, the example requires `Python 3`:

```shell
python3 check-token.py -t ${TENANT} -c ${API_APP_ID} -s ${API_APP_SECRET} -f ${FQDN}
```

Copy the following python code to `check-token.py`.

```python
#!/usr/bin/env python3

# REQUIRES Python 3.6
import sys
import argparse
import subprocess as sp
import urllib.parse
import base64
import json
import calendar
import datetime

verify_token=True
try:
    import jwcrypto
    import jwcrypto.jwk
    import jwcrypto.jwt
except ImportError:
    verify_token=False


def run():
    p = argparse.ArgumentParser( description=__doc__)

    p.add_argument("-T", "--token")
    p.add_argument("-t", "--tenant")
    p.add_argument("-c", "--client-id")
    p.add_argument("-s", "--client-secret")
    p.add_argument("-f", "--fqdn")

    args = p.parse_args()

    # Support checking a token provided 'as is' and also fetching and checking
    # a token using the expected customer configuration items

    token = args.token
    if token is None:
        secret = urllib.parse.quote(args.client_secret)
        resource = urllib.parse.quote("https://" + args.fqdn)

        data = f"grant_type=client_credentials&client_id={args.client_id}"
        data += f"&client_secret={secret}&resource={resource}"

        cmd = [
            "curl", "-X", "POST",
            "-HContent-Type: application/x-www-form-urlencoded",
            f"https://login.microsoftonline.com/{args.tenant}/oauth2/token",
            "-d", data]

        # Avoid the unpleasant curl output
        cp = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE, check=True)
        token = cp.stdout.decode()
        jdoc = json.loads(token)
        token = jdoc["access_token"]
        print("TOKEN:")
        print(token)

    header, payload, *sig = token.split('.')

    header = json.loads(base64.b64decode(header + "===").decode())
    print(json.dumps(header))

    payload = json.loads(base64.b64decode(payload + "===").decode())
    print(json.dumps(payload, indent=4, sort_keys=True))

    # Check that the 'aud' field matches the resource
    if args.fqdn and 'https://' + args.fqdn != payload["aud"]:
        print("Missing or unexepected aud", file=sys.stderr)
        return -1

    # Check that its issued by the expected tenancy
    if args.tenant and args.tenant not in payload["iss"]:
        print("Unexepected directory id in issuer (iss)", file=sys.stderr)

    # Check the Jitsuin RKVST roles are present
    roles = payload["roles"]
    if "archivist_administrator" not in roles and "guest" not in roles:
        print("Token is missing the required roles", file=sys.stderr)
        return -1

    # Check the freshly issued token has not expired and that the issue time is
    # sensible
    iat = int(payload["iat"])
    exp = int(payload["exp"])
    now = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    if now < iat:
        print(f"iat before 'now'. iat={iat}, now={now}", file=sys.stderr)
        return -1
    if now >= exp:
        print(
            f"now after 'exp', token expired "
            f"or invalid. now={now}, exp={exp}", file=sys.stderr)
        return -1

    # Get the IdP Open ID configuration
    cmd = [
        "curl", "-HAccept: application/json",
        f"{payload['iss']}/.well-known/openid-configuration"]
    cp = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE, check=True)

    oidconf = json.loads(cp.stdout.decode())

    # Fetch the keys for verification
    cmd = ["curl", "-HAccept: application/json", f"{oidconf['jwks_uri']}"]
    cp = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE, check=True)

    jwks = json.loads(cp.stdout.decode())
    key = None
    for k in jwks["keys"]:
        if k["kid"] == header["kid"]:
            key = k
            break
    if key is None:
        print(
            "Failed to find token verification key at issuer", file=sys.stderr)
        return -1

    if verify_token is False:
        print("Please install jwcrypto to verify your token")
        return 0

    jwk = jwcrypto.jwk.JWK(**key)
    jwt = jwcrypto.jwt.JWT()
    # If there is any problem with the token, this function will raise an
    # exception.
    jwt.deserialize(token, key=jwk)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except json.decoder.JSONDecodeError as e:
        print(f"json decoding error {str(e)}")
    except sp.CalledProcessError as cpe:
        print(cpe.output, file=sys.stderr)
    except KeyError as e:
        print(f"expected key missing {str(e)}", file=sys.stderr)
    except ValueError as e:
        print(str(e), file=sys.stderr)
    except Exception as e:
        print(str(e), file=sys.stderr)
    sys.exit(-1)
```


Delete the test secret once this test is completed.

{{< note >}}
Certificate based assertion of identity is fully supported. See `client_assertion_type` and `client_assertion` in the official [Azure documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-oauth2-client-creds-grant-flow>)
{{< /note >}}