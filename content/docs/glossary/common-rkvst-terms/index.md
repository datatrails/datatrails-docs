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
| [ABAC](https://docs.rkvst.com/docs/rkvst-basics/managing-access-to-an-asset-with-abac/)                | Attribute-Based Access Control; policy that allows you to grant fine-grain access to members of your tenancy         |
| [access policy](https://docs.rkvst.com/docs/overview/core-concepts/#access-policies)       | grants chosen asset and event access to stakeholders                                                                 |
| [app registration](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/#creating-an-app-registration)    | client ID and client secret credentials that are used to access the RKVST API                                        |
| [asset](https://docs.rkvst.com/docs/overview/core-concepts/#assets)               | an RKVST asset is an entry in your tenancy, which has a collection of attributes that describes its current state and a complete life history of events |
| [asset_attributes](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)    | key-value pairs that represent information about an asset                                                            |
| [bearer token](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)        | access token for RKVST API; created using app registration credentials                                               |
| [behaviours](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)          | detail what class of events in an asset lifecycle you might wish to record                                           |
| [compliance policy](https://docs.rkvst.com/docs/beyond-the-basics/compliance-policies/)   | user-defined rule sets that assets can be tested against                                                             |
| [event](https://docs.rkvst.com/docs/overview/core-concepts/#events)               | tracks key moments of an asset lifecycle; details of Who Did What When to an Asset                                   |
| [event_attributes](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/#creating-events)    | key-value pairs that represent information about an event                                                            |
| [OBAC](https://docs.rkvst.com/docs/rkvst-basics/sharing-assets-with-obac/)                | Organization-Based Access Control; policy allows sharing with the root user of another organization                  |
| [operation](https://docs.rkvst.com/docs/rkvst-basics/creating-an-event-against-an-asset/#creating-events)           | class of event being performed                                                                                       |
| [public asset](https://docs.rkvst.com/docs/beyond-the-basics/public-attestation/)        | assets that can be used to publicly assert data, accessible by URL without the need for an RKVST account                                                   |
| [root user](https://docs.rkvst.com/docs/rkvst-basics/getting-access-tokens-using-app-registrations/#creating-an-app-registration)           | user with permission to see all asset and event information within a tenancy, and to grant access to other users     |
| [selector](https://docs.rkvst.com/docs/rkvst-basics/creating-an-asset/#creating-an-asset)            | identifying attribute the yaml runner will use to check if your asset exists already before attempting to create it  |
| [tenancy](https://docs.rkvst.com/docs/overview/core-concepts/#tenancies)             | an organization’s private area within RKVST, containing asset and event data                                         |
| [tenant display name](https://docs.rkvst.com/docs/beyond-the-basics/verified-domain/) | displayed only within own tenancy for easy identification and switching                                              |
| [verified domain](https://docs.rkvst.com/docs/beyond-the-basics/verified-domain/)     | tenancy name visible to others you share with; must be verified by RKVST team                                        |