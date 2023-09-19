---
title: "Instaproof"
description: "A Guide to Instaproof"
lead: ""
date: 2023-07-18T12:10:19+01:00
lastmod: 2023-07-18T12:10:19+01:00
draft: false
images: []
menu: 
  platform:
    parent: "overview"
weight: 37
toc: true
---
Instaproof provides data provenance and authenticity with a simple drag-and-drop. 

Instaproof will search amongst the assets that have been registered with the document profile and return a list of all assets that have a matching hash value.

The initial version of a document is registered as a document profile asset. New versions of the document are published as events against that asset. See [Document Profile](/developers/developer-patterns/document-profile) more more information.

### Using the Instaproof UI
1. **Open Instaproof**. 

Using the sidebar, select `Instaproof`and then drag a document into the search area.
{{< img src="InstaproofStart.png" alt="Rectangle" caption="<em>Instaproof Search Area</em>" class="border-0" >}}


2. **Document not found**.

If the document that you are verifying has not been found, you will see a red response banner.
{{< img src="InstaproofNotFound.png" alt="Rectangle" caption="<em>Document Not Found</em>" class="border-0" >}}

The possible reasons for this outcome are:
* The document owner has not registered the document in their RKVST tenancy.
* The document owner has not published this version of the document as an event.
* The document has been modified since it was registered with RKVST!

In all cases you should contact the document owner to find out whether your document version can be trusted.

3. **Document Found**.

{{< note >}}
**Note:** In this screenshot we are using the file `greenfrog.jpg` which can be downloaded from our [Instaproof Samples](https://github.com/rkvst/instaproof-samples/tree/main/media) page.
{{< /note >}}

If the document has been registered with RKVST, you will see a green response banner together with a list of all the matching Document Profile Assets. This means that the version of the document that you have has a verifiable provenance record.

{{< img src="InstaproofFound.png" alt="Rectangle" caption="<em>Document Found</em>" class="border-0" >}}

At the top you can see the document that was checked and found on Instaproof. Don't worry! It's all kept locally - we don't need to peek inside your documents to find their provenance.

You can check additional documents by dragging them on top of here. 

Some of the results may be from verified organizations and others from unverified members of the RKVST community. All results contribute something to the provenance and life history of this document. 

A **Verified Organization** has a [verified domain](/platform/administration/verified-domain/) associated with their RKVST account. This helps to confirm the identity of the document source and is likely the thing to look for if you want 'official' provenance records.

The **Other Results** results are those from from unverified RKVST accounts - other members of the RKVST community who have made claims or observations about the document you're interested in. 

While they may seem less 'official' than verified account results, they may still be useful to you. The identity of all users making attestations in RKVST is checked, recorded, and immutable, even if they are not (yet) associated with a verified domain name. 

### What do the Instaproof results mean?

1. **Provenance Record** 

Click on a result to see details of the provenance record.

{{< img src="InstaproofResults.png" alt="Rectangle" caption="<em>Document Results Tab</em>" class="border-0" >}}

The **Document** tab shows the asset and event attributes that relate to the document profile.

**Public** - If this is green then the document is publicly accessible using the public URL. Otherwise it is private and requires shared access to be enabled for a user to be able to view it.

**Tick** - The anchor status of the document on the blockchain. A blue tick means that is has been anchored.

**Details** - The current version, the parent asset link (to the original version), the organization and Verified Domain badge, if applicable.

**Compare Local Copy** - Drag a copy here if you have a local copy of the document and you don't know which version it is. You do this by clicking on a version in the **Browse Events** section and then dragging a file to find if it matches this version.
{{< img src="InstaproofLocalCopy.png" alt="Rectangle" caption="<em>Comparing a Local Copy</em>" class="border-0" >}}

The **More Details** tab shows the asset details and attributes that are common to all RKVST assets.

{{< img src="InstaproofResultsDetails.png" alt="Rectangle" caption="<em>More Details Results Tab</em>" class="border-0" >}}

**Type** - The type of event. For Document Profile Events this will always be 'Publish'.

**Description** - An optional decription of the event.

**Event ID** -  The Event ID will always be of the format 'publicassets/<asset_id>/events/<event_id>' for public assets or 'assets/<asset_id>/events/<event_id>' for private assets.

**Attributes** - This section contains any custom attributes that were included added when the asset was created or when the current event was added to the asset.

**Transaction** - This link contains the details of the blockchain transaction.
{{< img src="InstaproofTransaction.png" alt="Rectangle" caption="<em>Transaction Details</em>" class="border-0" >}}

{{< note >}}
**Note:**
The share button allows you to access and copy the private and public (if enabled) links for the asset to share with other users. Private links are for logged in users with assigned permissions, Public links are for everyone.
{{< /note >}}

{{< img src="InstaproofShare.png" alt="Rectangle" caption="<em>Share Links</em>" class="border-0" >}}

