---
title: "State Machine and Supply Chains"
description: "Using RKVST to map a process"
lead: "Using RKVST to map a process"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "user-patterns"
weight: 32
toc: true
---

A common pattern for tracking asset lifecycles is the *State Machine* pattern. This is a good choice for multi-stakeholder process modelling, particularly where the order of operations is important or activities are triggered by actions of partners. Tracing multi-stakeholder business processes in RKVST not only ensures transparency and accountability among parties but is also faster and more reliable than typical cross-organization data sharing and process management involving phone calls and spreadsheets.

Modelling such systems in RKVST can help to rapidly answer questions like _"are my processes running smoothly?"_, _"do I need to act?"_, and _"has this asset been correctly managed?"_. In audit situations the Asset histories also allow stakeholders to look back in time and ask _"who knew what at the time? Could process violations have been detected earlier?"_

## Example 1: Multi-party change management and approvals

This pattern uses a purely virtual Asset to represent a policy or process and coordinate movement through that process, complete with multi-party inputs and approvals. The emphasis here is on Events rather than Asset Attributes: What Happened? Who Was There? What evidence was used to decide to move to the next sage of the process?

### Considerations

_Keep the Asset simple:_ This model typically uses mostly non-modifying events: "what happened" is more important than "what does this Asset look like?". Use Asset Attributes only to clearly identify the business process and store its current state. Otherwise concentrate on recording the When Who Did What in detailed Event attributes at attachments. 

_Map the business process:_ RKVST is here to support business operations, not disturb them. Try as far as possible to define one Event type for each stage of the process so that decisions and artifacts can be recorded naturally and completely during normal operations. In a mature business there may be formal documents such as a Process Map (PM), Business Process Model (BPM) or Universal Modeling Language description of the process, its steps and its approvers. Use this ads a base if it is available.

_Record decisions clearly:_ Future decisions will depend on the evidence of past ones. Make sure that all relevant information is recorded in Event records in the right format for the intended consumer: if decisions are made by humans then rich attachments are a good option, but if software or AI are involved then Event attributes are often a stronger choice.

_Access Policies:_ always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Generally all parties will need read access to all the events in the Asset history but it may be convenient to restrict Event write access to mirror real-world approvers and actors.  

## Example 2: Asset lifecycle tracing

Tracking and tracing the lifecycle of physical assets - from IoT Devices to skyscrapers - is a key strength of RKVST. The ability to collect and examine the entire life history of critical assets - their Provenance - is crucial to building secure and trustworthy systems.

Knowing what state an asset is in, whether or not it is compliant with organizational policy, and whether it needs any attention right now can help a connected system run smoothly. This eliminates the mundane in lifecycle management and allows expert resources to focus only on those parts of the estate that need attention.

### Considerations

_Build the Asset over time_: The Asset lifecycle covers its entire life, from design and build to procurement and use, and finally disposal. During this time the asset evolves and develops new properties and characteristics which are not necessarily foreseeable at creation time. RKVST supports the addition of new properties at any time in the lifecycle so there is no need to design and fill in everything up-front: start with a simple - even empty - Asset and let RKVST track and trace the new properties as they naturally occur.

_Verify and confirm security data_: For digital assets a lot of the effort spent on lifecycle management will be spent on software and firmware management. RKVST's 'Witness Statement' approach to creating Asset Histories enables statements of _intent_ to be recorded alongside _ground truths_, for example a claimed software update next to a digitally signed platform attestation proving that it was done.

_Access Policies:_ Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Generally all parties will need read access to all the events in the Asset history but it may be convenient to restrict Event write access to mirror real-world approvers and actors.  

## Example 3: Supply Chain Handling

_"Multi-party business processes"_ and _"Asset lifecycle tracing"_ are examples of a more general pattern: Supply Chain Handling.

The 'State Machine' and 'Lifecycle Tracing' pattens are very similar, but the former puts a greater emphasis on modeling and tracing the Events while the latter concentrates more on the evolving state of the Assets. Combining these concepts makes it possible to easily trace complex multi-party supply chains without stakeholders having to adapt to each other's ways of working. Everyone participates on their own terms using their own tools and processes, and RKVST bridges the gap to make data available where it is needed.

### Considerations

_GIS position information_: Make good use of the =arc_gic_*= attributes of Events in order to trace *Where* When Who Did What. Remember that physical environment can make a lot of difference to the virtual security of your Assets.

_Access Policies 1:_ Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Nonetheless complete supply chain operations are complex and thought must be given to Access Policy configuration to account for changes of custody. 

_Access Policies 2:_ Consider how far up or down the supply chain visibility should be offered. For example, a customer/operator should be able to see manufacturing data but the manufacturer may or may not be entitled to see usage data.



