---
title: "Reserved Attributes"
description: ""
lead: ""
date: 2022-10-19T07:39:44-07:00
lastmod: 2022-10-19T07:39:44-07:00
draft: false
images: []
menu: 
  glossary:
    parent: "glossary"
weight: 52
toc: true
aliases: 
  - /docs/glossary/reserved-attributes/
---

Reserved attributes are asset attributes that are used by the DataTrails platform and have a specific purpose. All reserved attributes have the `arc_` prefix.

Select an attribute to see an example of it in use.

Asset Attributes
----------------

| **Attribute**              | **Meaning**                                                      |
|----------------------------|------------------------------------------------------------------|
| [arc_description](/developers/api-reference/assets-api/#asset-record-creation)            | brief description of Asset or Event being recorded               |
| [arc_display_name](/developers/api-reference/assets-api/#asset-record-creation)           | friendly name identifier for Assets, Events, and policies        |
| [arc_display_type](/developers/api-reference/assets-api/#asset-record-creation)           | classification of the type of Asset being traced that can be used for grouping or access control |
| [arc_home_location_identity](/platform/overview/advanced-concepts/#locations) | physical location to which an Asset nominally 'belongs'. NOT related to the Asset's position in space. For that, use `arc_gis_*` (below)                             |
| [arc_primary_image](/platform/overview/advanced-concepts/#the-primary-image) | an image attachment that will display as the thumbnail of an Asset                                |

Event Attributes
----------------

| **Attribute**              | **Meaning**                                                      |
|----------------------------|------------------------------------------------------------------|
| [arc_correlation_value](/platform/administration/compliance-policies/#creating-a-compliance-policy)      | links Events together for evaluation in Compliance Policies             |
| [arc_gis_lat](/platform/overview/advanced-concepts/#locations)      | tags the Event as having happened at a particular latitude. Used in the DataTrails UI for mapping             |
| [arc_gis_lng](/platform/overview/advanced-concepts/#locations)      | tags the Event as having happened at a particular longitude. Used in the DataTrails UI for mapping             |
| [arc_description](/developers/api-reference/events-api/#event-creation)            | brief description of the Event being recorded               |
| [arc_display_type](/developers/api-reference/events-api/#event-creation)           | classification of the type of Event being performed that can be used for grouping or access control |
| [arc_primary_image](/platform/overview/advanced-concepts/#the-primary-image) | an image attachment that will display as the thumbnail of the Event                               |
