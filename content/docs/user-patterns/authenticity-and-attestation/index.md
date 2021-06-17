---
title: "Authenticity and Attestation"
description: "Assurance with RKVST"
lead: "Assurance with RKVST"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "user-patterns"
weight: 30
toc: true
---

A very simple yet powerful pattern for using RKVST is the *Authenticity* pattern. This is a good choice when dealing with data or documents that need to be broadly proven. In a single action files can be uploaded to RKVST and their integrity, origin, and timestamps can be verified forever. Stakeholders relying on these files can verify that what they see on their screen is authentic and untampered.

## Example: Evidential documents and photographs

There are a great many documents that serve as evidence in formal discussions: pictures of a traffic accident; education diplomas; contracts; statements of account. RKVST adds strong integrity to any document to allow easy verification later.

### Considerations

_Use Attachments:_ Create a very simple Asset structure with minimal attributes to identify the document and then store the file itself as an Asset attachment.

_Collections:_ If the document is strongly related to another one then consider adding and tracking them all as individual attachments in a single Asset record.

_Versions:_ If the document is a new version of something already stored in RKVST then use Events to replace the Asset attachment with the updated version. Any authorized stakeholder fetching the Asset record will automatically get the most up-to-date version without confusion, and prior versions can be retrieved if necessary from the Event history.
