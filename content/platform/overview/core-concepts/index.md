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

A Tenancy is an Organization's private area within DataTrails, containing [Asset](./#assets) and [Event](./#events) data. The user who created the Tenancy is the Administrator and has full administrative control over everything in that Tenancy. An Administrator can also create granular [Access Policies](./#access-policies) which allow data from their Tenancy to be shared to other Tenancies; for example, Organization A would share Asset data from their Tenancy to Organization B's Tenancy.

Administrators may invite other user accounts into their Tenancy. The invited user needs to have signed up for DataTrails with the same email address as the invite, they will then be added to the Tenancy as a Non-Administrator. Non-Administrators start off with no permissions but can be given specific permissions (including being upgraded to an Administrator) by any existing Administrator in that Tenancy.

## Assets

Assets are central to DataTrails. Each Asset Record represents ***a thing***; this could be a physical object, a smart device, or even a business process.

A DataTrails Asset has a collection of attributes that describes its current state and a complete life history of Events that brought it to that state. DataTrails Asset attributes track anything deemed important. For example, a Shipping Container as an Asset might have the attributes of height, width and depth, and have a handling history of movements through ports.

Each Asset has a fixed identity across all stakeholders, ensuring that all relevant parties are collaborating on the same object and see the same history of the Asset at any given time when shared through [Access Policies](./#access-policies).

## Events

Events are things that happen during an Asset's lifecycle. Each Event Record contributes to the ['Golden Thread'](./#the-golden-thread) of supply chain evidence by enriching the Asset's history. Events can be used to add or update Asset information if they change the Asset's state, but they also have their own attributes to add process detail and rich evidence.

Events can never be deleted or modified. Events provide details on Asset attributes, such as updating the weight of a shipment, and/or details about the event itself, such as a recording a shipment inspection.

## Access Policies

Sharing the right amount of information with your value chain partners is critical to creating a trustworthy shared history for any Asset. It is important that every participant be able to see and contribute to the management of those Assets without compromising security and private information. To ensure stakeholders can access only the Assets and attributes relevant to them, transactions are private by default. An Administrator may share as much or as little access to Assets as the needs of the value chain partners dictate through Access Policies.

An Attribute-Based Access Control (ABAC) policy is used to share with Non-Administrators within a Tenancy. An Organization-Based Access Control (OBAC) policy is used to share with the Administrators of another Tenancy. The Administrator of the external Tenancy may then use an ABAC policy to grant permissions to the relevant Non-Administrators of their Tenancy. In both cases, attribute-specific read and write access can be granted using fine-grained controls.

## The Golden Thread

Using the four concepts of Tenancy, Assets, Events and Access Policies it is possible to create a Golden Thread of evidence that underpins supply chain integrity, transparency and trust for all relevant stakeholders.

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}
