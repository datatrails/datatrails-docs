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
{{< /caution >}}

The following provides a template for how to secure a vCon on DataTrails.

TODO: convert the table to bullets, with descriptions

| Event Attribute                 | SCITT                                 | Source             |
| -                               | -                                     | -                  |
| `arc_display_type`              | `metamap.vcon_operation`              | code               |
| `payload_hash_alg`              | `payload_hash_alg`                    | code               |
| `payload_preimage_content_type` | `payload_preimage_content_type`       | `application/json` |
| `payload_hash_value`            | `protected-header.payload_hash_value` | vcon.hash          |
| `vcon_operation`                | `metamap.vcon_operation`              | code               |
| `vcon_pipeline`                 | `metamap.vcon_pipeline`               | code               |
| `vcon_pipeline_version`         | `metamap.vcon_pipeline_version`       | code               |
| `vcon_updated_at`               | `metamap.vcon_updated_at`             | `vcon.updated_at or `<br>`vcon.created_at` |
| `subject`                       | `protected-header.cwt-claims.subject` |`vcon_uuid` |

## User Agent Headers

TODO: Format these better

- `DataTrails-User-Agent`: `headers["DataTrails-User-Agent"]` diagnostics for the source of the request
- `partner_id`: `headers["DataTrails-Partner-ID"]` used for tracing source requests 
