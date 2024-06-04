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

    # Content type of the STATEMENT_FILE
    CONTENT_TYPE="application/json"

    # File representing the statement being registered
    STATEMENT_FILE="statement.json"
    
    # File representing the signed statement to be registered
    STATEMENT_SIGNED_FILE="statement-signed.cbor"

    # An Issuer created unique identifier used to correlate statements about an artifact
    SUBJECT="synsation.io/products/product42/v1.0.1.12"
    ```

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

DataTrails registers Signed SCITT Statements, providing users with the option to index the statement into Event Attributes. Larger statements may be referenced to existing storage solutions or saved as DataTrails Attachments.

- **Statements of 1mb or less** may be stored within the SCITT Envelope.  
DataTrails will index json documents into [event attributes](/developers/api-reference/events-api/).
- **Statements greater than 1mb** will be stored as detached statements.  
Detached statements may be stored with the [DataTrails Attachments API](/developers/api-reference/events-api/#adding-attachments), or use an existing storage service.  
When registering detached statements, a hash of the statement, the location (uri) and content-type will be signed, providing a tamper evident record for the Statement.

1. Create a simple statement, in json format which DataTrails will index into Event Attributes.

    ```bash
    cat > $STATEMENT_FILE <<EOF
    {
        "build-server": "22",
        "test-results": "passed",
        "compliance-22": "compliant"
    }
    EOF
    ```

1. Optionally save the statement as a DataTrails Attachment

    If you already have an existing storage solution, skip to the next step.

    {{< note >}}
    **INTERNAL-DEV-NOTE**: this is likely a curl/post command, capturing the attachment ID to save as a URL.
    {{< /note >}}

    ```bash
    python scitt/attach_statement.py \
      --subject $SUBJECT \
      --content-type $CONTENT_TYPE \
      --statement-file $STATEMENT_FILE

    ATTACHMENT_URI=<something-something>
    ```

## Create an Attached SCITT Signed Statement File

If your statement is larger than 1mb, or you already have the statement stored externally:

- SPDX/Cyclone DX SBOM stored in sbom.sh
- A manifest of an OCI Artifact stored in an OCI Registry
- AI Model Card stored on a file share

Skip to [Create a Detached SCITT Signed Statement](#create-a-detached-scitt-signed-statement)

If the `$STATEMENT_FILE` file is less than 1mb (such as the example in this quickstart) it can be saved within the SCITT Envelope.

The `create_signed_statement.py` sample script will construct a SCITT Signed Statement, with the contents of `$STATEMENT_FILE` encoded within the SCITT Envelope, saved as `$STATEMENT_SIGNED_FILE`

```bash
python scitt/create_signed_statement.py \
  --signing-key-file $SIGNING_KEY \
  --issuer $ISSUER \
  --subject $SUBJECT \
  --content-type $CONTENT_TYPE \
  --statement-file $STATEMENT_FILE \
  --statement-type "attached" \
  --output-file $STATEMENT_SIGNED_FILE
```

## Create a Detached SCITT Signed Statement

The `create_signed_statement.py` sample script will construct a SCITT Signed Statement, creating a hash of the `$STATEMENT_FILE` file, stored in the protected header.
The `statement-type` is set to `detached`, which sets the Signed Statement payload protected header to `null`.
An optional `location-hint` protected header property provides verifiers an option for where they may find the statement.

The `$ATTACHMENT_URI` may be set from the step above for saving as a DataTrails Attachment, or set to the existing storage location.

Alternatives may be:

```bash
#AI Model Card, stored on huggingface
ATTACHMENT_URI=https://huggingface.co/00BER/dc-weather-prediction

#SBOM Stored on sbom.sh
ATTACHMENT_URI=https://sbom.sh/retrieve/45c223ed-0905-4fe2-b57c-7d7edb21cf86

#Docker Scout Security scan for a container image stored on Docker Hub
ATTACHMENT_URI=docker.io/stevelasker/synsation-web@ sha256:a18b8db518a1017ebb46609c5fcae3cfa8206cf475db6cc8aa3c53883ca77795
```

```bash
python scitt/create_signed_statement.py \
  --signing-key-file $SIGNING_KEY \
  --issuer $ISSUER \
  --subject $SUBJECT \
  --content-type $CONTENT_TYPE \
  --statement-file $STATEMENT_FILE \
  --statement-type "detached" \
  --location-hint $ATTACHMENT_URI \
  --output-file $STATEMENT_SIGNED_FILE
```

## Register the SCITT Statement on DataTrails

1. Submit the Signed Statement to DataTrails, using the credentials in the `bearer-token.txt`

    ```bash
    OPERATION_ID=$(curl -X POST -H @$HOME/.datatrails/bearer-token.txt \
                    --data-binary @$STATEMENT_SIGNED_FILE \
                    https://app.datatrails.ai/archivist/v1/publicscitt/entries \
                    | jq -r .operationID)
    ```

    {{< note >}}
    **DEV-NOTE:** Registering the statement will create a DataTrails event with the following attributes:

  | DataTrails Event Attribute  | Source               | DataTrails Event Attribute Value |
  | --------------------------- | -------------------- | -------------------------------- |
  | scitt_issuer                | SCITT cwt-claims.iss | sample.synsation.io              |
  | scitt_subject               | SCITT cwt-claims.sub | synsation.io/products/product42/v1.0.1.12 |
  | scitt_content-type          | SCITT content-type   | application/json                 |
  | arc_statement-location-hint | Parameter passed in  | https://app.datatrails.ai/assets/8ee550dc-d896-4d47-a8d0-aba9b1052007 |
  | arc_statement-hash          | statement file hash  | uGunRfEH38lpqyJQbMsQStwtn9XxW/nlMKp3HReY5AE= </br> stored as binary, shown as base64|
  | arc_hash-algorithm          | hash-algorithm       | SHA256                           |

  TODO: add CBOR example

  All SCITT mapped properties have a preface of `scitt_`,

  All DataTrails created attributes will use the historic `arc_` preface.
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
