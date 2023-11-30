---
title: "Quickstart: SCITT for Supply Chains (Preview)"
description: "Getting Started with SCITT, enabling Software Supply Chain scenarios (Preview)"
lead: "Push a collection of Supply Chain Statements using SCITT APIs"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 112
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
1. create and register an SBOM for the artifact
1. create and register an attestation for the artifact
1. query a collection of statements about the artifact

## Prerequisites

- [A DataTrails subscription](https://app.datatrails.ai/signup)
- [DataTrails sample code](#datatrails-sample-code)
- [SBOM Tool][sbom-tool]
- [Environment Configuration](#environment-configuration)

### DataTrails Sample Code

The Quickstart uses existing samples and scripts to focus on the SCITT APIs.

Clone the [DataTrails SCITT Examples](https://github.com/datatrails/datatrails-scitt-samples) repository to copy those files to your environment.

  ```shell
  git clone https://github.com/datatrails/datatrails-scitt-samples.git

  cd datatrails-scitt-samples
  ```

## Environment Configuration

1. Create a Python Virtual Environment for the sample scripts and install the dependencies

    ```shell
    python -m  venv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt
    ```

1. To ease copying and pasting commands, update any variables to fit your environment

  ```shell
  ISSUER=sample.sysnation.dev
  SIGNING_KEY=my-signing-key.pem
  SIGNED_STATEMENT_FILE=signed-statement-sbom.txt
  ```

1. Create a [bearer_token](/developers/developer-patterns/getting-access-tokens-using-app-registrations) stored as a file, in a secure local directory with 0600 permissions.

## Create a Signing Key

{{< note >}}
If you already have a COSE Key, skip ahead to [Register a SBOM for the Artifact](#register-a-sbom-for-the-artifact)
{{< /note >}}

There are multiple methods to create a signed statement, for methods other than using a basic signing key, see: _(TODO: link to supporting docs)
_(TODO: link to supported DataTrails Signing Keys\)_<br>
For the Quickstart, create a testing [COSE Key](https://cose-wg.github.io/cose-spec/#key-structure) which DataTrails will cryptographically validate upon registration

  ```shell
  openssl ecparam -name prime256v1 -genkey -out $SIGNING_KEY
  ```

## Register a SBOM for the Artifact

When registering statements about an artifact, a common identifier (Feed) is required to correlate a collection of statements.

The example generates an [SPDX SBOM](https://spdx.dev/), which generates a [Document Namespace](https://spdx.github.io/spdx-spec/v2.2.2/document-creation-information/#65-spdx-document-namespace-field) field which is used for the `CWT_Claims subject` property.

_\<TODO: Add a doc for creating identifiers>_

1. Using the [SBOM Tool](https://github.com/microsoft/sbom-tool), generate an SPDX SBOM for `artifact.js`

    ```bash
    sbom-tool generate -D true \
      -b scitt/artifacts \
      -ps scitt-community \
      -pn scitt-nodejs-example -pv 0.0.0 \
      -nsb https://scitt.io/examples
    ```

    [More info for the SPDX sbom-tool](https://github.com/microsoft/sbom-tool/blob/main/docs/sbom-tool-arguments.md)
1. Capture the Document Namespace for the SCITT `subject`

    ```shell
    FEED=$(cat scitt/artifact/_manifest/spdx_2.2/manifest.spdx.json | jq -r .documentNamespace)
    ```

1. Create a Signed Statement for the SPDX SBOM

    ```shell
    python scitt/create_signed_statement.py \
      --signing-key-file $SIGNING_KEY \
      --issuer $ISSUER \
      --feed $FEED \
      --content-type application/spdx+json \
      --payload scitt/artifacts/_manifest/spdx_2.2/manifest.spdx.json \
      --output-file signed-statement-sbom.cbor

1. Register the SBOM

    ```shell
    SIGNED_STATEMENT=`cat $SIGNED_STATEMENT_FILE`
    curl -X POST -H "Authorization: Bearer $TOKEN" -d '{"statement":"'$SIGNED_STATEMENT'"}' https://app.datatrails.ai/archivist/v1/publicscitt/entries
    ```

1. Retrieve a SCITT Receipt

    ```shell
    statement-get-receipt.py $ENTRY_ID
    ```

## Register an Attestation

Create an Attestation that provides the artifacts compliance to the \<foo> specification

1. Create the Attestation

    ```shell
    cat > attestation.json <<EOF
    {
      "compliance": [
        {
          "name": "standard-alpha",
          "value": "true"
        },
        {
          "name": "standard-beta",
          "value": "false"
        }
      ]
    }
    EOF
    ```

1. Create a Signed Statement for the attestation

    ```shell
    python scitt/create_signed_statement.py \
      --signing-key-file $SIGNING_KEY \
      --issuer $ISSUER \
      --feed $FEED \
      --content-type application/json \
      --payload attestation.json \
      --output-file signed-statement-attestation.cbor

1. Register the SBOM

    ```shell
    ENTRY_ID=$(statement-register.py \
      issuer $ISSUER \
      signing-key $SIGNING_KEY \
      feed $FEED \
      payload artifacts/_manifest/spdx_2.2/manifest.spdx.json \
      content-type application/spdx+json)
    ```

## Retrieve Statements for the Artifact

The power of SCITT is the ability to retrieve the history of statements made for a given artifact.
By querying the series of statements, consumers can verify who did what and when for a given artifact.

1. Query DataTrails for the collection of statements

    ```shell
    curl https://app.datatrails.ai/archivist/v2/publicassets/-/events?event_attributes.feed_id={{feed}}
    ```

To filter on specific content types, such as what SBOMs have been registered, or which issuers have made statements, see \<TODO: here>

## Summary

The quickstart created a collection of statements for a given artifact.
Over time, as new information is available, authors can publish new statements which verifiers and consumers can benefit from.
There are no limits to the types of additional statements that may be registered, which may include new vulnerability information, notifications of new versions, end of life (EOL) notifications, or more.
By using the content-type parameter, verifiers can filter to specific types, and/or filter statements by the issuer.

For more information:

- [SCITT.io](SCITT.io)
- [DataTrails SCITT API Reference](TBD)

[sbom-tool]:  https://github.com/microsoft/sbom-tool
