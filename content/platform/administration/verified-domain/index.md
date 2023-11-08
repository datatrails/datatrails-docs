---
 title: "Verified Domain"
 description: "Domain Verification and Why It's Important"
 lead: "Domain Verification and Why It's Important"
 date: 2021-05-18T14:52:25+01:00
 lastmod: 2021-05-18T14:52:25+01:00
 draft: false
 images: []
 menu:
   platform:
     parent: "administration"
 weight: 42
 toc: true
 aliases:
  - /docs/beyond-the-basics/verified-domain/
---

## What is domain verification?

Domain verification assures that actors claiming to be part of an organization are authorized to share information on their behalf. If an organization's Tenancy has been verified by the DataTrails team, a badge indicating that they have been verified will appear next to their domain name.

{{< note >}}
**Note:** Having a verified domain is different from a `Tenant Display Name`. Tenant display names are internal, appearing only within your own Tenancy, and are not visible to anyone you share with. A verified domain name must be set by the DataTrails team, and will be visible to actors outside your Tenancy.
{{< /note >}}

## Why is it important to verify my organization's domain?

Getting your organization's domain verified indicates that you are who you say you are. This helps close the trust gap inherent to information sharing between organizations or with the public.

Without domain verification, the `Organization` is noted as the publisher's Tenant ID. Verifying your domain not only shows that this information comes from a legitimate actor on behalf of the organization, but also replaces the Tenant ID with your domain name so consumers can more easily identify the publishing organization. For example, someone attesting information on behalf of DataTrails would have `datatrails.com`.

{{< img src="UnverifiedDomain.png" alt="Rectangle" caption="<em>Organization without Verified Domain</em>" class="border-0" >}}

{{< img src="DomainBadge.png" alt="Rectangle" caption="<em>Organization with Verified Domain</em>" class="border-0" >}}

## How can I get my organization's domain verified?

The DataTrails team is happy to help you obtain your verified domain badge. Please contact support@datatrails.com from an email address which includes the domain you wish to verify. For example, email us from @datatrails.com to verify the datatrails.com domain.

In order to protect our user community, it is important for us to verify that the person making the request is authorized to do so by the owner of the domain. We will request evidence from you to prove that you own or control the domain in question. Typically, this will be in the form of public company information or domain registration records. Please be prepared to share this evidence with us.

## Checking the Verified Domain of an External Organization

If an organization has a verified domain with DataTrails, it will be displayed when you view a Public Asset they have published. You may also retrieve this information via the API if you know the organization's Tenant ID.

```bash
curl -v -X GET \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     https://app.datatrails.ai/archivist/v1/tenancies/{uuid}:publicinfo
```
