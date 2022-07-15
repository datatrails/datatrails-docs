---
title: "Bill of Materials"
description: "Using RKVST to track a Bill of Materials"
lead: "Using RKVST to track a Bill of Materials"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "user-patterns"
weight: 31
toc: true
---

A common pattern for tracking asset lifecycles is the *Bill of Materials* pattern. This is a good choice when dealing with multi-stakeholder systems which change over time, and it is important for the stakeholders to understand the composition of that system no matter who - or what - has changed things.

Modelling such systems in RKVST can help to rapidly answer questions like _"what is in my estate?"_, _"how did it come to be here?"_, and _"who brought it in?"_. In audit situations the Asset histories also allow stakeholders to look back in time and ask _"what did it look like to me at the time? Can I show that I made the best possible decision?"_

## Example 1: Software Bill of Materials (SBOM)

By keeping all the component packages and release history for a software package in one easily identifiable and integrity protected location, all relevant stakeholders can be sure they have the best and most up-to-date information on what software is in their supply chain and how it got there, and can readily identify problems if this record diverges from observed reality.

### Considerations

Key to any successful RKVST integration is keeping the number of asset attributes manageable and meaningful. Do not add every entry in the SBOM as an Asset attribute. Instead preserve Asset attributes to carry essential metadata such as final build hashes and assured current versions, and then put the full details of each released version in attachments and Events. 

Note: There are good standards for storing and exchanging SBOM data such as [SWID/ISO/IEC 19770-2:2015](https://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.IR.8060.pdf "NIST IR 8060"), [Cyclone DX](https://cyclonedx.org "Cyclone DX Homepage"), and [SPDX](https://spdx.github.io/spdx-spec/ "SPDX Specification"). Jitsuin recommends adopting standard data formats wherever possible as these vastly improve interoperability and utility of the data exchanged between RKVST participants.

_SBOM as a living document:_ As a vendor, try to model each final software product as an Asset, and releases/updates to that software product as Events on that Asset. That way, a single Asset history contains all the patch versions of a pristine build standard.

_Link to real assets:_ In reality, not every machine is going to be patched and running identical versions of software, and certainly not the most up-to-date one. As a user of devices, try to link the SBOM from your vendor to the device by having Asset attributes for the Asset Identity of the vendor-published SBOM and the version installed on the device. That way it is easy to find devices that need attention following an SBOM update.

_Access Policies:_ always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Typically very few parties need to update the SBOM record but many people will need to read it.

Remember that RKVST is a shared evidence platform: it is there to help share and publish the SBOM and create the trust and transparency that is demanded of modern systems to ensure the security of the digital supply chain.
