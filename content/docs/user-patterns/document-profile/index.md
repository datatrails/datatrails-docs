---
title: "Document Profile"
description: "Tracing the Lifecycle of a Document with RKVST"
lead: "Tracing the Lifecycle of a Document with RKVST"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "user-patterns"
weight: 34
toc: true
---

The RKVST document profile is a set of suggested Asset and Event attributes that allow you to trace the lifecycle of a document.

{{< note >}}
The `document_` prefix is used to designate attributes that are part of the profile.
{{< /note >}}

### Document Profile Asset Attributes 

| Asset Attributes              | Meaning                                                                                        | Requirement                 |
|------------------------|------------------------------------------------------------------------------------------------|-----------------------------|
| arc_profile            | designates that the Asset follows the document profile                                         | Required, set as `document` |
| document_document      | attachment containing the most recently uploaded version of the document being traced      | Optional, can use hash only |
| document_hash_value    | hash of the most recent version of the document                                                | Required                    |
| document_hash_alg      | algorithm used to compute document_hash_value (currently, only SHA-256 is supported)           | Required                            |
| document_version       | specific version string for the most recent version of the document                            | Optional                    |
| document_status        | label for filtering and accommodating critical document lifecycle events (Published, Withdrawn)| Optional, but encouraged    |
| document_portable_name | formal name or identifier for document that persists across boundaries and throughout versions | Optional, not interpreted by RKVST |

### Publish Event

Publish a new version of the document using special attributes interpreted by RKVST for this event type.

| Event Attributes         | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | tells RKVST how to interpret Event              | Required, must be set to `Publish`        |
| document_version_authors | list of authors on this version of the document | Optional, if present must be list of maps |

| Asset Attributes      | Meaning                                                                        | Requirement                                     |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------|
| document_document     | attachment containing this version of the document | Optional, can use hash only                     |
| document_hash_value   | hash of the most this version of the document                                | Required                                        |
| document_hash_alg     | algorithm used for hashing. We only officially support SHA-256.                | Required
| document_version      | specific version string for the most recent version of the document            | Optional                                        |
| document_status       | label for filtering and accommodating critical document lifecycle events       | Required, must be `Published` |

### Withdraw Event

Withdraw an entire document (mark that it is no longer considered current).

| Event Attributes                | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | tells RKVST how to interpret Event                    | Required, must be set to `Withdraw`        |
| document_withdraw_reason | reason why document has been withdrawn | Optional, should be one of `Retired` or `Published In Error` |

| Asset Attributes             | Meaning                                                                        | Requirement                                                        |
|------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------|
| document_document            | attachment that points to the most recent version of the document being traced | Optional, can use hash only                                        |
| document_hash_value          | hash of the most recent version of the document                                | Optional, must be present if `document_latest_document` is present |
| document_hash_alg            | algorithm used for hashing                                                     | Required if `document_hash_value` is present                       |
| document_version             | specific version string for the most recent version of the document            | Optional                                                           |
| document_status              | label for filtering and accommodating critical document lifecycle events       | Required, must be `withdrawn`                                      |
| document_withdrawal_reason   | reason for withdrawing the document                                            | Optional, but encouraged 
