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
weight: 30
toc: true
aliases:
  - /docs/user-patterns/authenticity-and-attestation/
  - /usecases/authenticity-and-attestation/
---

A very simple yet powerful pattern for using DataTrails is the *Authenticity* pattern. This is a good choice when dealing with data or documents where trust, integrity and authenticity are more important than secrecy. This could be data that is shared between business partners or more simply the relationship between creators and consumers of digital media. 

The DataTrails platform separates data from its provenance metadata. By recording the metadata as a DataTrails ledger it becomes an irrefutable record of the origin, provenance, integrity and authenticity of the media asset. When the data is updated a corresponding Event updates the metadata in DataTrails to build an immutable audit trail of the history of the data.

Together with fine-grained attribute based access controls the platform provides a trust and visibility layer to support trusted data sharing and provides evidence to resolve contested scenarios. 

Both private and public stakeholders can verify that what they see on their screen is authentic and and has not been tampered with.

## Example 1: Digital Media

The obvious example of a piece of digital media is a photographic image but it equally applies to graphical images and also sound and video recordings. 

A provenance history helps to establish the authenticity and integrity of digital media content. It allows users to verify that the content that they are consuming or sharing is genuine and has not been tampered with or manipulated. In an era of fake news, misinformation, AI, and deepfakes, understanding the provenance of digital media is crucial to ensuring trust and credibility.

Digital media provenance ensures transparency, trustworthiness, and accountability benefiting both content creators and consumers.
voice recordings or video audio files

### Considerations

**Media Origin**
The provenance record helps with attributing credit to the original creators of digital media. It enables content creators to protect their intellectual property rights and ensures they receive appropriate recognition for their work.

Consumers of the media can check the origin and history of the media to give confidence that the media is authentic and if it has been processed.

**Versions**
Changes are recorded as Events. The immutable audit trail provided by DataTrails records the history of the media allowing users to verify that it contains no unofficial changes. 

## Example 2: Evidential Documents

There are a great many documents that serve as evidence in formal discussions: shipping manifests; pictures of a traffic accident; statements of account; education diplomas; contracts. DataTrails adds strong integrity to any document to allow easy verification.

It is rare for a document to remain unchanged during it’s lifetime. Some documents are expected to go though many versions while others change much less frequently.

The [Document Profile](/developers/developer-patterns/document-profile/) pattern is a suggested set of attributes for Assets and Events for recording the life cycle of a document.

### Considerations

**Track Documents:** Create a very simple Asset structure with minimal attributes to identify the document and additional attributes to store the key metadata, such as a hash of the document.

**Collections:** If the document is strongly related to another one, consider adding and tracking them all as Events against a single Asset record.

**Versions:** If the document is a new version of something already stored in DataTrails, then use Events to replace the document's metadata with the updated version. Any authorized stakeholder fetching the Asset record will automatically get the most up-to-date version, and prior versions can be retrieved if necessary from the Event history.

**Access** With Publicly Attested documents and Instaproof, anyone can check a document without the need for a DataTrails account. Private documents can be protected by an Access Policy.

