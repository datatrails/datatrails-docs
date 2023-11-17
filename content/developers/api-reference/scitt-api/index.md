---
title: "SCITT API (Preview)"
description: "SCITT API Reference (Preview)"
lead: "SCITT API Reference (Preview)"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu: 
  developers:
    parent: "api-reference"
weight: 112
toc: true
aliases: 
  - /docs/api-reference/scitt-api/
---

{{< note >}}
The SCITT API is currently in preview and subject to change.
{{< /note >}}

The **S**upply **C**hain **I**ntegrity, **T**ransparency and **T**rust (SCITT) initiative is a set of [IETF standards](https://datatracker.ietf.org/group/scitt/documents/) for managing the compliance and auditability of goods and services across end-to-end supply chains.
SCITT supports the ongoing verification of goods and services where the authenticity of entities, evidence, policy, and artifacts can be assured and the actions of entities can be guaranteed to be authorized, non-repudiable, immutable, and auditable.

DataTrails provides a SCITT implementation for developers looking to integrate Auditing and Compliance capabilities into their services.

## Dependencies

The following are required to complete this walkthrough:

- [A DataTrails subscription](https://app.datatrails.ai/signup)
- [DataTrails scripts](#data-trails-scripts)
- [SBOM Tool](https://github.com/microsoft/sbom-tool)
- [Sample Code](#sample-code)

### Data Trails Scripts

TODO: Add details for installing the datatrails scripts

### Sample Code

Create a directory and clone the [SCITT Examples](https://github.com/scitt-community/scitt-examples) repository

```bash
mkdir datatrails-scitt-demo
cd datatrails-scitt-demo/
git clone https://github.com/scitt-community/scitt-examples.git
cd scitt-examples/nodejs/
```

## Sample

The following will accomplish the following tasks:

1. Create a signing key
1. Register provenance for a new artifact
1. Create and register an SBOM for the artifact
1. Create an register attestation for the artifact
1. Query DataTrails for the statements about the artifact

## Create a Signing Key

DataTrails supports multiple signing keys.
(TODO: link to supported DataTrails Signing Keys\)<br>
For a quick start, we'll create a jwk which DataTrails will cryptographically validate upon registration.

1. Create a local signing key

    ```shell
    dt-key-create.py <parameters>
    ```

## Register Provenance for an Artifact

When registering statements about an artifact, a common identifier is required to corelate a series of statements.
A SCITT `CWT_Claims subject` property captures the identifier.

The example uses SPDX, which generates a [Document Namespace](https://spdx.github.io/spdx-spec/v2.2.2/document-creation-information/#65-spdx-document-namespace-field) field which is used for the `subject` property.

_\<TODO: Add a doc for creating unique identifiers>_

1. Generate an SPDX SBOM for `artifact.js`

    ```bash
    sbom-tool generate -D true \
      -b artifacts \
      -ps scitt-community \
      -pn scitt-nodejs-example -pv 0.0.0 \
      -nsb https://scitt.io/examples
    ```

    [More info for the SPDX sbom-tool](https://github.com/microsoft/sbom-tool/blob/main/docs/sbom-tool-arguments.md)
1. Capture the Document Namespace for the SCITT `subject`

    ```shell
    SUBJECT=$(cat artifacts/_manifest/spdx_2.2/manifest.spdx.json | jq -r .documentNamespace)
    ```

1. Create a Signed Statement for the SPDX SBOM

    ```shell
    dt-statement-create.py \
      issuer <identity-reference> \
      subject $SUBJECT \
      payload artifacts/_manifest/spdx_2.2/manifest.spdx.json \
      content-type application/spdx+json \
      output signed-statement.cbor
    ```

1. Register the SPDX SBOM for the artifact

    ```shell
    ENTRY_ID=$(dt-register-signed-statement.py signed-statement.cbor)
    ```

1. **COMBINED?:** Sign and Register the SBOM<br>
    An alternative to the above two commands

    ```shell
    ENTRY_ID=$(dt-statement-register.py \
      issuer <identity-reference> \
      subject $SUBJECT \
      payload artifacts/_manifest/spdx_2.2/manifest.spdx.json \
      content-type application/spdx+json)
    ```

1. Retrieve a SCITT Receipt

    ```shell
    dt-statement-get-receipt.py $ENTRY_ID
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

1. Sign and Register the Attestation

    ```shell
    ENTRY_ID=$(dt-statement-register.py \
      issuer <identity-reference> \
      subject $SUBJECT \
      payload attestation.json \
      content-type attestation/example )
    ```

## Retrieve Statements for the Artifact

The power of SCITT is the ability to retrieve the history of statements made for a given artifact.
By querying the series of statements, consumers can verify who did what and when for a given artifact.

1. Query DataTrails for the collection of statements

    ```shell
    dt-feed-get.py $SUBJECT
    ```

To filter on specific content types, such as what SBOMs have been registered, or which issuers have made statements, see \<TODO: here>
