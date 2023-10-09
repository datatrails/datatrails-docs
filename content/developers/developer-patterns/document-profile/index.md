---
title: "Document Profile"
description: "Tracing the Lifecycle of a Document with RKVST"
lead: "Tracing the Lifecycle of a Document with RKVST"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 35
toc: true
---

The RKVST document profile is a set of suggested Asset and Event attributes that allow you to trace the lifecycle of a document.

{{< note >}}

##### Profile Attribute Namespace

The `document_` prefix is used to designate attributes that are part of the profile. Some of these are interpreted by RKVST and others are guidelines.
{{< /note >}}

### Document Profile Asset Attributes

| Asset Attributes              | Meaning                                                                                        | Requirement                 |
|------------------------|------------------------------------------------------------------------------------------------|-----------------------------|
| arc_profile            | Designates that the Asset follows the document profile                                         | Required, set as `Document` |
| document_hash_value    | Hash of the most recently published version of the document                                    | Required                    |
| document_hash_alg      | Algorithm used to compute document_hash_value (currently, only SHA-256 is supported)           | Required                            |
| document_document      | Attachment containing the most recently uploaded version of the document being traced.         | Optional |
| document_version       | Specific version string for the most recent version of the document                            | Optional, but encouraged    |
| document_status        | Label for filtering and accommodating critical document lifecycle events (Published, Withdrawn)| Optional, enforced when using lifecycle events    |
| document_portable_name | Formal name or identifier for document that persists across boundaries and throughout versions | Optional, not interpreted by RKVST |

{{< note >}}

##### Uploading Documents as Attachments

For more detailed information on Attachments and how to implement them, please refer to [the Blobs API Reference](../../api-reference/blobs-api/) and [the Attachments section of the Events API](../../api-reference/events-api/#adding-attachments)
{{< /note >}}

### Publish Event

Publish a new version of the document using special attributes interpreted by RKVST for this event type.

| Event Attributes         | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | Tells RKVST how to interpret Event              | Required, must be set to `Publish`        |
| document_version_authors | List of authors on this version of the document | Optional, see format below |

{{< note >}}

##### Document Version Authors

You must express `document_version_authors` as a list of objects that have `display_name` as a property.

```json
[
  {
    "display_name": "Alice", 
    "email": "", 
    ...
  }
]
```

{{< /note >}}

| Asset Attributes      | Meaning                                                                        | Requirement                                     |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------|
| document_hash_value   | Hash of this version of the document                                           | Required                                        |
| document_hash_alg     | Algorithm used for hashing. We only officially support SHA-256.                | Required
| document_status       | Label for filtering and accommodating critical document lifecycle events       | Required, must be `Published` |
| document_document     | Attachment containing this version of the document                             | Optional
| document_version      | Version string for the this version of the document                            | Optional                                        |

### Withdraw Event

Withdraw an entire document (mark that it is no longer considered current.)

| Event Attributes                | Meaning                                         | Requirement                               |
|---------------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type                | Tells RKVST how to interpret Event              | Required, must be set to `Withdraw`        |
| document_withdrawal_reason      | Reason why document has been withdrawn          | Optional, but encouraged |

| Asset Attributes             | Meaning                                                                        | Requirement                                                        |
|------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------|
| document_status              | Label for filtering and accommodating critical document lifecycle events       | Required, must be `Withdrawn`                                      |
