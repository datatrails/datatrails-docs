---
title: "Supply Chain: Chain of Custody"
description: "DataTrails ensures Integrity, Transparency and Trust for Supply Chains"
lead: "Tracking the Chain of Custody"
date: 2024-03-26T14:03:19Z
lastmod: 2024-03-26T14:03:19Z
draft: false
images: []
menu: 
  usecases:
    parent: "usecases"
weight: 34
toc: true
---

*"Multi-party business processes"* and *"Asset lifecycle tracing"* are examples of a more general pattern: Supply Chain Handling.

The 'State Machine' and 'Lifecycle Tracing' pattens are very similar, but the former puts a greater emphasis on modeling and tracing the Events while the latter concentrates more on the evolving state of the Assets. Combining these concepts makes it possible to easily trace complex multi-party supply chains without stakeholders having to adapt to each other's ways of working. Everyone participates on their own terms using their own tools and processes, and DataTrails bridges the gap to make data available where it is needed.

The *Chain of Custody* is a documented record of the people or entities that physically or digitally handle a product as it moves from constituent parts to the end customer.

By combining all three, to complete the Supply Chain, DataTrails allows you to:  

* Enable global visibility to all stakeholders
* Provide continuous data assurance for accessibility, integrity and resilience
* Integrate with physical items and devices in a platform agnostic way
* Comply with internal and external regulatory standards
* Use defined and continuously improving process

## Chain of Custody
DataTrails records `who did what when` (and `where` when appropriate) to build an immutable and auditable record of the entire history of an product as it passes through the supply chain.

The platform allows multi-party sharing and visibility of supply chain data which empowers trusted data exchange and verification. Supply chain partners have a single source of truth that gives them confidence that decisions are made by the right people, at the right step of the process, using the right data and with confidence that the data is the correct version and is untampered. 

It also provides proof of the ownership and operational status of both digital and physical assets and enhances statements of compliance and quality assurance. 

 operational efficiency.

### Considerations

**Custom Attributes:** A core set of attributes can be created specifically to suit each asset and event type. DataTrails has the flexibility to allow these to be modified as the business needs develop over time. They are not set in stone.

**GIS position information:** Make good use of the arc_gis_* attributes of Events in order to trace *Where* Who Did What When. Remember that physical environment can make a lot of difference to the virtual security of your Assets.

**Access Policies 1:** Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Nonetheless, complete supply chain operations are complex and thought must be given to Access Policy configuration to account for changes of custody.

**Access Policies 2:** Consider how far up or down the supply chain visibility should be offered. For example, a customer/operator should be able to see manufacturing data but the manufacturer may or may not be entitled to see usage data.
