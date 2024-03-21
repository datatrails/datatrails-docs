---
title: "Bill of Materials"
description: "Using DataTrails to track a Bill of Materials"
lead: "Using DataTrails to track a Bill of Materials"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  usecases:
    parent: "usecases"
weight: 33
toc: true
aliases:
  - /docs/user-patterns/bill-of-materials/
---

A common pattern for tracking an asset's lifecycle is the *Bill of Materials* pattern. This is a good choice when dealing with multi-stakeholder systems which change over time, and it is important for the stakeholders to understand the composition of that system no matter who - or what - has changed things.

Modelling such systems in DataTrails can help to rapidly answer questions like _"what is in my estate?"_, _"how did it come to be here?"_, and _"who brought it in?"_. In audit situations the Asset histories also allow stakeholders to look back in time and ask _"what did it look like to me at the time? Can I show that I made the best possible decision?"_

## Example: Software Bill of Materials (SBOM)

Maintaining and publishing an accurate Software Bill of Materials (SBOM) is an essential cybersecurity activity for all vendors of critical software and cyber physical systems. However, publishing is not enough: users of the software also need to be able to find the information and be able to understand it in order to make strong and rational decisions about their own system security.

By keeping all the component packages and release history for a software package in one easily identifiable and integrity protected location, all relevant stakeholders can be sure they have the best and most up-to-date information on what software is in their supply chain and how it got there. Stakeholders can then readily identify problems if this record diverges from observed reality.

In its [recommendations for the minimum required elements of an SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom), the NTIA identifies the need to balance transparency with access controls ("*SBOMs should be available in a timely fashion to those who need them and must have appropriate access permissions and roles in place*"), and illustrates in its [NTIA SBOM Proof of Concept](https://www.ntia.doc.gov/files/ntia/publications/ntia_sbom_energy_pocplanning.pdf) the need for strong stakeholder community management and a trusted SBOM data sharing mechanism which protects the interests of all parties.

The DataTrails Software Package profile is a set of suggested Asset and Event attributes that offers a solution to this sharing and distribution problem: vendors retain control of their proprietary information and release processes while customers have assured and reliable visibility into their digital supply chain risks with reliable access to current and historical SBOM data for the components they rely on.

As an Asset, a Software Package may hold many different SBOMs over its lifecycle representing the introduction of new releases and versions of the Software Package. Each ‘Release’ is recorded as an Event to capture the known SBOM at the time.

If a particular Software Package has constituent components composed of other Software Package Assets this would be tracked within the SBOM of the component Supplied Software Package, ensuring full traceability across the Supply Chain.

### Considerations

Key to any successful DataTrails integration is keeping the number of Asset attributes manageable and meaningful. ***Do not add every entry in the SBOM as an Asset attribute.*** Instead, preserve Asset attributes to carry essential metadata such as final build hashes and assured current versions, and put the full details of each released version in attachments and Events.

Note: There are good standards for storing and exchanging SBOM data such as [SWID/ISO/IEC 19770-2:2015](https://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.IR.8060.pdf "NIST IR 8060"), [Cyclone DX](https://cyclonedx.org "Cyclone DX Homepage"), and [SPDX](https://spdx.github.io/spdx-spec/ "SPDX Specification"). DataTrails recommends adopting standard data formats wherever possible, as these vastly improve interoperability and utility of the data exchanged between DataTrails participants.

*SBOM as a living document:* As a vendor, try to model each final software product as an Asset, and releases/updates to that software product as Events on that Asset. That way, a single Asset history contains all the patch versions of a pristine build standard.

*Link to real assets:* In reality, not every machine is going to be patched and running identical versions of software, and certainly not the most up-to-date one. As a user of devices, try to link the SBOM from your vendor to the device by having Asset attributes for the Asset Identity of the vendor-published SBOM and the version installed on the device. That way it is easy to find devices that need attention following an SBOM update.

*Access Policies:* Always try to avoid proliferating Access Policies and make as few as possible with clear user populations and access rights. Typically, very few parties need to update the SBOM record, but many people will need to read it.

{{< note >}}
**Remember that DataTrails is a shared evidence platform.** It is there to help share and publish the SBOM and create the trust and transparency that is demanded of modern systems, to ensure the security of the digital supply chain.
{{< /note >}}
