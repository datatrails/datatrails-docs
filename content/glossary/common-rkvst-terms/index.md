---
title: "Common RKVST Terms"
description: ""
lead: ""
date: 2022-10-19T07:39:44-07:00
lastmod: 2022-10-19T07:39:44-07:00
draft: false
images: []
menu: 
  glossary:
    parent: "glossary"
weight: 51
toc: true
aliases: 
  - /docs/glossary/common-rkvst-terms/
---

Select a term for more information.

| **Term**            | **Definition**                                                                                                       |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| [ABAC](/platform/administration/managing-access-to-an-asset-with-abac/)                | Attribute-Based Access Control; policy that allows you to grant fine-grain access to members of your Tenancy         |
| [access policy](/platform/overview/core-concepts/#access-policies)       | grants chosen Asset and Event access to stakeholders                                                                 |
| [administrator](/developers/developer-patterns/getting-access-tokens-using-app-registrations/#creating-an-app-registration)           | user with permission to see all Asset and Event information within a Tenancy, and to grant access to other users                                   |
| [anchored](/developers/developer-patterns/verifying-with-simple-hash/)  | Simple Hash events are committed to the blockchain by hashing them in batches. The hash recorded on the chain is called the anchor |
| [asset](/platform/overview/core-concepts/#assets)               | an RKVST Asset is an entry in your tenancy, which has a collection of attributes that describes its current state and a complete life history of Events |
| [asset_attributes](/platform/overview/creating-an-asset/#creating-an-asset)    | key-value pairs that represent information about an Asset                                                            |
| [audit trail](https://en.wiktionary.org/wiki/audit_trail) | a formal record of activities (Events) that are made against a piece of data (an Asset)|
| [bearer token](/platform/overview/creating-an-asset/#creating-an-asset)        | access token for RKVST API; created using Custom Integration credentials                                               |
| [behaviours](/platform/overview/creating-an-asset/#creating-an-asset)          | detail what class of events in an Asset lifecycle you might wish to record                                           |
| [compliance policy](/platform/administration/compliance-policies/)   | user-defined rule sets that Assets can be tested against
| [custom integration](/developers/developer-patterns/getting-access-tokens-using-app-registrations/#creating-an-app-registration)    | client ID and client secret credentials that are used to access the RKVST API. Formerly known as an App Registration                                                             |
| [event](/platform/overview/core-concepts/#events)               | tracks key moments of an Asset lifecycle; details of Who Did What When to an Asset                                   |
| [event_attributes](/platform/overview/creating-an-event-against-an-asset/#creating-events)    | key-value pairs that represent information about an Event                                                            |
| [integration](/platform/administration/dropbox-integration/) | built-in API functionality that allows RKVST to connect to third party products such as Dropbox |                                                           |
| [linked folder](/platform/administration/dropbox-integration/#editing-the-list-of-linked-folders) | a folder that has been selected to be linked to RKVST during the configuration of an Integration|
| [metadata](https://en.wiktionary.org/wiki/metadata) | structured information about a file. In RKVST this metadata is recorded in the Asset and Event attributes|
| [OBAC](/platform/administration/sharing-assets-with-obac/)                | Organization-Based Access Control; policy allows sharing with the Administrator of another organization                  |
| [operation](/platform/overview/creating-an-event-against-an-asset/#creating-events)  | class of Event being erformed                                                                                       |
| [proof mechanism](/platform/overview/advanced-concepts/#proof-mechanisms)           | method by which information on the RKVST blockchain can be verified; selected when an Asset is created                                                                                       |
| [provenance](https://en.wiktionary.org/wiki/provenance) | the version and ownership history of a piece of data. With RKVST this is an immutable audit trail to prove Who Did What When to any piece of data  |
| [public asset](/platform/overview/public-attestation/)        | Assets that can be used to publicly assert data, accessible by URL without the need for an RKVST account                                                   |
| [selector](/platform/overview/creating-an-asset/#creating-an-asset)            | identifying attribute the Yaml Runner will use to check if your Asset exists already before attempting to create it  |
| [simple hash](/platform/overview/advanced-concepts/#simple-hash)            | Proof Mechanism that commits information to the RKVST blockchain in batches; value can confirm that information in the batch has not changed |
| [tenancy](/platform/overview/core-concepts/#tenancies)             | an organization’s private area within RKVST, containing Asset and Event data                                         |
| [tenant display name](/platform/administration/identity-and-access-management/#tenant-display-name) | displayed only within own Tenancy for easy identification and switching |
| [unlinked folder](/platform/administration/dropbox-integration/#editing-the-list-of-linked-folders) | a folder that has not been selected to be linked to RKVST during the configuration or reconfiguration of an Integration                                              |
| [verified domain](/platform/administration/verified-domain/)     | Tenancy name visible to others in place of the tenancy ID when viewing the Asset Overview of a public Asset or a shared private Asset. Must be verified by the RKVST team                                        |
| [verified organization](/platform/administration/verified-domain/)| an organization which has subscribed to a paid tier and who has had their domain verified and displayed in place of their tenancy ID in the Asset Overview |
