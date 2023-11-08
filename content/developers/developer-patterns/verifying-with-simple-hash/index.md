---
 title: "Verifying Assets and Events with Simple Hash"
 description: "Ensure Asset and Event Data Has Not Changed"
 lead: "Ensure Asset and Event Data Has Not Changed"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   developers:
     parent: "developer-patterns"
 weight: 34
 toc: true
 aliases: 
  - /docs/beyond-the-basics/verifying-with-simple-hash/
---

Verifying your Simple Hash events provides an additional layer of assurance to your data, so you can ensure the information you have at a given time has not changed.

To verify your data, you may use the [DataTrails Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python), available on GitHub.

Please note that with Simple Hash, Events are committed to the DataTrails blockchain as a batch. Events with the blue tick have been committed to the blockchain as part of a batch, and will have a `Transaction ID`. With the free tier of DataTrails, Simple Hash batched commits happen every 30 days by default. For Public Assets, batched commits happen each day. If the tick mark is grey, your event has been confirmed in the system but not yet committed to the blockchain. **Your event(s) must have a blue tick for transaction details to be available for data verification.**

## Step-by-Step Guide for Using the Simple Hash Tool

1. Retrieve your transaction information. This will give you the inputs you need in later steps to check the hash for that batch of Events.

{{< note >}}
For Public Assets, retrieve the transaction information from the public view of the Asset and Events, or from the [Public Assets Endpoint](/developers/api-reference/public-assets-api/).
{{< / note >}}

{{< tabs name="retrieve-transaction-info" >}}
{{{< tab name="UI" >}}
Select `Audit/Filters` from the sidebar and select a `Transaction` from the Events Overview List.
{{< img src="AuditSearch.png" alt="Rectangle" caption="<em>Audit/Search</em>" class="border-0" >}}

Copy the `start time` and `end time` from the Simple Hash Details. These will be used as inputs to the [DataTrails Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python).

{{< img src="SimpleHashDetails.png" alt="Rectangle" caption="<em>Simple Hash Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="Command Line" >}}
The [Blockchain API](/developers/api-reference/blockchain-api/) allows you to fetch transactions for an Event. See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

Using the Event ID as a parameter, run the following command:

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v1alpha2/blockchain/assets/<asset-id>/events/<event-id>
```

This will return a list of matching blockchain transactions, as well as the `simple_hash_details`. Copy the `start_time` and `end_time` values to be used as inputs to the [DataTrails Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python).

{{< /tab >}}
{{< /tabs >}}

1. Use the [DataTrails Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python) to generate the hash of your Events.

{{< tabs name="simple-hash-script" >}}
{{{< tab name="Python" >}}
Use Python pip utility to install the `datatrails-simplehash` package. This package is supported for Python versions 3.7, 3.8, 3.9, and 3.10.

```bash
python3 -m pip install datatrails-simplehash
```

You may then use the code to recreate the hash, using your [`BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) as the `auth_token` and the `start_date` and `end_date` copied in the last step:

```python
from rkvst_simplehash.v1 import (
    anchor_events,
    SimpleHashError,
)

with open("credentials/token", mode="r", encoding="utf-8") as tokenfile:
    auth_token = tokenfile.read().strip()

try:
    simplehash = anchor_events(
        "2022-10-07T07:01:34Z",
        "2022-10-16T13:14:56Z",
        "app.datatrails.ai",
        auth_token,
    )
except SimpleHashError as ex:
    print("Error", ex)

else:
    print("simplehash=", simplehash)
```

Run your Python file to return the hash value.

{{< note >}}
**Note:** SimpleHashClientAuthError is raised if the auth token is invalid or expired.
{{< /note >}}

{{< /tab >}}
{{< tab name="Command Line" >}}
Enter the query information you copied in the last step and run the command. See instructions for [creating your `BEARER_TOKEN_FILE`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) here.

Commands can be executed anywhere using a virtual environment and published wheel. Credentials are stored in files within the credentials directory.

Using an [`auth token`](/developers/developer-patterns/getting-access-tokens-using-app-registrations/) directly:

```bash
python3 -m venv simplehash-venv
source simplehash-venv/bin/activate
python3 -m pip install -q rkvst_simplehash

rkvst_simplehashv1 \
    --auth-token-file "credentials/token" \
    --start-time "2022-11-16T00:00:00Z" \
    --end-time "2022-11-17T00:00:00Z"

deactivate
rm -rf simplehash-venv
```

Using a `Client ID` and `Client Secret`:

```bash
python3 -m venv simplehash-venv
source simplehash-venv/bin/activate
python3 -m pip install -q rkvst_simplehash

CLIENT_ID=$(cat credentials/client_id)
rkvst_simplehashv1 \
    --client-id "${CLIENT_ID}" \
    --client-secret-file "credentials/client_secret" \
    --start-time "2022-11-16T00:00:00Z" \
    --end-time "2022-11-17T00:00:00Z"

deactivate
rm -rf simplehash-venv
```

{{< note >}}
**Note:** If you are using an environment other than `app.datatrails.ai`, add the URL with the `--fqdn` option. For example, `--fqdn "app.datatrails-poc.ai"`.
{{< /note >}}

{{< /tab >}}
{{< /tabs >}}

1. Compare the hash from your `Transaction Details` to the hash generated by the tool. If they match, your Event history has not changed.
