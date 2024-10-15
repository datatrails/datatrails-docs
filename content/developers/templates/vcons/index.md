---
title: "vCon Template"
description: "Creating DataTrails Events for vCons"
lead: "Securing vCons with DataTrails Events"
date: 2021-06-09T13:49:35+01:00
lastmod: 2021-06-09T13:49:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "templates"
weight: 20
toc: true
aliases:
---
vCons safely and securely carry conversations from the network elements that create them to the applications that analyze them, enabling responsible management of the most personal of data.
Recording the current state of a vCon on DataTrails secures the integrity and inclusion of the vCon from tampering or deleting a specific version.

{{< caution >}}
[IETF SCITT](https://datatracker.ietf.org/wg/scitt/about/) is currently in draft and subject to change.
The following template provides DataTrails Event APIs, enabling production SLA for securing vCons.
{{< /caution >}}
{{< caution >}}
[IETF vCon](https://datatracker.ietf.org/wg/vcon/about/) is currently in draft and subject to change.
The following template references the specific draft version the template applies to.
[vCon Draft 00](https://datatracker.ietf.org/doc/draft-vcon-vcon-container/00/)
{{< /caution >}}

The following provides a template for how to secure a vCon on DataTrails.

### vCon Event Example

The following example highlights a typical DataTrails Event, based on a vCon:

[Events API](../../api-reference/events-api/)

```json
{
  "operation": "Record",
  "behaviour": "RecordEvidence",
  "event_attributes": {
    "arc_display_type": "vcon_create",
    "payload_hash_alg": "SHA-256",
    "payload_preimage_content_type": "application/json",
    "payload_hash_value": "e5e20exxxxxxxxxx78383479f9de138cf71b98b740fd5d7ee3xxxxxxxxxxde05",
    "vcon_operation": "vcon_create",
    "vcon_pipeline": "create-pipeline",
    "vcon_pipeline_version": "1.0.0",
    "vcon_updated_at": "2024-05-07T16:33:29.004994",
    "subject": "vcon://xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "vcon_draft_version": "00"
  }
}
```

### arc_display_type (REQUIRED)

Default within DataTrails to categorize events.
`arc_display_type` is also the default means to [configure permissions](https://docs.datatrails.ai/platform/administration/sharing-access-inside-your-tenant/) for which type of events a client my view/edit.

For simplicity in configuring permissions, this property is a duplicate of the [vcon_operation](#vcon_operation) but could vary in advanced scenarios.

### vcon_operation (REQUIRED)

A DataTrails Event should be created for each completed vCon operation.
For every creation and update to a vCon, a SCITT Statement would seal the vCon, recording it on the ledger for inclusion and verification.
The defined lifecycle events of a vCon will likely evolve with the standard.
For now, the `vcon_operation` (`string`) is the placeholder.

### payload_hash_alg (REQUIRED)

The hash algorithm used to has the vCon.
Currently, this is `SHA-256`, but should be sourced by the vCon object to support agility.

### payload_preimage_content_type (REQUIRED)

The property name comes from [draft-ietf-cose-hash-envelope](https://datatracker.ietf.org/doc/draft-steele-cose-hash-envelope/), representing the `content-type` of the vCon, prior to hashing.

[Section 5.3.1 of vCon 00](https://www.ietf.org/archive/id/draft-vcon-vcon-container-00.html#section-5.3.1) specifies `application/vcon`.
There is [vcon issue](https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-container/issues/7), and discussion for using `application/vcon+json`

### payload_hash_value (REQUIRED)

The hash of the vCon as its recorded on DataTrails.

### vcon_pipeline (OPTIONAL)

vCons are processed by workflow pipelines that run multiple steps.
In the [conserver model](https://www.conserver.io/), these are called chains which run one ore more links.
For each chain, a vCon is complete and written to the SCITT Ledger to protect its integrity and inclusion.
For debugging purposes, the vCon pipeline may wish to store the name of the pipeline.
This property may prove to be redundant to the [vcon_operation](#vcon_operation).

### vcon_pipeline_version (OPTIONAL)

The version of the [vcon_pipeline](#vcon_pipeline).

### vcon_updated_at (REQUIRED)

See [vCon updated_at](https://www.ietf.org/archive/id/draft-ietf-vcon-vcon-container-00.html#name-updated_at)

### subject (REQUIRED)

The [vCon unique identifier](https://www.ietf.org/archive/id/draft-ietf-vcon-vcon-container-00.html#name-uuid).
Subject is used to align with the [SCITT Protected Header](https://www.ietf.org/archive/id/draft-ietf-scitt-architecture-08.html#:~:text=Subject:)

## User Agent Headers

When submitting requests to DataTrails, the following header parameters are required for tracking, independent of authorization.

### DataTrails-User-Agent (REQUIRED)

Diagnostics and tracking for the source of the request.
Typically set to the code or service.
For example: (`DataTrails-User-Agent:oss/conserverlink/0.1.0`)

### Partner_ID (REQUIRED)

Diagnostics and tracking of the Partner making requests.
This header is independent of the [DataTrails-User-Agent](#datatrails-user-agent), as multiple services may be running the same codebase, such as the [vCon Conserver](https://github.com/vcon-dev/vcon-server/)

For example: (`DataTrails-Partner-ID:synsation.io"`
