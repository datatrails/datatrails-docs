---
title: "Authenticity of Media and Files"
description: "Assurance with DataTrails"
lead: "Assurance with DataTrails"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  usecases:
    parent: "usecases"
weight: 31
toc: true
aliases:
  - /docs/user-patterns/authenticity-and-attestation/
  - /usecases/authenticity-and-attestation/
---

A very simple yet powerful pattern for using DataTrails is the *Authenticity* pattern. This is a good choice when dealing with data or documents where trust, integrity and authenticity are more important than secrecy. This could be data that is shared between business partners or more simply the relationship between creators and consumers of digital media. 

The DataTrails platform separates data from its provenance metadata. By recording the metadata in the DataTrails platform it becomes an irrefutable record of the origin, provenance, integrity and authenticity of the media asset. When the data is updated a corresponding Event updates the metadata in DataTrails to build an immutable audit trail of the history of that data.

Together with fine-grained attribute based access controls the platform provides a trust and visibility layer to support trusted data sharing and provides evidence to resolve contested scenarios. 

Both private and public stakeholders can verify that what they see on their screen is authentic and and has not been tampered with.

## Example 1: Digital Media

The obvious example of a piece of digital media is a photographic image but it equally applies to graphical images and also sound and video recordings. 

A provenance history helps to establish the authenticity and integrity of digital media content. It allows users to verify that the content that they are consuming or sharing is genuine and has not been tampered with or manipulated. In an era of declining trust in digital media caused by an increased awareness of misinformation, AI, and deepfakes, understanding the provenance of digital media is crucial for restoring trust and credibility.

Digital media provenance ensures transparency, trustworthiness, and accountability benefiting both content creators and consumers.

### Considerations

**Media Origin:**
The provenance record helps with attributing credit to the original creators of digital media. It enables content creators to protect their intellectual property rights and ensures they receive appropriate recognition for their work.

Consumers of the media can check the origin and history of the media to give confidence that the media is authentic and if it has been processed.

**Versions:**
Changes are recorded as Events. The immutable audit trail provided by DataTrails records the history of the media allowing users to verify that it contains no unofficial changes. 

## Example 2: Evidential Documents

There are a great many documents that serve as evidence in formal discussions: shipping manifests; pictures of a traffic accident; statements of account; education diplomas; contracts. DataTrails adds strong integrity to any document to allow easy verification.

It is rare for a document to remain unchanged during it’s lifetime. Some documents are expected to go though many versions while others change much less frequently.

The [Document Profile](/developers/developer-patterns/document-profile/) pattern is a suggested set of attributes for Assets and Events for recording the life cycle of a document.

### Considerations

**Track Documents:** Create a very simple Asset structure with minimal attributes to identify the document and additional attributes to store the key metadata, such as a hash of the document.

**Collections:** If the document is strongly related to another one, consider adding and tracking them all as Events against a single Asset record.

**Versions:** If the document is a new version of something already stored in DataTrails, then use Events to replace the document's metadata with the updated version. Any authorized stakeholder fetching the Asset record will automatically get the most up-to-date version, and prior versions can be retrieved if necessary from the Event history.

**Access:** For each asset record, it is possible to choose if you want to share that publicly by creating a Public Asset, or with a select group of "friendly" associates by creating a Private asset that is protected by an Access Policy. By sharing publicly, your trail will be verifiable on our Instaproof service by anyone without the need for a DataTrails account.
