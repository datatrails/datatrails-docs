---
title: "State Machine and Supply Chains"
description: "Using DataTrails to map a process"
lead: "Using DataTrails to map a process"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  usecases:
    parent: "usecases"
weight: 32
toc: true
aliases:
    - /docs/user-patterns/state-machine/
---

A common pattern for tracking an Asset lifecycle is the *State Machine* pattern. This is a good choice for multi-stakeholder process modelling, particularly where the order of operations is important or activities are triggered by actions of partners. Tracing multi-stakeholder business processes in DataTrails not only ensures transparency and accountability among parties, but is also faster and more reliable than typical cross-organization data sharing and process management involving phone calls and spreadsheets.

Modelling such systems in DataTrails can help to rapidly answer questions like _"are my processes running smoothly?"_, _"do I need to act?"_, and _"has this asset been correctly managed?"_. In audit situations, the Asset histories also allow stakeholders to look back in time and ask _"who knew what at the time? Could process violations have been detected earlier?"_

## Example 1: Multi-party change management and approvals

This pattern uses a purely virtual Asset to represent a policy or process and coordinate movement through that process, complete with multi-party inputs and approvals. The emphasis here is on Events rather than Asset attributes: What Happened? Who Was There? What evidence was used to decide to move to the next sage of the process?

### Considerations

**Keep the Asset simple:** This model typically uses mostly non-modifying Events: "what happened" is more important than "what does this Asset look like?". Use Asset attributes only to clearly identify the business process and store its current state. Otherwise, concentrate on recording the `Who Did What When` in detailed Event attributes and attachments.

**Map the business process:** DataTrails is here to support business operations, not disturb them. Try to define one Event type for each stage of the process, so decisions and artifacts can be recorded naturally and completely during normal operations. In a mature business, there may be formal documents such as a Process Map (PM), Business Process Model (BPM) or Universal Modeling Language description of the process, its steps, and its approvers. Use this as a base if it is available.

**Record decisions clearly:** Future decisions will depend on the evidence of past ones. Make sure that all relevant information is recorded in Event records in the right format for the intended consumer: if decisions are made by humans, rich attachments are a good option. If software or AI are involved, then Event attributes are often a stronger choice.

**Access Policies:** Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Generally, all parties will need read access to all the Events in the Asset history, but it may be convenient to restrict Event write access to mirror real-world approvers and actors.  

## Example 2: Asset lifecycle tracing

Tracking and tracing the lifecycle of physical Assets - from IoT Devices to skyscrapers - is a key strength of DataTrails. The ability to collect and examine the entire life history of critical Assets - their provenance - is crucial to building secure and trustworthy systems.

Knowing what state an asset is in, whether or not it is compliant with organizational policy, and whether it needs any attention right now can help a connected system run smoothly. This eliminates the mundane in lifecycle management and allows expert resources to focus only on those parts of the estate that need attention.

### Considerations

**Build the Asset over time:** The Asset lifecycle covers its entire life, from design and build to procurement and use, and finally disposal. During this time the Asset evolves and develops new properties and characteristics which are not necessarily foreseeable at creation time. DataTrails supports the addition of new properties at any time in the lifecycle so there is no need to design and fill in everything up-front. Start with a simple - even empty - Asset and let DataTrails track and trace the new properties as they naturally occur.

**Verify and confirm security data:** For digital Assets, a lot of the effort spent on lifecycle management will be spent on software and firmware management. DataTrails's 'Witness Statement' approach to creating Asset histories enables statements of _intent_ to be recorded alongside _ground truths_. For example, a claimed software update next to a digitally signed platform attestation proving that it was done.

**Access Policies:** Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Generally, all parties will need read access to all the Events in the Asset history but it may be convenient to restrict Event write access to mirror real-world approvers and actors.  

## Example 3: Supply Chain Handling

_"Multi-party business processes"_ and _"Asset lifecycle tracing"_ are examples of a more general pattern: Supply Chain Handling.

The 'State Machine' and 'Lifecycle Tracing' pattens are very similar, but the former puts a greater emphasis on modeling and tracing the Events while the latter concentrates more on the evolving state of the Assets. Combining these concepts makes it possible to easily trace complex multi-party supply chains without stakeholders having to adapt to each other's ways of working. Everyone participates on their own terms using their own tools and processes, and DataTrails bridges the gap to make data available where it is needed.

### Considerations

**GIS position information:** Make good use of the =arc_gis_*= attributes of Events in order to trace *Where* Who Did What When. Remember that physical environment can make a lot of difference to the virtual security of your Assets.

**Access Policies 1:** Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Nonetheless, complete supply chain operations are complex and thought must be given to Access Policy configuration to account for changes of custody.

**Access Policies 2:** Consider how far up or down the supply chain visibility should be offered. For example, a customer/operator should be able to see manufacturing data but the manufacturer may or may not be entitled to see usage data.
