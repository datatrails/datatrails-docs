---
title: "Supply Chain: State Machine"
description: "DataTrails ensures Integrity, Transparency and Trust for Supply Chains"
lead: "Tracking multi-stakeholder business processes"
date: 2024-03-26T14:03:01Z
lastmod: 2024-03-26T14:03:01Z
draft: false
images: []
menu: 
  usecases:
    parent: "usecases"
weight: 31
toc: 
aliases:
    - /docs/user-patterns/state-machine/
    - /usecases/state-machine/
---

A common pattern for tracking an Asset lifecycle is the *State Machine* pattern. This is a good choice for multi-stakeholder process modelling, particularly where the order of operations is important or activities are triggered by actions of partners. Tracing multi-stakeholder business processes in DataTrails not only ensures transparency and accountability among parties, but is also faster and more reliable than typical cross-organization data sharing and process management involving phone calls and spreadsheets.

Modelling such systems in DataTrails can help to rapidly answer questions like *"are my processes running smoothly?"*, *"do I need to act?"*, and *"has this asset been correctly managed?"*. In audit situations, the Asset histories also allow stakeholders to look back in time and ask *"who knew what at the time? Could process violations have been detected earlier?"*

## Multi-party change management and approvals

This pattern uses a purely virtual Asset to represent a policy or process and coordinate movement through that process, complete with multi-party inputs and approvals. The emphasis here is on Events rather than Asset attributes: What Happened? Who Was There? What evidence was used to decide to move to the next sage of the process?

### Considerations

**Keep the Asset simple:** This model typically uses mostly non-modifying Events: "what happened" is more important than "what does this Asset look like?". Use Asset attributes only to clearly identify the business process and store its current state. Otherwise, concentrate on recording the `Who Did What When` in detailed Event attributes and attachments.

**Map the business process:** DataTrails is here to support business operations, not disturb them. Try to define one Event type for each stage of the process, so decisions and artifacts can be recorded naturally and completely during normal operations. In a mature business, there may be formal documents such as a Process Map (PM), Business Process Model (BPM) or Universal Modeling Language description of the process, its steps, and its approvers. Use this as a base if it is available.

**Record decisions clearly:** Future decisions will depend on the evidence of past ones. Make sure that all relevant information is recorded in Event records in the right format for the intended consumer: if decisions are made by humans, rich attachments are a good option. If software or AI are involved, then Event attributes are often a stronger choice.

**Access Policies:** Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Generally, all parties will need read access to all the Events in the Asset history, but it may be convenient to restrict Event write access to mirror real-world approvers and actors.  

**Compliance Policies** If the process must meet recognized standards and is subject to regular audits these can be monitored and recorded using a compliance policy. 
