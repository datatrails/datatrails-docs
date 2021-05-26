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

If you wish to begin tracking actions against your asset you need to create events.

While the Asset Creation phase is important it is only the first event in an Asset's history. The more events you create against an asset, the richer and deeper its' history becomes.

Events are where we track many of the key features of the Asset's lifecycle; this is where we track in closer detail the When, the Who and the What happens to the Asset.

Creating Events
---------------

1. When viewing your Asset select the 'Record Event' button

{{< img src="EventRecord.png" alt="Rectangle" caption="<em>Recording an Event</em>" class="border-0" >}}

2. This will open up the following screen, where you can record the type of event that occured and a description

{{< img src="EventInformation.png" alt="Rectangle" caption="<em>Entering Event Details</em>" class="border-0" >}}

3. You will also have tabs available to add both event attributes and asset attributes

* Event Attributes - Attributes specific to an event e.g. which device was used to record the event
* Asset Attributes - Attributes of the Asset that may change as a result of the event e.g. overall weight of the container

Similar to Asset Creation you would select the 'Add Attribute' button on each and then add your Key-Value pairs.

For example:

{{< img src="EventAttributes.png" alt="Rectangle" caption="<em>Event Specific Attributes</em>" class="border-0" >}}

{{< img src="EventAssetAttributes.png" alt="Rectangle" caption="<em>Event Asset Attributes</em>" class="border-0" >}}

Here we can see that someone has noted down the type of cargo being loaded at the time in the Event but has marked the overall weght of the cargo against the asset itself.

We could have optionally set the timestamp_declared and principal_declared attributes on the event if we were not the ones who performed the inspection, or had done it a significant time ago, which helps to create a more obvious and compelling source of truth on events.

You can also optionally upload a pdf or image with an event in the same way you would an Asset. This is useful for when associated material should be uploaded for posterity. For example if a container is inspected against one set of standards a PDF of those standards can be stored with the inspection so that people can see what criteria was being used at the time.

4. Once complete you can select the Record Event Button, the event should then be recorded against you specific asset.

You should also see the Asset Attribute we changed has also been recorded in the Asset View also.

{{< img src="EventRecorded.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

5. We can then use the same eye symbol ( ![](EyeSymbol.png) ) we used to inspect the Asset to dig deeper in to the Event like so:

{{< img src="EventView.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here we can see the details we filled out earlier and we can also see we have a tab available that will show us both the Event Attributes and Asset Attributes we added like so:

{{< img src="EventAttributeView.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}

In the next section we will learn about using [Locations]() to group items together for both logical grouping and better access management using [ABAC]() and [OBAC]().

