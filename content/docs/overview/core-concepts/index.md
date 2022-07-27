---
title: "Core Concepts"
description: "RKVST Core Concepts"
lead: "RKVST Core Concepts"
date: 2021-06-14T10:57:58+01:00
lastmod: 2021-06-14T10:57:58+01:00
draft: false
images: []
menu: 
  docs:
    parent: "overview"
weight: 3
toc: true
---

## Tenancies
To get started with RKVST, you will need to configure your Tenancy. Each Tenancy has Root users and Non-Root users. A Root user will have read and write access to everything in the RKVST tenancy. Non-root users can be given specific, attribute-based permissions which are granted via an ABAC Access Policy, created by a Root user.

You may add users to your tenancy using an invite. To do so, go to: Manage RKVST > Users > Invite New User or use the [Invites API](https://docs.rkvst.com/docs/api-reference/invites-api/). This will send an email to the person you'd like to add as part of your tenancy. As long as they sign up for their RKVST account with the same email address as the invite, they will automatically be added to your tenancy so you may begin collaborating and sharing information. 

## Assets

Assets are central to RKVST. Each one represents something that requires shared accountability and trustworthy sharing. This could be a physical object, a smart device, or even a business process. Each Asset is a 'Golden Thread' of immutable evidence that can be shared in real-time with all stakeholders. An RKVST Asset is a collection of attributes that describe the Asset, expressed in JSON format. RKVST Asset content is flexible; anything deemed important can be tracked. Each Asset will have a fixed identity across all stakeholders, ensuring that all relevant parties are collaborating on the same object and can see the full history of the Asset at any given time.

## Events 

Events are performed against a particular Asset. Each Event contributes to the 'Golden Thread' by enriching the Asset's history. Events can be used to add or update Asset information, but they can never be deleted or modified. Events provide details on Asset attributes, such as updating the weight of a shipment, and/or details about the event itself, such as a recording a shipment inspection.

## Access Policies 

Sharing the right amount of information with your value chain partners is critical to creating a trustworthy shared history for Assets. It is important that every participant be able to see and contribute to the management of Assets without compromising security and private information. To ensure stakeholders can view and contribute only to the Assets and attributes relevant to them, transactions are private by default. A Root user may share as much or as little access to Assets as the needs of the value chain partners dictate through Access Policies. 

An Attribute-Based Access Control (ABAC) policy is used to share with Non-Root users within one's tenancy. An Organization-Based Access Control (OBAC) policy is used to share with the Root users of another tenancy. The Root user of the external tenancy may then use an ABAC policy to grant permissions to the relevant Non-Root users of their tenancy. In both cases, attribute-specific read and write access can be granted using fine-grained controls. 

## The Golden Thread

A stream of untamperable, assured, and trusted Events against an Asset to track and follow key information, shared securely with relevant stakeholders.

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}