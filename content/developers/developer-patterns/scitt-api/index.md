---
title: "Quickstart: SCITT Statements (Preview)"
description: "Getting Started with SCITT: creating a collection of statements  (Preview)"
lead: "How to push a collection of Statements using SCITT APIs"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 110
toc: true
aliases: 
  - /docs/developer-patterns/scitt-api/
---

{{< caution >}}
The SCITT API is currently in preview and subject to change
{{< /caution >}}

The **S**upply **C**hain **I**ntegrity, **T**ransparency and **T**rust (SCITT) initiative is a set of [IETF standards](https://datatracker.ietf.org/group/scitt/documents/) for managing the compliance and auditability of goods and services across end-to-end supply chains.
SCITT supports the ongoing verification of goods and services where the authenticity of entities, evidence, policy, and artifacts can be assured and the actions of entities can be guaranteed to be authorized, non-repudiable, immutable, and auditable.

To assure insights to supply chain artifacts are current, the SCITT APIs provide a correlation of statements, allowing verifiers to view a full history of statements.
This includes previously registered statements, and newly registered statements providing the most up to date insights.

This quickstart will:

1. create, or use an existing a key to sign a collection of statements about an artifact
1. create and register a statement for the artifact
1. create and register an attestation for the artifact
1. query a collection of statements about the artifact

## Prerequisites

- [A DataTrails subscription](https://app.datatrails.ai/signup) with a [Token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) for API access
- [DataTrails sample code](#datatrails-sample-code)
- [Python](https://www.python.org/downloads/) to run the samples
- [Environment Configuration](#environment-configuration)

### DataTrails Sample Code

The Quickstart uses existing samples and scripts to focus on the SCITT APIs.

Clone the [DataTrails SCITT Examples](https://github.com/datatrails/datatrails-scitt-samples) repository to copy those files to your environment.

  ```bash
  git clone https://github.com/datatrails/datatrails-scitt-samples.git && \
  cd datatrails-scitt-samples
  ```

## Environment Configuration

1. Create a Python Virtual Environment for the sample scripts and install the dependencies

    ```bash
    python -m  venv venv && \
    source venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt
    ```

1. To ease copying and pasting commands, update any variables to fit your environment

    ```bash
    # your identity
    ISSUER="sample.synsation.io"

    # signing key to sign the SCITT Statements
    SIGNING_KEY="my-signing-key.pem"

    # File representing the signed statement to be registered
    SIGNED_STATEMENT_FILE="signed-statement.cbor"

    # Subject is a property used to correlate a collection of statements about an artifact
    SUBJECT="my-product-id"
    ```

## Create a Signing Key

{{< note >}}
If you already have a COSE Key, skip ahead to [Generating a Payload](#generating-a-payload)
{{< /note >}}

For the Quickstart, create a testing [COSE Key](https://cose-wg.github.io/cose-spec/#key-structure) which DataTrails will cryptographically validate upon registration

  ```bash
  openssl ecparam -name prime256v1 -genkey -out $SIGNING_KEY
  ```

## Generate a Payload

Create any payload you wish to register on DataTrails. JSON based payloads are indexed for query capabilities.

{{< note >}}
The current version of the DataTrails SCITT API is limited to JSON payloads.
This will be relaxed in a future release
{{< /note >}}

```bash
cat > payload.json <<EOF
{
    "author": "fred",
    "title": "my biography",
    "reviews": "mixed"
}
EOF
```

## Create a COSE Signed Statement

Using the `payload.json` file, create a COSE Signed Statement

```bash
python scitt/create_signed_statement.py \
  --signing-key-file $SIGNING_KEY \
  --issuer $ISSUER \
  --feed $SUBJECT \
  --content-type "application/json" \
  --payload-file payload.json \
  --output-file $SIGNED_STATEMENT_FILE
```

## Register the SCITT Statement on DataTrails

Submit the Signed Statement to DataTrails, using the credentials in the `bearer-token.txt`

  ```bash
  OPERATION_ID=$(curl -X POST -H @$HOME/.datatrails/bearer-token.txt \
                  --data-binary @$SIGNED_STATEMENT_FILE \
                  https://app.datatrails.ai/archivist/v1/publicscitt/entries \
                  | jq -r .operationID)
  ```

1. Monitor for the Statement to be anchored. Once `"status": "succeeded"`, proceed to the next step

    ```bash
    ENTRY_ID=$(python scitt/check_operation_status.py --operation-id $OPERATION_ID)
    ```

1. Retrieve a SCITT Receipt

    ```bash
    
    curl -H @$HOME/.datatrails/bearer-token.txt \
      https://app.datatrails.ai/archivist/v1/publicscitt/entries/$ENTRY_ID/receipt \
      -o receipt.cbor
    ```

## Retrieve Statements for the Artifact

The power of SCITT is the ability to retrieve the history of statements made for a given artifact.
By querying the series of statements, consumers can verify who did what and when for a given artifact.

1. Query DataTrails for the collection of statements

    ```bash
    curl -H @$HOME/.datatrails/bearer-token.txt \
      https://app.datatrails.ai/archivist/v2/publicassets/-/events?event_attributes.feed_id=$SUBJECT | jq
    ```

{{< note >}}
Coming soon: Filter on specific content types, such as what SBOMs have been registered, or which issuers have made statements.
{{< /note >}}

## Summary

The quickstart created a collection of statements for a given artifact.
Over time, as new information is available, authors can publish new statements which verifiers and consumers can benefit from.
There are no limits to the types of additional statements that may be registered, which may include new vulnerability information, notifications of new versions, end of life (EOL) notifications, or more.
By using the content-type parameter, verifiers can filter to specific types, and/or filter statements by the issuer.

For more information:

<!-- - [DataTrails SCITT API Reference](TBD) -->
- [SCITT.io](SCITT.io)
