---
title: "Configuring Clients for Non-Interactive Use"
description: "Creating Clients for RKVST"
lead: "Creating Clients for RKVST"
date: 2021-06-16T11:12:25+01:00
lastmod: 2021-06-16T11:12:25+01:00
draft: false
images: []
menu: 
  docs:
    parent: "setup-and-administration"
weight: 12
toc: true
---

To enable non-interactive access to RKVST APIs:

* Create an Application Registration in your archivist.

## Create an Application Registration

* Visit the APP REGISTRATIONS tab on the Manage RKVST page in the archivist ui.
* Click CREATE APP REGISTRATION.
* Enter any display name you like.
* Optional - using the ADD CUSTOM CLAIM button Add any extra claims you require in your access token.
* Click CREATE APP REGISTRATION. The response will include the CLIENTID and
  SECRET required by the archivist token endpoint.

You MUST take note of the secret - it can not be viewed again.
