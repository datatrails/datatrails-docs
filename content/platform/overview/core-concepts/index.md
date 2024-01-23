---
title: "Core Concepts"
description: "DataTrails Core Concepts"
lead: "DataTrails Core Concepts"
date: 2021-06-14T10:57:58+01:00
lastmod: 2021-06-14T10:57:58+01:00
draft: false
images: []
menu: 
  platform:
    parent: "overview"
weight: 31
toc: true
aliases:
  - ../quickstart/when-who-did-what-to-an-asset
  - /docs/overview/core-concepts/
---

## Tenancies

A Tenancy is an Organization's private area within DataTrails, containing [Asset](./#assets) and [Event](./#events) data that build over time to create an Audit Trail. The user who created the Tenancy is the Administrator and has full administrative control over everything in that Tenancy. An Administrator can also create granular [Access Policies](./#access-policies) which allow data from their Tenancy to be shared to other Tenancies; for example, Organization A would share Asset data from their Tenancy to Organization B's Tenancy.

Administrators may invite other user accounts into their Tenancy. The invited user needs to have signed up for DataTrails with the same email address as the invite, they will then be added to the Tenancy as a Non-Administrator. Non-Administrators start off with no permissions but can be given specific permissions (including being upgraded to an Administrator) by any existing Administrator in that Tenancy.

## Assets

Assets are central to DataTrails. Each Asset Record represents ***a thing***; this could be a file, a physical object, a smart device, or even a business process.

A DataTrails Asset has a collection of attributes that describes its current state and, when combined with a complete life history of Events that brought it to that state, we have an immutable Audit Trail. DataTrails Asset attributes track anything deemed important. For example, a Document will have the attributes of author, title and a content hash and will have a history of different versions and release dates. A Shipping Container as an Asset might have the attributes of height, width and depth, and have a handling history of movements through ports.
These are examples of completely different ***things*** that can have a Data Trails Audit Trail.

Each Asset has a fixed identity across all stakeholders, ensuring that all relevant parties are collaborating on the same object and see the same history of the Asset at any given time when shared through [Access Policies](./#access-policies).

## Events

Events are things that happen during an Asset's lifecycle. Each Event Record contributes to the ['Golden Thread'](./#the-golden-thread) of the audit trail by enriching the Asset's history. Events can be used to add or update Asset information if they change the Asset's state, but they also have their own attributes to add process detail and rich evidence.

Events can never be deleted or modified. Events provide details on Asset attributes, such as updating the weight of a shipment, and/or details about the event itself, such as a recording a new document version.

## Access Policies

Sharing the right amount of information with the consumers of your data is critical to creating a trustworthy shared history for any Asset. It is important that every participant be able to see and contribute to the management of those Assets without compromising security and private information. To ensure stakeholders can access only the Assets and attributes relevant to them, transactions are private by default, unless the Asset was created as a [Public Asset](./#the-public-view). An Administrator defines how many of the Asset's attributes the Access Policy permits a user to see so that they only see what they need to complete a task.

An Attribute-Based Access Control (ABAC) policy is used to share with Non-Administrators within a Tenancy. An Organization-Based Access Control (OBAC) policy is used to share with the Administrators of another Tenancy. The Administrator of the external Tenancy may then use an ABAC policy to grant permissions to the relevant Non-Administrators of their Tenancy. In both cases, attribute-specific read and write access can be granted using fine-grained controls.

## The Public View

Every Asset has a private view which is only visible to Tenancy Administrators and those who are given access through an Access Policy. Other Assets, such as those that meet the requirements of the [Document Profile](/developers/developer-patterns/document-profile/), have a [Public View](/platform/overview/public-attestation/) which is visible to everyone.
The purpose of this view is to allow anyone to verify that the document that they are using is genuine and has not been altered. When the document Audit Trail is combined with [Instaproof](/platform/overview/instaproof/) a user of your data can easily find out which version of a document they have and confirm that it is genuine.

## The Golden Thread

Using the four concepts of Tenancy, Assets, Events and Access Policies it is possible to create a Golden Thread of evidence makes up the Data Trails Audit Trail.
This has many use cases relating to content authenticity but can also be applied to supply chain integrity and standards compliance, or fact anything where stakeholders need transparency and trust.

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}
