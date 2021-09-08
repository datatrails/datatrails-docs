---
title: "Tutorial"
description: "Draft"
lead: "Draft"
date: 2021-05-18T15:33:31+01:00
lastmod: 2021-05-18T15:33:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 26
toc: true
---

## How to think about RKVST

When planning to use RKVST it is important to consider not just what you need to track but how to track it and what information you may want to share with others along the way.

These considerations and their conclusions can vary heavily from situation to situation, the following guide will take you through a basic walkthrough of how to build up your RKVST solution.

### Planning your Asset

Often many know ahead of time what they would like to track in RKVST; whether it's a Shipping Container and its route, the status of a Software Bill of Materials as a product gets updated or even the impact of decisions made during a business process.

Whether you do know or not, it would be worth asking the following questions to establish a good understanding of what you aim to achieve with RKVST:

**What am I interested in tracking?**

Here you need to consider what information you are interested in, is it a particular object whose history you would like to track?

Maybe you have a process your business is performing and you'd like to add some kind of assurance to it?

What kind of assurance are you seeking?

We'll follow along with a simple example to illustrate; I am interested in tracking the changes my bike will go through over it's lifetime.

**Why am I interest in tracking this?**

Here we need to consider why this process or object needs assurance.

Why is it we need to track it? What do we hope to gain by tracking it?

Some things to consider are the following:

* **Metadata Governance** - Empowering the right people in organizations to set, enforce and execute complex data sharing policies.

* **Authenticated Provenance** - Delivering full traceability on all internal and external data sources to speed and assure critical decisions.

* **Continuous Accountability** - Instantly auditable evidence “Proves When Who Did What” for any shared asset to delight your GRC team.

* **Persistent Integrity** - Create a complete, unbroken, and permanent record of shared event transactions, delivering continuous assurance for faster critical decisions.

Applying this to our bike example:

I am an avid cyclist, it is important my bike is always in top condition when I go racing.

I would like to be able to go into any race assured that my bike has a recorded history of being properly serviced by the right mechanics.

I should be able to asset that once serviced all of the parts are in order, so that I can assure my bike's integrity has not been tampered with.

This should also mean that if I ever choose to sell my bike I can demonstrate to the buyer a full history of all changes to my bike and I can resolve any queries or disputes that may occur.

**What are the properties of the item I am interested in tracking?**

