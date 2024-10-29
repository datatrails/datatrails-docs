---
title: "SCITT vCon Template"
description: "Creating SCITT Signed Statements for vCons"
lead: "Register SCITT Signed Statements for vCon Updates"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "templates"
weight: 18
toc: true
aliases:
---
vCons safely and securely carry conversations from the network elements that create them to the applications that analyze them, enabling responsible management of the most personal of data.
Recording the current state of a vCon on a SCITT Transparency Service secures the integrity and inclusion of the vCon from tampering or deleting a specific version.

This template provides a standard set of COSE Headers and mapping to vCons, providing integrity and inclusion protection while mitigating potential PII concerns.

The **S**upply **C**hain **I**ntegrity, **T**ransparency and **T**rust (SCITT) initiative is a set of [IETF standards](https://datatracker.ietf.org/group/scitt/documents/) for managing the compliance and auditability of goods and services across end-to-end supply chains.
SCITT supports the ongoing verification of goods and services where the authenticity of entities, evidence, policy, and artifacts can be assured and the actions of entities can be guaranteed to be authorized, non-repudiable, immutable, and auditable.

The following provides a template for securing a vCon with a SCITT Signed Statement.

### vCon Signed Statement Example

The following example highlights a typical SCITT Signed Statement, based on a vCon:

[Events API](../../api-reference/events-api/)

```cddl
Signed_Statement = #6.18(COSE_Sign1)
Receipt = #6.18(COSE_Sign1)

COSE_Sign1 = [
  protected   : bstr .cbor Protected_Header,
  unprotected : bstr .cbor Unprotected_Header,
  payload     : bstr / nil,
  signature   : bstr
]

Protected_Header = {
  &(CWT_Claims: 15) => CWT_Claims
  ? &(alg: 1) => int
  ? &(payload_hash_alg: TBD_1) => int
  ? &(payload_preimage_content_type: TBD_2) => tstr / uint
  ? &(payload_location: TBD_3) => tstr
  ? &(kid: 4) => bstr
  ? &(x5t: 34) => COSE_CertHash
  ? &(x5chain: 33) => COSE_X509
  ? &(meta-map: TBD_4) => meta-map
  * int => any
}

CWT_Claims = {
  &(iss: 1) => tstr
  &(sub: 2) => tstr
  * int => any
}

meta-map = {
    * tstr=> tstr
}

Unprotected_Header = {
  ? &(receipts: 394)  => [+ Receipt]
  * int => any
}
```

### metamap key/value pairs

The following values are added to the Protected Header meta-map, providing enough information to validate the inclusion and integrity protection of a vCon, providing audit and debugging insight, without risk of any PII information being maintained.

```json
{
  "conserver_link": "scitt",
  "conserver_link_name":  "scitt_created",
  "conserver_link_version": "0.2.0",
  "timestamp_declared": "2024-05-07T16:33:29.004994",
  "vcon_operation": "vcon_create",
  "vcon_draft_version": "00"
}
```

### conserver_link (OPTIONAL)

The link `type` as named under the conserver links folder.

While optional, this value is useful for tracing and debugging, knowing the source of the statement, long after troubleshooting or auditing may be needed.

For the [SCITT Conserver Link](https://github.com/vcon-dev/vcon-server/tree/main/server/links/scitt), this value would be `scitt`

### conserver_link_name (OPTIONAL)

vCons are processed by workflow pipelines that run multiple steps.
In the [conserver model](https://www.conserver.io/), these are called chains which run one or more links.
The `conserver_link_name` is the link as instanced and executed, different from the `conserver_link` which is the type name, that may be instanced 1 or more times.

Based on the conserver link implementation, this value is likely sourced from a [conserver configuration](https://github.com/vcon-dev/vcon-server/tree/main/server/links/scitt#configuration):
For debugging purposes, the vCon pipeline may wish to store the name of the pipeline.
This property may prove to be redundant to the [vcon_operation](#vcon_operation), however it's proven helpful for tracing and debugging as the `vcon_operation` will likely turn into a standard set of lifetime values, while configuration will be unique to each instance.

```yaml
links:
  scitt-created:
    module: links.scitt
    options:
      api_url: "https://app.datatrails.ai/archivist/v2"
      vcon_operation: "vcon_created"
      auth:
        type: "OIDC-client-credentials"
        token_endpoint: "https://app.datatrails.ai/archivist/iam/v1/appidp/token"
        client_id: "<your_client_id>"
        client_secret: "<your_client_secret>"
  scitt_consent_revoked:
    module: links.scitt
    options:
      api_url: "https://app.datatrails.ai/archivist/v2"
      vcon_operation: "vcon_consent_revoked"
      auth:
        type: "OIDC-client-credentials"
        token_endpoint: "https://app.datatrails.ai/archivist/iam/v1/appidp/token"
        client_id: "<your_client_id>"
        client_secret: "<your_client_secret>"

chains:
  create_chain:
    links:
      - scitt_created
    ingress_lists:
      - create_ingress
    egress_lists:
      - default_egress
    enabled: 1
  consent_revoked_chain:
    links:
      - scitt_consent_revoked
    ingress_lists:
      - consent_ingress
    egress_lists:
      - default_egress
    enabled: 1
```

In the above configuration, depending on whether the `create_chain` or the `consent_revoked_chain` chain was instanced, `conserver_link_name` would equal: `scitt_created` or `scitt_consent_revoked`.
In both instances, the `conserver_link` would be `scitt`.

### conserver_link_version (OPTIONAL)

The version of the `conserver_link`.
This template applies to version `0.2.0`

### payload (REQUIRED)

The hash of the vCon as it's recorded on the SCITT Transparency Service.
Setting the `payload_hash_alg` indicates the payload is a hash of content in `payload_preimage_content_type` format, using the `payload_hash_alg` algorithm.

`payload`, `payload_hash_alg` and `payload_preimage_content_type` originate from the IETF Draft: [COSE Hash Envelope](https://datatracker.ietf.org/doc/draft-ietf-cose-hash-envelope/).

### payload_hash_alg (REQUIRED)

The hash algorithm used to hash the vCon.
Currently, this is `SHA-256`, but should be sourced by the vCon object to support agility.

### payload_preimage_content_type (REQUIRED)

The property name comes from [draft-ietf-cose-hash-envelope](https://datatracker.ietf.org/doc/draft-steele-cose-hash-envelope/), representing the `content-type` of the vCon, prior to hashing.

[Section 5.3.1 of vCon 00](https://www.ietf.org/archive/id/draft-vcon-vcon-container-00.html#section-5.3.1) specifies `application/vcon`.
There is [vcon issue](https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-container/issues/7), and discussion for using `application/vcon+json`

### subject (REQUIRED)

The [vCon unique identifier](https://www.ietf.org/archive/id/draft-ietf-vcon-vcon-container-00.html#name-uuid).
Subject is used to align with the [SCITT Protected Header](https://www.ietf.org/archive/id/draft-ietf-scitt-architecture-08.html#:~:text=Subject:)

### timestamp_declared (REQUIRED)

Set to [vCon updated_at](https://www.ietf.org/archive/id/draft-ietf-vcon-vcon-container-00.html#name-updated_at), capturing the datetime the vCon was updated.
As vCon processing may take time, and the processing of various steps (Conserver links & chains), may create out of order entries to the ledger, capturing the updated time creates consistency across a set of independent operations.
All entries related to the same vCon version (`updated_at` | `hash`), should likely be considered equal in timing.

### vcon_operation (REQUIRED)

A SCITT Signed Statement should be created for each completed vCon operation.
For every creation and update to a vCon, a SCITT Statement would seal the vCon, recording it on the ledger for inclusion and verification.
The defined lifecycle events of a vCon will likely evolve with the standard.
For now, the `vcon_operation` (`string`) is the placeholder.

## Verifying vCons

DataTrails provides several APIs for verifying the integrity and inclusion of changes to a vCons history.
These changes are being proposed to the SCITT Reference API (SCRAPI).

We'll also explore specific vCon scenarios, such as consent and revocation validation.

### Retrieving All vCon Events

For each important operation performed on a vCon, a SCITT Signed Statement should be recorded.

To align with SCITT semantics, the vcon_uuid is set to the DataTrails `subject` event attribute. (`event_attributes.subject`)

To query the history of SCITT Signed Statements for a given vCon, use the following:

- For bash/curl commands, configure the `.datatrails/bearer-token.txt` using the DataTrails [Creating Access Tokens](https://docs.datatrails.ai/developers/developer-patterns/getting-access-tokens-using-app-registrations/) developer docs.
- Query the collection of SCITT Signed Statements, using the `subject` attribute.
  Set the `VCON` env variable to the `vcon_uuid`

   ```bash
   DATATRAILS_EVENTS_URL="https://app.datatrails.ai/archivist/v2/assets/-/events"
   VCON="bbba043b-d1aa-4691-8739-ac3ddd0303af"
   curl -g -X GET -H "@$HOME/.datatrails/bearer-token.txt" \
     "$DATATRAILS_EVENTS_URL?event_attributes.subject=vcon://$VCON" \
     | jq
   ```

- Verify Inclusions of a Specific vCon Hash

   ```bash
   DATATRAILS_EVENTS_URL="https://app.datatrails.ai/archivist/v2/assets/-/events"
   VCON="bbba043b-d1aa-4691-8739-ac3ddd0303af"
   VCON_HASH="eae12ce2ae12c7b1280921236857d2dc1332babd311ae0fbcab620bdb148fd0d"
  curl -g -X GET -H "@$HOME/.datatrails/bearer-token.txt" \
     "$DATATRAILS_EVENTS_URL?event_attributes.subject=vcon://$VCON&event_attributes.payload_hash_alg=SHA-256&event_attributes.payload_hash_value=$VCON_HASH" \
     | jq
   ```

- Query Events for a Specific vCon for a Specific Operation

   ```bash
   DATATRAILS_EVENTS_URL="https://app.datatrails.ai/archivist/v2/assets/-/events"
   VCON="bbba043b-d1aa-4691-8739-ac3ddd0303af"
   VCON_OPERATION="vcon_created"
   curl -g -X GET -H "@$HOME/.datatrails/bearer-token.txt" \
     "$DATATRAILS_EVENTS_URL?event_attributes.subject=vcon://$VCON&event_attributes.vcon_operation=$VCON_OPERATION" \
     | jq
   ```

- Query All Events for a Specific Operations

   ```bash
   DATATRAILS_EVENTS_URL="https://app.datatrails.ai/archivist/v2/assets/-/events"
   VCON_OPERATION="vcon_created"
   curl -g -X GET -H "@$HOME/.datatrails/bearer-token.txt" \
     "$DATATRAILS_EVENTS_URL?event_attributes.vcon_operation=$VCON_OPERATION" \
     | jq
   ```

- Limit Events Created by a Specific DataTrails Identity

   ```bash
   DATATRAILS_EVENTS_URL="https://app.datatrails.ai/archivist/v2/assets/-/events"
   VCON="bbba043b-d1aa-4691-8739-ac3ddd0303af"
   PRINCIPAL="b5cfacfd-b918-4338-ad61-f4947477f874"
   curl -g -X GET -H "@$HOME/.datatrails/bearer-token.txt" \
     "$DATATRAILS_EVENTS_URL?event_attributes.subject=vcon://$VCON&principal_declared.issuer=https://app.datatrails.ai/appidpv1&principal_declared.subject=$PRINCIPAL" \
     | jq
   ```

### More Info:

- [DataTrails Quickstart: SCITT Statements (Preview)](../../developer-patterns/scitt-api/)
- [SCITT.io](https://scitt.io)
- [vCons and Conserver.io](https://www.conserver.io/)
