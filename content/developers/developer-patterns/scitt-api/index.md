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

{{< note >}}
The following Quickstart aligns with the [SCITT Architecture Draft 07](https://ietf-wg-scitt.github.io/draft-ietf-scitt-architecture/draft-ietf-scitt-architecture.html)
{{< /note >}}

{{< caution >}}
The DataTrails SCITT API is currently in preview and subject to change
{{< /caution >}}

The **S**upply **C**hain **I**ntegrity, **T**ransparency and **T**rust (SCITT) initiative is a set of [IETF standards](https://datatracker.ietf.org/group/scitt/documents/) for managing the compliance and auditability of goods and services across end-to-end supply chains.
SCITT supports the ongoing verification of goods and services where the authenticity of entities, evidence, policy, and artifacts can be assured and the actions of entities can be guaranteed to be authorized, non-repudiable, immutable, and auditable.

To assure insights to supply chain artifacts are current, the SCITT APIs provide a correlation of statements, allowing verifiers to view a full history of statements for a given artifact.
This includes previously registered statements, and newly registered statements providing the most up to date insights.

This quickstart will:

1. create, or use an existing a key to sign a collection of statements about an artifact
1. create and register a statement for the artifact
1. query the collection of statements about the artifact, using the subject property

## Prerequisites

- [A DataTrails subscription](https://app.datatrails.ai/signup)
- [DataTrails sample code](#datatrails-sample-code)
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

    # File representing the statement being registered
    STATEMENT_FILE="statement.json"
    
    # File representing the signed statement to be registered
    SIGNED_STATEMENT_FILE="signed-statement.cbor"

    # An Issuer created unique identifier used to correlate statements about an artifact
    SUBJECT="synsation.io/products/product42/v1.0.1.12"
    ```

1. Create a [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) stored as a file, in a secure local directory with 0600 permissions.

## Create a Signing Key

The following Quickstart aligns with the [SCITT Architecture Draft 07](https://ietf-wg-scitt.github.io/draft-ietf-scitt-architecture/draft-ietf-scitt-architecture.html)
{{< note >}}
If you already have a COSE Key, skip ahead to [Generating a Statement](#generating-a-statement)
{{< /note >}}

For the Quickstart, create a testing [COSE Key](https://cose-wg.github.io/cose-spec/#key-structure) which DataTrails will cryptographically validate upon registration

  ```bash
  openssl ecparam -name prime256v1 -genkey -out $SIGNING_KEY
  ```

## Generating a Statement

1. Create a simple json statement

    ```bash
    cat > $STATEMENT_FILE <<EOF
    {
        "build-server": "22",
        "test-results": "passed",
        "compliance-22": "compliant"
    }
    EOF
    ```

1. Optionally save the statement in the [DataTrails Events Attachments API](/developers/api-reference/events-api/#adding-attachments)

   **INTERNAL-DEV-NOTE**: this is likely a curl/post command, capturing the attachment ID to save as a URL.

    ```bash
    python scitt/attach_statement.py \
      --subject $SUBJECT \
      --content-type "application/json" \
      --statement-file statement.json

    ATTACHMENT_URI=<something-something>
    ```

1. Create a SCITT Signed Statement for the `statement.json` file

    {{< note >}}
    In this version, signed statements are always registered as hashes of the statement file (Equivalent to:`--payload-type statement-hash`), which is the default and only currently supported parameter.
  
  A `location-hint` parameter stores a reference to a location the statement may be stored.
  
  Verification is based on the hash of the file, which can be verified from any location.
    {{< /note >}}

    ```bash
    python scitt/create_signed_statement.py \
      --signing-key-file $SIGNING_KEY \
      --issuer $ISSUER \
      --subject $SUBJECT \
      --content-type "application/json" \
      --location-hint $ATTACHMENT_URI \
      --statement-file statement.json \
      --output-file $SIGNED_STATEMENT_FILE
    ```

1. Register the Statement

    ```bash
    OPERATION_ID=$(curl -X POST -H @$HOME/.datatrails/bearer-token.txt \
                    --data-binary @$SIGNED_STATEMENT_FILE \
                    https://app.datatrails.ai/archivist/v1/publicscitt/entries \
                    | jq -r .operationID)
    ```

    {{< note >}}
    **DEV-NOTE:** Registering the statement will create a DataTrails event with the following attributes:

  | Source                     | DataTrails Event Attribute Name | DataTrails Event Attribute Value |
  | -------------------------- | ------------------------------- | -------------------------------- |
  | SCITT content-type         | scitt_content-type              | application/json                 |
  | DataTrails Attachments API | arc_statement-location-hint     | https://app.datatrails.ai/assets/8ee550dc-d896-4d47-a8d0-aba9b1052007 |
  | SCITT cwt-claims.iss       | scitt_issuer                    | sample.synsation.io              |
  | statement file hash        | scitt_statement-payload         | uGunRfEH38lpqyJQbMsQStwtn9XxW/nlMKp3HReY5AE= |
  | SCITT cwt-claims.sub       | scitt_subject                   | synsation.io/products/product42/v1.0.1.12 |

  All SCITT mapped properties have a preface of `scitt_`, while DataTrails created attributes will use the historic `arc_` preface.
    {{< /note >}}

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
      https://app.datatrails.ai/archivist/v2/publicassets/-/events?event_attributes.subject=$SUBJECT | jq
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
