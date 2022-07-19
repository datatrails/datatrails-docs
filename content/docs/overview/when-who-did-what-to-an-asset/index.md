---
title: "Who Did What When to an Asset?"
description: "Understanding Shared Evidence"
lead: "Understanding Shared Evidence"
date: 2020-11-12T13:26:54+01:00
lastmod: 2020-11-12T13:26:54+01:00
draft: false
images: []
menu:
  docs:
    parent: "overview"
weight: 4
toc: true
---


Enterprise developers are challenged to build apps that track usage and build trust in multi-party data while meeting assurance, governance, and compliance needs of the business. Assurance needs to be _continuous_ and _system-wide_.

Unlike forming your own blockchain consortium, committing to expensive integrations or managing spreadsheets, RKVST brings the right level of trust in data and confidence in decisions with a single line of code integration at a fraction of cost and time to value.

This guide will give a basic overview of RKVST concepts and get you started quickly with the RKVST UI.  

Before you begin with RKVST there's one key model to use when mapping to business process:

***Who Did What When to an Asset.***

{{< img src="WhenWhoDidWhattoAThing.png" alt="Rectangle" caption="<em>Who did What When to an Asset</em>" class="border-0" >}}

## What is an Asset?

An Asset can be anything; a weather station sensor, an invoice, or even a shipping container. 

An Asset is an object, physical or otherwise, that has an Identity, a Description, and a set of Attributes. 

In most cases, attributes are fairly simple Key-Value pairs. However, RKVST can also store more detailed information, including associated binaries such as PDFs or Pictures.

Take the following example:

{{< img src="AssetExample.png" alt="Rectangle" caption="<em>Example Asset</em>" class="border-0" >}}

Here our Asset represents a specific shipping crate. It has basic Attributes that describe its capacity, more specific Attributes such as internal tracking IDs, and even a picture to show us its last recorded physical state.

Here is an example of another Asset:

{{< img src="SecondAssetExample.png" alt="Rectangle" caption="<em>Example Asset 2</em>" class="border-0" >}}

In this example, our Asset describes a smart-lock on a building. This Asset has Attributes that describe on which building it is installed, its firmware version, and which key last opened it.

RKVST allows you to enter as many custom attributes as you need to describe an Asset, allowing you the freedom to record your needs with ease and accessibility.

For more detailed information on Assets and how to implement them, [please refer to the Assets API Reference](../../api-reference/assets-api/).

## What can happen to an Asset?

Many things may happen to an Asset over its entire lifecycle, either directly affecting its state or decisions about what should happen to it. If an Asset Attribute is changed or if there is a noteworthy decision made about it, RKVST considers this an ***Event***.

Similar to an Asset, Events also have Identities, Descriptions, and their own set of Attributes. Importantly, a key attribute of Events is tracking ***when*** an action happens, ***what*** that action is, and ***who*** acted upon it.

For example:

{{< img src="EventExample.png" alt="Rectangle" caption="<em>Example Event</em>" class="border-0" >}}

Here we can see a single event against our Shipping Crate Asset. We can see that after a physical inspection, the Container has an Event explaining it was unsealed at a factory. This Event has been automatically reported by a sensor on the crate and the Event was completed on the 12th March 2020.

We can also see that this Event belongs to a specific Asset. As more Events happen to an Asset, the richer the information on it becomes. Over time, your Asset will not just be the attributes it is described by but also the sum of its entire shared Event history. 

Events can be very extensive and descriptive but will always belong to a specific Asset. Later on in this guide, we will see a step-by-step example on how to record an event. For details and examples on how to implement more comprehensive Events, [please refer to the Events API Reference](../../api-reference/events-api/).

## Who can perform an Event against an Asset?

Now that we understand what an Asset is and what sort of Event can happen to it, it is important to understand who can perform an Event.

Access to Events, Assets and their Attributes are controlled by two different sets of policies:

* ***ABAC*** (Attribute Based Access Control) - controls access for non-root users of your internal organization to Assets and Events based on specific attributes
* ***OBAC*** (Organization Based Access Control) - controls access for external organizations to specific Assets and Events based on specific attributes 

Specifically, in the case of OBAC, you share access to the root users of the external organization. Then those organizations apply ABAC themselves to further share Assets and Events within their own organization.

Both ABAC and OBAC use the same format for controlling access; they provide filters and restrictions to what a specific subject or Actor can read and write following the same generic pattern:

* `Subject`
* `Attribute Read`
* `Attribute Write`
* `Event Read`
* `Event Write`

You can also mix and match ABAC and OBAC into the same policy, for example:

{{< img src="IAMPolicyExample.png" alt="Rectangle" caption="<em>Example IAM Policy</em>" class="border-0" >}}

Here we can see an access policy that allows specific members of the Internal Organization and an External organization to read all of the event attributes, as well as the `Height`, `Width`, and `Length` of Assets. The Users can also create `Dispose` Events, but they cannot change the attribute of an Asset itself.

We can then define filters for the asset types users are allowed to see, which will be [covered in more detail in the IAM Policies API Reference](../../api-reference/iam-policies-api/).

## The Golden Thread

Now we understand 'Who did What to an Asset'. We can bring it all together, creating a stream of untamperable, assured, and trusted Events against an Asset to track and follow the key information that is needed. 

{{< img src="TheGoldenThread.png" alt="Rectangle" caption="<em>The Golden Thread</em>" class="border-0" >}}

We can ensure the data recorded is only accessible by the people who need it, and those users and organizations can only see what they need to see, when they need to see it.

This provides a strong and compelling platform for building cross-organizational, multi-party trust.

If you'd like to understand more about the application of RKVST to specific Usecases, please see our [User Patterns Section](../../user-patterns/).

