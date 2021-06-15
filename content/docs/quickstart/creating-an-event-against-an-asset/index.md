---
title: "Creating an Event Against an Asset"
description: ""
lead: ""
date: 2021-05-18T15:32:01+01:00
lastmod: 2021-05-18T15:32:01+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 3
toc: true
---

If you wish to begin tracking your Asset history, you need to create Events.

Asset Creation is the first Event and the more Events recorded against an Asset, the richer and deeper its history becomes.

Events track key moments of an Asset's lifecycle; details of When Who Did What to an Asset.

## Creating Events

1. When viewing your Asset select the `Record Event` button.

{{< img src="EventRecord.png" alt="Rectangle" caption="<em>Recording an Event</em>" class="border-0" >}}

2. You will see the following screen, where you can enter an Event type and description.

{{< img src="EventInformation.png" alt="Rectangle" caption="<em>Entering Event Details</em>" class="border-0" >}}

3. Tabs enable you to enter both Event and Asset attributes.

* `Event Attributes` - Attributes specific to an Event e.g. which device recorded the Event
* `Asset Attributes` - Attributes of the Asset that may change as a result of the Event e.g. overall weight of a container

Select the `Add Attribute` button on each field to add your Key-Value pairs.

For example:

{{< img src="EventAttributes.png" alt="Rectangle" caption="<em>Event Specific Attributes</em>" class="border-0" >}}

{{< img src="EventAssetAttributes.png" alt="Rectangle" caption="<em>Event Asset Attributes</em>" class="border-0" >}}

Here we see someone noted the type of cargo loaded in the Event, and has also recorded the total weight of the cargo using a newly defined `Weight` attribute.

Every Event has an automatically generated `timestamp_accepted` and `principal_accepted` attribute that records when who performed what as submitted to RKVST.

There is an option to append `timestamp_declared` and `principal_declared` attributes on the Event. For example if the Event happened offline or is reported by a third party, which helps to create a detailed record.

PDFs or images can be recorded with an Event in the same way as an Asset. 

This is useful for storing associated material for posterity. For example, each `Inspection` Event can store the PDF document of a specific standard for container inspection. This allows historical compliance checking of Events.

4. Once you have entered all data, select the `Record Event` Button, to add to your Asset.

You will see that the Asset Attribute we changed is also recorded in the Asset View.

{{< img src="EventRecorded.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

5. Use the eye symbol ( ![](EyeSymbol.png) ) to inspect the Event:

{{< img src="EventView.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here we see the details entered earlier and also a tab that will show both the Event Attributes and Asset Attributes:

{{< img src="EventAttributeView.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}

In the next section we will learn about using [Locations](../../locations/locations-overview) to group items together for both logical grouping and better access management using [ABAC and OBAC Policies](../../iam-policies/iam-policies-overview).

