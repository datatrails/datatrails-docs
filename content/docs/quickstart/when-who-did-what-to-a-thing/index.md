---
title: "When Who Did What to a Thing?"
description: "Understanding the Core Principles of RKVST"
lead: "Understanding the Core Principles of RKVST"
date: 2020-11-12T13:26:54+01:00
lastmod: 2020-11-12T13:26:54+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 1
toc: true
---


Enterprise developers are challenged to build apps that track usage and build trust in multi-party data while meeting assurance, governance, and compliance needs of the business. 

The Jitsuin RKVST is a Data Assurance Hub which stores shared asset evidence that proves when who did what to reduce risk, authenticates provenance in data for confident decisions, while governing complex data sharing controls. 

Unlike forming your own blockchain consortium, committing to expensive integrations or managing spreadsheets, RKVST brings the right level of trust to data with a single line of code integration at a fraction of cost and time to value.

This guide will get you started quickly with the RKVST UI and provide an understanding of core RKVST concepts.  

Before you begin with RKVST there's one key model to use when mapping to business process:

***When who did what to a thing.***

{{< img src="WhenWhoDidWhattoAThing.png" alt="Rectangle" caption="<em>When who did what to a thing</em>" class="border-0" >}}

What is a Thing?
----------------

A Thing can be anything; a weather station sensor, an invoice, or even a shipping container. Whatever the Thing is, RKVST considers it an ***Asset***.

An Asset is an object, physical or otherwise, that has an Identity, a Description, and a set of Attributes. 

In most cases, Attributes are Key-Value pairs; However, RKVST can also store more detailed information including associated binaries, PDFs or Pictures.

Take the following example:


{{< img src="AssetExample.png" alt="Rectangle" caption="<em>Example Asset</em>" class="border-0" >}}

Here our Asset represents a specific shipping crate, it has basic Attributes that describe its capacity, more specific Attributes such as internal tracking IDs and even a picture to show us its last recorded physical state.

Here is an example of another Asset:

{{< img src="SecondAssetExample.png" alt="Rectangle" caption="<em>Example Asset 2</em>" class="border-0" >}}

In this example, our Asset describes a smart-lock on a building. This Asset has Attributes that describe on which building it is installed, its firmware version, and which key last opened it.

In both cases, it may be necessary to track more detailed information specific to the class of Asset. 

RKVST allows you to create as many custom Attributes as you need to describe an Asset, allowing you the freedom to record your needs with ease and accessibility.

[For more detailed information on Assets and how to implement them please click here]()

What happens to an Asset?
-----------------------------

Many things may happen to an Asset over its entire lifecycle, either directly affecting its state or decisions about what should happen to it. If an Asset Attribute is changed or if there is a noteworthy decision made about it, RKVST considers this an ***Event***.

Similar to an Asset, Events also have Identities, Descriptions and their own set of Attributes. Importantly, a key attribute of Events is tracking ***when*** an action happens, ***what*** that action is and ***who*** acted upon it.

For example:

{{< img src="EventExample.png" alt="Rectangle" caption="<em>Example Event</em>" class="border-0" >}}

Here we see a single Event recorded on our Shipping Crate Asset. After a physical inspection, the Container has an Event that shows it was unsealed at a factory; this Event was automatically reported by a connected crate sensor on the 12th March 2020.

We can also see the Event belongs to a specific Asset. As more Events happen to an Asset, the richer the information on it becomes. Over time, your Asset record will not just be the attributes by which it is described, but also the shared asset evidence history of its entire lifecycle. 

Events can be highly descriptive and will always belong to a specific Asset. A simple step-by-step guide on how to record an Event will follow but, [for details on how to implement more comprehensive Events please refer to this Section]().

Who can create an Event against an Asset?
-------------------------------------------

Now we understand what an Asset is and what sort of Events can happen to it. It is also important to understand who can perform an Event.

Access to Events, Assets and their Attributes are governed by two different sets of policies:

* ***ABAC*** (Attribute Based Access Control) - controls access for non-root users of your internal organization to Assets and Events based on specific Attributes
* ***OBAC*** (Organization Based Access Control) - controls access for external organizations to specific Assets and Events based on specific Attributes 

Specifically, in the case of OBAC you must share access to root users of the external organization, then those root users of the organization must apply ABAC to govern sharing of Assets and Events for their own users.

To understand more about Root Users and non-Root users, [please refer to the section on Tenancies.]()

Both ABAC and OBAC use the same format for controlling access; they provide filters and restrictions to what a specific subject or Actor can read and write following the same generic pattern:

* Subject
* Attribute Read
* Attribute Write
* Event Read
* Event Write

You can also mix and match ABAC and OBAC into the same policy, for example:

{{< img src="IAMPolicyExample.png" alt="Rectangle" caption="<em>Example IAM Policy</em>" class="border-0" >}}

Here we can see an access policy that allows specific members of the Internal Organization, and an External Organisation to read all Event attributes including the Height, Width, and Length of Assets. The Users can also create "Dispose" Events but they cannot change Attributes of an Asset.

We can also define filters for the Asset types that users are allowed to see, which will be [covered in more detail in the IAM Policies Section.]()

The Golden Thread
-----------------

Now we understand "Who did What to a Thing" we can bring it all together, creating a stream of irrefutable, assured Events on Assets which form a complete traceable historical record to build trust in key information needed by data consumers. 

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}

We can ensure the recorded data is only accessible by the people and organizations who need to see it. Those users who need to know see the same data as other authorized users.

This provides a strong and compelling Data Assurance Hub for multi-party trust.

To see how you can apply the RKVST please check the process modelling section.

To continue with the Quickstart guide and create your first Asset, [please click here.]()

