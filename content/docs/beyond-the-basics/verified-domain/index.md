---
 title: "Verified Domains"
 description: "Association of Tenant Identity and Verified Name"
 lead: "How to Get Your Domain Verified and Check Other Domains"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   docs:
     parent: "beyond-the-basics"
 weight: 43
 toc: true
---

## Getting Your Domain Verified

## Verifying the Actor for a Publicly Attested Asset or Event
First you get the sbom/asset/event via the api
then you extract the tenantid from the response
then you extract the uuid from the tenantid
then you call `/archivist/v1/tenancies/{uuid}:publicinfo
this gives you the verified domain

1. Get the desired Public Asset or Event. 

{{< tabs name="get_asset_verified_domain" >}}
{{{< tab name="UI" >}}
Select `Manage Assets` from the sidebar.
#change to screenshot with button highlight
{{< /tab >}}
{{< tab name="JSON" >}}
Create an empty file, in later steps we will add the correct JSON.

```json
{
  
}
```
{{< /tab >}}
{{< /tabs >}}

## How does RKVST verify domains? 
