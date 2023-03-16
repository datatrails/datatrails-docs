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
| document_document      | attachment that points to the most recent version of the document being traced                 | Optional, can use hash only |
| document_hash_value    | hash of the most recent version of the document                                                | Required                    |
| document_hash_alg      | algorithm used for hashing                                                                     | Required                            |
| document_version       | specific version string for the most recent version of the document                            | Optional                    |
| document_publish_date  | timestamp of the appearance of the most recent document version in RKVST                       | Required, must be current time and date                            |
| document_status        | label for filtering and accommodating critical document lifecycle events                       | Optional, but encouraged    |
| document_portable_name | formal name or identifier for document that persists across boundaries and throughout versions | Optional                    |

### Publish Event

Publish an update to the document.

| Event Attributes                | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | tells RKVST how to interpret Event                    | Required, must be set to `publish`        |
| document_version_authors | list of authors on this version of the document | Optional, if present must be list of maps |

| Asset Attributes      | Meaning                                                                        | Requirement                                     |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------|
| document_document     | attachment that points to the most recent version of the document being traced | Optional, can use hash only                     |
| document_hash_value   | hash of the most recent version of the document                                | Required                                        |
| document_hash_alg     | algorithm used for hashing                                                     | Required                                        |
| document_version      | specific version string for the most recent version of the document            | Optional                                        |
| document_publish_date | timestamp of the appearance of the most recent document version in RKVST       | Required, must be current time and date         |
| document_status       | label for filtering and accommodating critical document lifecycle events       | Optional, should be one of `Draft` or `Published` |

### Recorded Read Event

Make a declaration in the document history that it was accessed.

| Event Attributes            | Meaning                                                                        | Requirement                                      |
|----------------------|--------------------------------------------------------------------------------|--------------------------------------------------|
| arc_display_type     | tells RKVST how to interpret Event                                             | Required, must be set to `recorded read`         |
| document_read_type   | designates if the latest version of the document has been read, or its history | Required, must be one of `document` or `history` |
| document_read_filter | any filter on the Events list to be fetched                                    | Optional, encouraged if `document_read_type` is `history`                                         |

### Withdraw Event

Withdraw an entire document (mark that it is no longer available).

| Event Attributes                | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | tells RKVST how to interpret Event                    | Required, must be set to `withdraw`        |
| document_withdraw_reason | reason why document has been withdrawn | Optional, should be one of `Retired` or `Published In Error` |

| Asset Attributes             | Meaning                                                                        | Requirement                                                        |
|------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------|
| document_document            | attachment that points to the most recent version of the document being traced | Optional, can use hash only                                        |
| document_hash_value          | hash of the most recent version of the document                                | Optional, must be present if `document_latest_document` is present |
| document_hash_alg            | algorithm used for hashing                                                     | Required if `document_hash_value` is present                       |
| document_version             | specific version string for the most recent version of the document            | Optional                                                           |
| document_latest_publish_date | timestamp of the appearance of the most recent document version in RKVST       | Optional, must be present if `document_latest_document` is present |
| document_status              | label for filtering and accommodating critical document lifecycle events       | Required, must be `withdrawn`                                      |

### Revoke Version Event

Mark a particular version of a document from its history as no longer reliable.

| Event Attributes                | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | tells RKVST how to interpret Event                    | Required, must be set to `withdraw version`        |
| document_withdraw_version | version of document you wish to mark as no longer valid | Required, should be version string from a previous Publish Event |
| document_withdraw_reason | reason why document has been withdrawn | Optional, should be one of `Retired` or `Published In Error` |

| Asset Attributes                | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| document_status         | updates status of document                    | Optional, must be set to `withdrawn` if present        |