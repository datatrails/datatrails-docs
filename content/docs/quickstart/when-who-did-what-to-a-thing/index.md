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


RKVST offers a simple platform of trust-based, multi-party evidence sharing that can augment and boost existing decision making processes, whether your system or supply chain has already been digitized or still needs paper to be processed.

RKVST provides a golden thread of traceable, unshreddable evidence and make it available to the right people at the right time; trusted by everyone.

This guide will get you started quickly with the Archivist UI and provide an understanding of core RKVST concepts.  

Before we begin with RKVST we need to understand one key piece of information: 

***When who did what to a thing.***

{{< img src="WhenWhoDidWhattoAThing.png" alt="Rectangle" caption="<em>When who did what to a thing</em>" class="border-0" >}}

What is a Thing?
----------------

A thing can be anything; a weather station sensor, an invoice or even a shipping container. Whatever this thing may be, in RKVST it would be considered ***An Asset***.

At its core an Asset is an object, physical or otherwise, that has an identity, a description and a set of attributes. 

In most cases attributes are fairly simple Key-Value pairs, however RKVST can also store more detailed information including associated binaries such as PDFs or Pictures.

Take the following example:


{{< img src="AssetExample.png" alt="Rectangle" caption="<em>Example Asset</em>" class="border-0" >}}

Here our Asset represents a specific Shipping Crate, it has basic attributes that describe it including capacity, more specific qualities like internal tracking IDs and even a picture to show us its last recorded physical state.

Here is an example of another Asset:

{{< img src="SecondAssetExample.png" alt="Rectangle" caption="<em>Example Asset 2</em>" class="border-0" >}}

In this example our Asset describes the smart lock on a building, this asset has attributes which describe the building it belongs to, the firmware of the lock and even who last used it.

In both of these cases it may be necessary to track more detailed information specific to that class of asset. RKVST allows you to put in as many custom attributes as you need to describe an Asset, allowing you the freedom to record your needs with ease and accessility.

[For more detailed information on Assets and how to implement them please click here]()

What can happen to an Asset?
-----------------------------

Over the lifecycle of an Asset many actions may happen against it, say if an Asset Attribute is changed or there is a noteworthy decision against an Asset, RKVST considers this ***An Event***.

Similarly to an Asset, Events also have an identity, a description and their own set of attributes. Importantly a key attribute of Events is tracking both ***when*** an action happens, ***what*** that action affects and ***who*** acted upon it.

For example:

{{< img src="EventExample.png" alt="Rectangle" caption="<em>Example Event</em>" class="border-0" >}}

Here we can see a single event against our Shipping Crate Asset. We can see that after a physical inspection the Container has an event explaining it was unsealed at a factory, this event has been automatically reported by a sensor on the crate and the event was completed on the 12th March 2020.

We can also see that this event belongs to a specific asset. As more events happen to an asset the richer the information on it becomes, over time your asset will not just be the attributes it is described by but also the sum of it's entire history. 

Events can be very extensive and descriptive but will always belong to a specific Asset, later on in this guide we will see a very basic step by step guide on how to record an event but, [for details on how to implement more comprehnsive Events please refer to this Section]().

Who can perform an Event against an Asset?
-------------------------------------------

Now we understand an Asset is and what sort of Event can happen to it. It is important to understand who can perform an event.

Access to events, assets and their attributes are controlled by two different sets of policies:

* ***ABAC*** (Attribute Based Access Control) - controls access for non-root users of your internal organization to assets and event based on specific attributes
* ***OBAC*** (Organization Based Access Control) - controls access for external organizations to specific assets and events based on specific attributes 

Specifically in the case of OBAC you share access to the root users of the external organization and then those organizations apply ABAC themselves to further share assets and events within their own organization.

To understand more about Root Users and non-Root users, [please refer to the section on Tenancies.]()

Both ABAC and OBAC use the same format for controlling accesses, they provide filters and restrictions to what a specific subject or Actor can read and write following the same generic pattern:

* Subject
* Attribute Read
* Attribute Write
* Event Read
* Event Write

You can also mix and match ABAC and OBAC into the same policy, for example:

{{< img src="IAMPolicyExample.png" alt="Rectangle" caption="<em>Example IAM Policy</em>" class="border-0" >}}

Here we can see an access policy that allows specific members of the Internal Organization, and an External Organisation to read all of the event attributes as well as the Height, Width and Length of Assets. The Users can also create "Dispose" Events as well but they cannot cannot change the attribute of an Asset itself.

We can then define filters for the asset types users are allowed to see, which will be [covered in more detail in the IAM Policies Section.]()

The Golden Thread
-----------------

Now we understand "Who did What to a Thing" we can bring it all together, creating a stream of untamperable, assured and trusted events against an asset to track and follow the key information that is needed. 

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}

We can ensure the data that is recorded is only accessible by the people who need it and those users and organisations can only see what they need to see, when they need to see it.

This provides a strong and compelling platform for cross-organizational, multi-party trust.

To see how this can be applied please check the process modelling section.

To follow continue with the Quickstart guide and create your first asset, [please click here.]()