As discussed in our [Core Concepts Section](../../overview/core-concepts#assets):

>RKVST Assets are essentially very simple: a collection of attributes that describe the Asset expressed as a standard JSON document.

This collection of attributes that describe the Asset are called `Asset Attributes`.

These are individual properties of the Asset itself and the Asset Attributes should always be up to date with the state of the Asset.

When considering my bike I am interested in a number of things:

* Tracking the serial numbers of the replaceable parts
* Tracking the last time the bike raced
* Tracking the last time the bike got serviced
* Tracking who last serviced it

I am also interested in tracking the times I placed in my last few races as well.

You should notice that some of these things I'd like to track aren't strictly properties of the bike itself.

This is because we have also have another aspect of our bike to consider, what kind of Events can happen to the bike?

### Planning Events

There are things that happen throughout an Asset's lifecyle that you may want to track.  

These events are important because they could change an Asset's state, change an Asset's Attribute, verify that an activity has been performed or help with a dispute or audit.

It's not a requirement to track every event, only those that help prove **Who Did What When**.  

The below questions will help you identify events the kind of events you may be interested in.

**What kind of things can happen to my asset?**

Let's discuss what could happen to my bike:

* Worn or Damaged Parts: broken chain, flat tire
* Maintenance: Cleaning, checking brake pads
* Upgrade: bar tape, tires, saddle

I am interested in these events as they impact the bike itself; the performance of the bike and the ability to race. 

**What kind of decisions that are made during my assets lifecycle am I interested in?**

Not all decisions made require tracking, however those that affect the state of my bike, change an attribute or help me verify that an activity has been
performed are decisons of interest.

Based on the aforementioned events, let's take a look at actions of importance:

- Worn or Damaged Parts:
   - What parts have been replaced?
   - Who replaced the parts?
   - When were the parts replaced?
- Maintenance:
   - What type of maintenance was done?
   - Who performed the maintenance?
   - When was the mainteance performed?
- Upgrade:
   - What was upgraded?
   - Who did the upgrade?
   - When was the upgrade performed?

The answers to the above help me understand alterations to my bike in addtion to proving **Who Did What When**.  

The tracking of these answers will help with dispute resolution and hopefully lessen confusion between parties.

**What are the properties of these decisions that I am interested in tracking?**

Properties of interest would be those that: change the state of an Asset, change an attribute of the Asset, verify that a relevant activity has been performed and/or would help
with dispute resolution.  

Depending on the type of Asset these properties can range from: location change, change in size (i.e. weight), verification and validation just to name a few.

Focusing on the bike, let's take a look at properties of interest:

- Worn or Damaged Parts:
   - Type of part replaced
   - Serial number of part
- Upgrade:
   - Type of part upgraded
   - Serial number of upgraded part

Understanding the impact of a replaced or upgraded part is important because it could change the dynamics of my bike.

These critical changes could significantly affect the performance, change the look and feel and/or increase longevity.  

**What kind of changes to the Asset can I expect, does it gain more properties? Does it change properties itself as a result of the event?**

Part of understanding what to track and what not to track, is knowing which properties may change the Asset.  

In addition, does the change to the Asset have other affects.

For example, changing the frame of the bike could change the color/look, however upgrading the tires may not change the look but will change the performance.

Let's add the above as part of my bike's lifecycle:

- Worn or Damaged Parts:
   - Replacing frame (same size as old frame but different color)
- Upgrade:
   - Tires for higher performance during inclement weather/terrain

Changes that I could expect from the above events and how they affect my bike.

- Replacement Frame
   - Color Change 
   - Size (still want to track to ensure the sizing hasn't changed)
   - Make/model of frame
- New Tires
   - Make/model of tires
   - Size of tires
   - PSI of tires

After the above work is completed, my Asset will change.  In addition to tracking the process of the installation, I also want to know how my bike changed post completion.  My bike looks and feels different and I want to track the final result.

**Who needs to see which events and which properties?**

My bike is getting a new frame and tires, who else needs to know about this?  Who are the important parties involved?

- Me: owner of the bike
- Two shops: one will install the frame and the other will upgrade the tires

The owner (me), I want to be able to view the entire lifecycle of my bike.  From when I drop it off to when I pick it up and everything in between.

The frame shop, should be able to view all things related to my new frame: status of order, color of frame, make/model, dimenstions, etc.  Events and properties related to the frame should be available for the shop to also update.

The tire shop, should be able tto view all things related to my new tires: status of order, make/model, dimensions, type of tire, etc.  Events and properties related to the tires should be available for the shop to also update.

The two shops should be able to view progress but it's not a requirement to see "everything".  My bike will be at the frame shop first, then when done will be dropped off at the tire shop.
Both shops should see when I dropped off the bike making parties aware that the lifecycle has begun.  However, the tire shop should only need to know when the frame shop is done and ETA of drop off, so they can begin work. Establishing the above will increase effecient and effective communication.

### Planning who to Share with

When sharing data, it's important to understand: who needs to see what, when do they need to see it and who requires read and/or write access.  Recognizing these aspects will ensure that **the right data will be shared at the right time to the right resources**.

## Creating an Asset

1. Using the Sidebar, select `Add Asset`.

{{< img src="AssetAdd.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}

2. You will see an Asset Creation form, where you provide details of your new Asset:

{{< img src="AssetCreateNT.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}

3. At minimum, you will need to add an Asset Name and Asset Type when using the UI to create an Asset:

* `Asset Name` - This is the unique name of the Asset i.e. 'My First Container'
* `Asset Type` - This is the class of object, while it is arbitrary, it is best to have consistency amongst the type of Assets you use i.e. if it is a shipping container, the type could be `Shipping Container` which will then be pre-populated for future Assets to use as their own types

{{< img src="AssetCreationDetailsNT.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}

4. At this point, you may wish to add other details to your Asset including attachments such as PDFs or Thumbnail Images. You may also wish to add Extended Attributes. 

Extended Attributes are user-defined and can be added to each unique Asset. 

Not all Assets of a specific type need to have the same Extended Attributes, but in most cases it is better to do so for consistency. 

To add a new Attribute to an Asset select `Add Attribute` then enter your key-value pair.

For Example:

{{< img src="AssetExtendedAttributesNT.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}

5. Once complete, click `Create Asset`

{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}

6. Navigate to `Manage Assets` to see your Asset in the UI.

{{< img src="AssetManage.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}

7. To view your Asset, click on the small eye symbol ( ![](EyeSymbol.png) ) to the right of the Asset in the Manage view. You will see the detailed history of your Asset.

{{< img src="AssetView.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}

Here we see all details entered: The Extended Attributes and a history of Events recorded on the Asset.

The first Event will always be the Asset Creation, in the next section we will cover how to create your own Events for your Asset.


## Adding External Organizations to Allow Sharing

In order to share Assets and their details with another Organization or Tenant we must first import the ID of the External Organization.

### Finding Your Own ID

1. As a Root User, navigate to `Access Policies`

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and your Organization's ID will be contained within the `Self` box.

This string is the one you should share with a 3rd Party who wants to share their data with you.

{{< img src="PolicyOBACSubjectSelf.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

### Importing another Organization's ID

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and then `Import Subject`.

{{< img src="PolicyOBACSubjectImport.png" alt="Rectangle" caption="<em>Importing a Subject</em>" class="border-0" >}}

3. You will be presented with a form, the `Subject String` is the ID of the Organization with which you wish to share Asset evidence. The `Name` is a Friendly Name for you to label the imported organization.

{{< img src="PolicyOBACSubjectAdd.png" alt="Rectangle" caption="<em>Adding the Subject</em>" class="border-0" >}}

## Creating an OBAC Sharing Policy

1. Navigate to the `Access Policies` section on the Sidebar of the RKVST Dashboard.

{{< img src="PolicyManage.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

2. Here you will see any existing policies, select `Add Policy`.

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a policy the following form will appear:

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. Here you can begin applying filters to your Policy for the right assets. In this case we're going to filter for any Assets in the `UK Factory` Location created earlier.

{{< img src="PolicyOBACFilter.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Next we select the `Permissions` Tab to set which Organizations can read and write certain Asset attributes, as well as Event visibility.

{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In our case we want the `Organization` actor which implies OBAC. Type the Friendly Name of the Organization we wish to share with into the box and we should see a prepopulated drop-down search.

{{< note >}} **Note:** You will need to have imported another Organization's ID before you can specify a policy to share information with that Organization. {{< /note >}}

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. When the relevant controls are in place we then add the Permisson Group to the policy.

Note we have included RKVST-significant atributes: `arc_display_name` and `arc_display_type` which brings visibility to the Name and Type of Asset being shared. 

{{< img src="PolicyOBACPermissions.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete, submit the policy and check the Asset is shared appropriately; Mandy should only be able to see the Name and Type of Asset as well as the Asset's custom `Weight` attribute.

{{< img src="PolicyOBACMandyView.png" alt="Rectangle" caption="<em>Mandy's view as a Root User of the External Organization</em>" class="border-0" >}}

By comparison our Root User, Jill, can see the full details of the Asset:

{{< img src="PolicyOBACJillView.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

9. If Mandy wishes to share what she can to Non-Root Users within her organization, it is her responsibility to create an ABAC Policy as she would any other Asset she has access to.

There are many possible fine-grained controls and as such ABAC and OBAC Policy Creation is an extensive topic. To find out more, head over to the [IAM Policies API Reference](../../api-reference/iam-policies-api/).


## Creating Events

1. When viewing your Asset click the `Record Event` button.

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

Every Event has an automatically generated `timestamp_accepted` and `principal_accepted` attribute that records _when_ who performed what, as submitted to RKVST.

There is an option to append `timestamp_declared` and `principal_declared` attributes on the Event. For example, if the Event happened offline or a third party reports it. This option helps to create a detailed record.

PDFs or images can be recorded with an Event in the same way as an Asset. 

This is useful for storing associated material for posterity. For example, each `Inspection` Event can store the PDF document of a specific standard for container inspection. This allows historical compliance checking of Events.

4. Once you have entered all data, click the `Record Event` Button, to add to your Asset.

You will see that the Asset Attribute we changed is also recorded in the Asset View.

{{< img src="EventRecorded.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

5. Use the eye symbol ( ![](EyeSymbol.png) ) to inspect the Event:

{{< img src="EventView.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here we see the details entered earlier and also a tab that will show both the Event Attributes and Asset Attributes:

{{< img src="EventAttributeView.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}
