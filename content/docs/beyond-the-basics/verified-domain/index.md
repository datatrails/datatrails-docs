---
 title: "Verified Domain"
 description: "Domain Verification and Why It's Important"
 lead: "Domain Verification and Why It's Important"
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

## What is domain verification?

Domain verification assures that actors claiming to be part of an organization are authorized to share information on their behalf. If an organization's tenancy has been verified by the RKVST team, a badge indicating that they have been verified will appear next to their domain name.

{{< note >}}
**Note:** Having a verified domain is different from a `Tenant Display Name`. Tenant display names are internal, appearing only within your own tenancy, and are not visible to anyone you share with. A verified domain name must be set by the RKVST team, and will be visible to actors outside your tenancy. 
{{< /note >}}

## Why is it important to verify my organization's domain?

Getting your organization's domain verified indicates that you are who you say you are to those you wish to share with. This helps close the trust gap inherent to information sharing between organizations or with the public.

Without domain verification, the `Organisation` is noted as the publisher's Tenant ID. Verifying your domain not only shows that this information comes from a legitimate actor on behalf of the organization, but also replaces the Tenant ID with your domain name so consumers can more easily identify the publishing organization. For example, someone attesting information on behalf of RKVST would have `rkvst.com`. 

{{< img src="UnverifiedDomain.png" alt="Rectangle" caption="<em>Organisation without Verified Domain</em>" class="border-0" >}}

{{< img src="VerifiedDomain.png" alt="Rectangle" caption="<em>Organisation with Verified Domain</em>" class="border-0" >}}

## How can I get my organization's domain verified? 

The RKVST team is happy to help you obtain your verified domain badge. Please contact support@rkvst.com from an email address which includes the domain you wish to verify. For example, email us from @rkvst.com to verify the rkvst.com domain. 

## Checking the Verified Domain of an External Organization

If an organization has a verified domain with RKVST, it will be displayed when you view a Public Asset they have published. You may also retrieve this information via the API if you know the organization's Tenant ID.

```bash
curl -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     https://app.rkvst.io/archivist/v1/tenancies/{uuid}:publicinfo
```