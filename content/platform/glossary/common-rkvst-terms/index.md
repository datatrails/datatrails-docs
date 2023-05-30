---
title: "Common RKVST Terms"
description: ""
lead: ""
date: 2022-10-19T07:39:44-07:00
lastmod: 2022-10-19T07:39:44-07:00
draft: false
images: []
menu: 
  platform:
    parent: "glossary"
weight: 51
toc: true
---

Select a term for more information.

| **Term**            | **Definition**                                                                                                       |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| [ABAC](/platform/rkvst-basics/managing-access-to-an-asset-with-abac/)                | Attribute-Based Access Control; policy that allows you to grant fine-grain access to members of your Tenancy         |
| [access policy](/platform/overview/core-concepts/#access-policies)       | grants chosen Asset and Event access to stakeholders                                                                 |
| [administrator](/platform/rkvst-basics/getting-access-tokens-using-app-registrations/#creating-an-app-registration)           | user with permission to see all Asset and Event information within a Tenancy, and to grant access to other users     |
| [app registration](/platform/rkvst-basics/getting-access-tokens-using-app-registrations/#creating-an-app-registration)    | client ID and client secret credentials that are used to access the RKVST API                                        |
| [anchored](/platform/beyond-the-basics/verifying-with-simple-hash/)  | Simple Hash events are committed to the blockchain by hashing them in batches. The hash recorded on the chain is called the anchor |
| [asset](/platform/overview/core-concepts/#assets)               | an RKVST Asset is an entry in your tenancy, which has a collection of attributes that describes its current state and a complete life history of Events |
| [asset_attributes](/platform/rkvst-basics/creating-an-asset/#creating-an-asset)    | key-value pairs that represent information about an Asset                                                            |
| [bearer token](/platform/rkvst-basics/creating-an-asset/#creating-an-asset)        | access token for RKVST API; created using App Registration credentials                                               |
| [behaviours](/platform/rkvst-basics/creating-an-asset/#creating-an-asset)          | detail what class of events in an Asset lifecycle you might wish to record                                           |
| [compliance policy](/platform/beyond-the-basics/compliance-policies/)   | user-defined rule sets that Assets can be tested against                                                             |
| [event](/platform/overview/core-concepts/#events)               | tracks key moments of an Asset lifecycle; details of Who Did What When to an Asset                                   |
| [event_attributes](/platform/rkvst-basics/creating-an-event-against-an-asset/#creating-events)    | key-value pairs that represent information about an Event                                                            |
| [khipu](/platform/overview/advanced-concepts/#khipu)    | Proof Mechanism that commits information directly to the RKVST blockchain so it can be verified any time after it is confirmed                                                            |
| [OBAC](/platform/rkvst-basics/sharing-assets-with-obac/)                | Organization-Based Access Control; policy allows sharing with the Administrator of another organization                  |
| [operation](/platform/rkvst-basics/creating-an-event-against-an-asset/#creating-events)           | class of Event being performed                                                                                       |
| [proof mechanism](/platform/overview/advanced-concepts/#proof-mechanisms)           | method by which information on the RKVST blockchain can be verified; selected when an Asset is created                                                                                       |
| [public asset](/platform/beyond-the-basics/public-attestation/)        | Assets that can be used to publicly assert data, accessible by URL without the need for an RKVST account                                                   |
| [selector](/platform/rkvst-basics/creating-an-asset/#creating-an-asset)            | identifying attribute the Yaml Runner will use to check if your Asset exists already before attempting to create it  |
| [simple hash](/platform/overview/advanced-concepts/#simple-hash)            | Proof Mechanism that commits information to the RKVST blockchain in batches; value can confirm that information in the batch has not changed |
| [tenancy](/platform/overview/core-concepts/#tenancies)             | an organization’s private area within RKVST, containing Asset and Event data                                         |
| [tenant display name](/platform/overview/identity-and-access-management/#tenant-display-name) | displayed only within own Tenancy for easy identification and switching                                              |
| [verified domain](/platform/beyond-the-basics/verified-domain/)     | Tenancy name visible to others you share with; must be verified by RKVST team                                        |