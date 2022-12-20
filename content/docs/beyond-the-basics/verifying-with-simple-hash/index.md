---
 title: "Verifying Assets and Events with Simple Hash"
 description: "Ensure Asset and Event Data Has Not Changed"
 lead: "Ensure Asset and Event Data Has Not Changed"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   docs:
     parent: "beyond-the-basics"
 weight: 44
 toc: true
---

Verifying your Simple Hash events provides an additional layer of assurance to your data, so you can ensure the information you have at a given time has not changed.

To verify your data, you may use the [RKVST Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python), available on GitHub. 

Please note that with Simple Hash, events are committed to the RKVST blockchain as a batch. Events with the blue tick have been committed to the blockchain as part of a batch, and will have a `Transaction ID`. With the free tier of RKVST, Simple Hash batched commits happen every 30 days by default. If the tick mark is grey, your event has been confirmed in the system but not yet committed to the blockchain. **Your event(s) must have a blue tick for transaction details to be available for data verification.**

## Step-by-Step Guide for Using the Simple Hash Tool 

1. Retrieve your transaction information. This will give you the inputs you need in later steps to check the hash for that batch of events. 

{{< tabs name="retrieve-transaction-info" >}}
{{{< tab name="UI" >}}
Select `Auditor View` from the sidebar and select a `Transaction` from the Events Overview List.
{{< img src="AuditorView.png" alt="Rectangle" caption="<em>Auditor View</em>" class="border-0" >}}

Copy the `start time` and `end time` from the Simple Hash Details. These will be used as inputs to the [RKVST Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python).

{{< img src="SimpleHashDetails.png" alt="Rectangle" caption="<em>Simple Hash Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="Command Line" >}}
The [Blockchain API](../../api-reference/blockchain-api/) allows you to fetch transactions for an event. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.

Using the Event ID as a parameter, run the following command: 

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v1alpha2/blockchain/assets/<asset-id>/events/<event-id>
```

This will return a list of matching blockchain transactions, as well as the `simple_hash_details`. Copy the `start_time` and `end_time` values to be used as inputs to the [RKVST Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python).

{{< /tab >}}
{{< /tabs >}}

2. Use the [RKVST Simple Hash tool](https://github.com/rkvst/rkvst-simplehash-python) to generate the hash of your events. 

{{< tabs name="simple-hash-script" >}}
{{{< tab name="Python" >}}
Use Python pip utility to install the `rkvst-simplehash` package. This package is supported for Python versions 3.7, 3.8, 3.9, and 3.10.

```bash
python3 -m pip install rkvst-simplehash
```

You may then use the code to recreate the hash, using your [`BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) as the `auth_token` and the `start_date` and `end_date` copied in the last step:

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
        "app.rkvst.io",
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
Enter the query information you copied in the last step and run the command. See instructions for [creating your `BEARER_TOKEN_FILE`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) here.

Commands can be executed anywhere using a virtual environment and published wheel. Credentials are stored in files within the credentials directory. 

Using an [`auth token`](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/) directly: 

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
**Note:** If you are using an environment other than `app.rkvst.io`, add the URL with the `--fqdn` option. For example, `--fqdn "app.rkvst-poc.io"`.
{{< /note >}}

{{< /tab >}}
{{< /tabs >}}

3. Compare the hash from your `Transaction Details` to the hash generated by the tool. If they match, your event history has not changed. 