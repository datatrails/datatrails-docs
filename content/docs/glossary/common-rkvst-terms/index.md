---
title: "Common RKVST Terms"
description: ""
lead: ""
date: 2022-10-19T07:39:44-07:00
lastmod: 2022-10-19T07:39:44-07:00
draft: false
images: []
menu: 
  docs:
    parent: "glossary"
weight: 51
toc: true
---

Select a term for more information.

| **Term**            | **Definition**                                                                                                       |
|---------------------|----------------------------------------------------------------------------------------------------------------------|
| [ABAC](https://docs.rkvst.com/docs/rkvst-basics/managing-access-to-an-asset-with-abac/)                | Attribute-Based Access Control; policy that allows you to grant fine-grain access to members of your Tenancy         |
| [access policy](https://docs.rkvst.com/docs/overview/core-concepts/#access-policies)       | grants chosen Asset and Event access to stakeholders                                                                 |
| [administrator](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/#creating-an-app-registration)           | user with permission to see all Asset and Event information within a Tenancy, and to grant access to other users     |
| [app registration](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/#creating-an-app-registration)    | client ID and client secret credentials that are used to access the RKVST API                                        |
| [asset](https://docs.rkvst.com/docs/overview/core-concepts/#assets)               | an RKVST Asset is an entry in your tenancy, which has a collection of attributes that describes its current state and a complete life history of Events |
| [asset_attributes](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)    | key-value pairs that represent information about an Asset                                                            |
| [bearer token](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)        | access token for RKVST API; created using App Registration credentials                                               |
| [behaviours](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)          | detail what class of events in an Asset lifecycle you might wish to record                                           |
| [compliance policy](https://docs.rkvst.com/docs/beyond-the-basics/compliance-policies/)   | user-defined rule sets that Assets can be tested against                                                             |
| [event](https://docs.rkvst.com/docs/overview/core-concepts/#events)               | tracks key moments of an Asset lifecycle; details of Who Did What When to an Asset                                   |
| [event_attributes](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/#creating-events)    | key-value pairs that represent information about an Event                                                            |
| [khipu](https://docs.rkvst.com/docs/overview/advanced-concepts/#khipu)    | Proof Mechanism that commits information directly to the RKVST blockchain so it can be verified any time after it is confirmed                                                            |
| [OBAC](https://docs.rkvst.com/docs/rkvst-basics/sharing-assets-with-obac/)                | Organization-Based Access Control; policy allows sharing with the Administrator of another organization                  |
| [operation](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/#creating-events)           | class of Event being performed                                                                                       |
| [proof mechanism](https://docs.rkvst.com/docs/overview/advanced-concepts/#proof-mechanisms)           | method by which information on the RKVST blockchain can be verified; selected when an Asset is created                                                                                       |
| [public asset](https://docs.rkvst.com/docs/beyond-the-basics/public-attestation/)        | Assets that can be used to publicly assert data, accessible by URL without the need for an RKVST account                                                   |
| [selector](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)            | identifying attribute the Yaml Runner will use to check if your Asset exists already before attempting to create it  |
| [simple hash](https://docs.rkvst.com/docs/overview/advanced-concepts/#simple-hash)            | Proof Mechanism that commits information to the RKVST blockchain in batches; value can confirm that information in the batch has not changed |
| [tenancy](https://docs.rkvst.com/docs/overview/core-concepts/#tenancies)             | an organization’s private area within RKVST, containing Asset and Event data                                         |
| [tenant display name](https://docs.rkvst.com/docs/overview/identity-and-access-management/#tenant-display-name) | displayed only within own Tenancy for easy identification and switching                                              |
| [verified domain](https://docs.rkvst.com/docs/beyond-the-basics/verified-domain/)     | Tenancy name visible to others you share with; must be verified by RKVST team                                        |