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

To assure insights to supply chain artifacts are current, the SCITT APIs provide a correlation of statements for a specific artifact, allowing newer information to be registered for the most up to date insights.

This quickstart will:

1. create, or use an existing a key to sign a collection of statements about an artifact
1. create and register an SBOM for the artifact
1. create and register an attestation for the artifact
1. query a collection of statements about the artifact

## Prerequisites

- [A DataTrails subscription](https://app.datatrails.ai/signup)
- [DataTrails sample code](#datatrails-sample-code)
- [SBOM Tool](https://github.com/microsoft/sbom-tool)

### DataTrails Sample Code

Clone the [DataTrails SCITT Examples](https://github.com/datatrails/datatrails-scitt-samples) repository

```bash
git clone https://github.com/datatrails/datatrails-scitt-samples.git

cd datatrails-scitt-samples
```

## Create a Signing Key

{{< note >}}
If you already have a COSE Key, skip ahead to [Register a SBOM for the Artifact](#register-a-sbom-for-the-artifact)
{{< /note >}}

DataTrails supports multiple signing keys.
_(TODO: link to supported DataTrails Signing Keys\)_<br>
For a quickstart, we'll create a testing [COSE Key](https://cose-wg.github.io/cose-spec/#key-structure) which DataTrails will cryptographically validate upon registration

1. Create a local signing key

    ```shell
    openssl ecparam -name prime256v1 -genkey -out scitt-signing-key.pem
    ```

## Register a SBOM for the Artifact

When registering statements about an artifact, a common identifier is required to correlate a collection of statements.

When registering statements about an artifact, a common identifier is required to correlate a collection of statements. To accomplish this today, we use the feed property of the protected header

**_NOTE:_**  SCITT is an evolving standard and in the lastest work, a `CWT_Claims subject` property captures the identifier. And this platform will be aligning in a future release

The example generates an [SPDX SBOM](https://spdx.dev/), which generates a [Document Namespace](https://spdx.github.io/spdx-spec/v2.2.2/document-creation-information/#65-spdx-document-namespace-field) field which is used for the `CWT_Claims subject` property.

_\<TODO: Add a doc for creating unique identifiers>_

1. Using the [SBOM Tool](https://github.com/microsoft/sbom-tool), generate an SPDX SBOM for `artifact.js`

    ```bash
    sbom-tool generate -D true \
      -b scitt/artifact \
      -ps scitt-community \
      -pn scitt-nodejs-example -pv 0.0.0 \
      -nsb https://scitt.io/examples
    ```

    [More info for the SPDX sbom-tool](https://github.com/microsoft/sbom-tool/blob/main/docs/sbom-tool-arguments.md)
1. Capture the Document Namespace for the SCITT `subject`

    ```shell
    SUBJECT=$(cat scitt/artifact/_manifest/spdx_2.2/manifest.spdx.json | jq -r .documentNamespace)
    ```

1. Sign and Register the SBOM

    ```shell
    ENTRY_ID=$(statement-register.py \
      issuer scitt-signing-key.pem \
      subject $SUBJECT \
      payload artifacts/_manifest/spdx_2.2/manifest.spdx.json \
      content-type application/spdx+json)
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

1. Sign and Register the Attestation

    ```shell
    ENTRY_ID=$(statement-register.py \
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
    feed-get.py $SUBJECT
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
