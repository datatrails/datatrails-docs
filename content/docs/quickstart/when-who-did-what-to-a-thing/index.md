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


Enterprise developers are challenged to build apps that track usage and build trust in multi-party data while meeting assurance, governance and compliance needs of the business. 

The Jitsuin RKVST is a Data Assurance Hub which stores shared asset evidence that proves when who did what to reduce risk, authenticates provenance in data for confident decisions, while governing complex data sharing controls. 

Unlike forming your own blockchain consortium, committing to expensive integrations or managing spreadsheets, RKVST brings the right level of trust to data with a single line of code integration at a fraction of cost and time to value.

This guide will get you started quickly with the Archivist UI and provide an understanding of core RKVST concepts.  

Before you begin with RKVST there's one key concept to shape your thinking: 

***When who did what to a thing.***

{{< img src="WhenWhoDidWhattoAThing.png" alt="Rectangle" caption="<em>When who did what to a thing</em>" class="border-0" >}}

What is a Thing?
----------------

A Thing can be anything; a weather station sensor, an invoice or even a shipping container. Whatever this Thing may be, in RKVST considered it an ***Asset***.

At its core an Asset is an object, physical or otherwise, that is uniquely identifiable, and is a describable with a set of attributes. 

In most cases attributes are fairly simple Key-Value pairs, however RKVST can also store more detailed information including associated binaries, PDFs or Pictures.

Take the following example:


{{< img src="AssetExample.png" alt="Rectangle" caption="<em>Example Asset</em>" class="border-0" >}}

Here our Asset represents a specific shipping crate, it has basic attributes that describe it including capacity, more specific attributes such as internal tracking IDs and even a picture to show us its last recorded physical state.

Here is an example of another Asset:

{{< img src="SecondAssetExample.png" alt="Rectangle" caption="<em>Example Asset 2</em>" class="border-0" >}}

In this example our Asset describes a smart lock on a building, this asset has attributes describing on which building it is installed, the firmware version and which key last opened it.

In both of these cases it may be necessary to track more detailed information specific to that class of asset. RKVST allows you to create as many custom attributes as you need to describe an Asset, allowing you the freedom to record your needs with ease and accessibility.

[For more detailed information on Assets and how to implement them please click here]()

What happens to an Asset?
-----------------------------

Many things may happen to an Asset over its entire lifecycle, either directly affecting its state or decisions about what should happen to it. If an Asset Attribute is changed or there is a noteworthy decision upon an Asset, RKVST considers this an ***Event***.

Similar to an Asset, Events also have identities, descriptions and their own set of attributes. Importantly a key attribute of Events is tracking both ***when*** an action happens, ***what*** that action is and ***who*** acted upon it.

For example:

{{< img src="EventExample.png" alt="Rectangle" caption="<em>Example Event</em>" class="border-0" >}}

Here we can see a single Event recorded on our Shipping Crate Asset. We can see that after a physical inspection the Container has an Event explaining it was unsealed at a factory; this Event has been automatically reported by a sensor on the crate and the event was completed on the 12th March 2020.

We can also see that this Event belongs to a specific Asset. As more Events happen to an Asset the richer the information on it becomes. Over time your Asset will not just be the attributes it is described by but also the shared asset evidence history of its entire lifecycle. 

Events can be very extensive and descriptive but will always belong to a specific Asset, later on in this guide we will see a very basic step-by-step guide on how to record an Event but, [for details on how to implement more comprehensive Events please refer to this Section]().

Who can create an Event against an Asset?
-------------------------------------------

Now we understand an Asset is and what sort of Events can happen to it. It is important to understand who can perform an Event.

Access to events, assets and their attributes are goverened by two different sets of policies:

* ***ABAC*** (Attribute Based Access Control) - controls access for non-root users of your internal organization to Assets and Events based on specific attributes
* ***OBAC*** (Organization Based Access Control) - controls access for external organizations to specific Assets and Events based on specific attributes 

Specifically in the case of OBAC you share access to the root users of the external organization and then those organizations apply ABAC themselves to further share Assets and Events within their own organization.

To understand more about Root Users and non-Root users, [please refer to the section on Tenancies.]()

Both ABAC and OBAC use the same format for controlling access, they provide filters and restrictions to what a specific subject or Actor can read and write following the same generic pattern:

* Subject
* Attribute Read
* Attribute Write
* Event Read
* Event Write

You can also mix and match ABAC and OBAC into the same policy, for example:

{{< img src="IAMPolicyExample.png" alt="Rectangle" caption="<em>Example IAM Policy</em>" class="border-0" >}}

Here we can see an access policy that allows specific members of the Internal Organization, and an External Organisation to read all Event attributes as well as the Height, Width and Length of Assets. The Users can also create "Dispose" Events as well but they cannot cannot change the attribute of an Asset itself.

We can then define filters for the Asset types users are allowed to see, which will be [covered in more detail in the IAM Policies Section.]()

The Golden Thread
-----------------

Now we understand "Who did What to a Thing" we can bring it all together, creating a stream of untamperable, assured Events on Assets track that build a complete traceable historical record that builds trust in the key information needed by data users. 

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}

We can ensure the recorded data is only accessible by the people and organsiations who need to see it. Those users who need to know see the same data as other authorised users.

This provides a strong and compelling Data Assurance Hub for multi-party trust.

To see how this can be applied please check the process modelling section.

To follow continue with the Quickstart guide and create your first asset, [please click here.]()

