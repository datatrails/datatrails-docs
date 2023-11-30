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

1. Using the sidebar, select `Instaproof`and then drag a document into the search area
{{< img src="InstaproofStart.png" alt="Rectangle" caption="<em>Instaproof Search Area</em>" class="border-0" >}}
1. **Document not found**  
If the document that you are verifying has not been found, you will see a red response banner.
{{< img src="InstaproofNotFound.png" alt="Rectangle" caption="<em>Document Not Found</em>" class="border-0" >}}
  The possible reasons for this outcome are:

   * The document owner has not registered the document in their DataTrails tenancy
   * The document owner has not published this version of the document as an event
   * The document has been modified since it was registered with DataTrails

   In all cases you should contact the document owner to find out whether your document version can be trusted.

1. **Document Found**
{{< note >}}
**Note:** In this screenshot we are using the file `greenfrog.jpg` which can be downloaded from our [Instaproof Samples](https://github.com/datatrails/instaproof-samples/tree/main/media) page.
{{< /note >}}
If the document has been registered with DataTrails, you will see a green response banner together with a list of all the matching Document Profile Assets. This means that the version of the document that you have has a verifiable provenance record and an immutable audit trail.
{{< img src="InstaproofFound.png" alt="Rectangle" caption="<em>Document Found</em>" class="border-0" >}}
At the top you can see the document that was checked and found on Instaproof. Don't worry! It's all kept locally - we don't need to peek inside your documents to find their provenance.  

    You can check additional documents by dragging them on top of here.

    Some of the results may be from verified organizations and others from unverified members of the DataTrails community. All results contribute something to the provenance and life history of this document.

    A **Verified Organization** has a [verified domain](/platform/administration/verified-domain/) associated with their DataTrails account. This helps to confirm the identity of the document source and is likely the thing to look for if you want 'official' provenance records.

    The **Other Results** results are those from from unverified DataTrails accounts - other members of the DataTrails community who have made claims or observations about the document you're interested in.

    While they may seem less 'official' than verified account results, they may still be useful to you. The identity of all users making attestations in DataTrails is checked, recorded, and immutable, even if they are not (yet) associated with a verified domain name.

### What Do the Instaproof Results Mean

#### Immutable Audit Trail

Click on a result to see details of the document history. You will see the Event details of the version that matches your document on the right with a partial view of the Asset details for the latest version on the left. Close the Event details to see the full Asset details view.

{{< img src="InstaproofResults.png" alt="Rectangle" caption="<em>Asset Details Tab</em>" class="border-0" >}}

The **Asset details** tab shows the information about the asset attributes.
Includes the current version, the organization, and Verified Domain badge, if applicable. 

**Public attestation and visibility** - *Public* means that the document is publicly accessible using the public URL. *Permissioned* means that it is private and requires shared access to be enabled for a user to be able to view it.

**Type** - For Document Profile Assets this will always be 'Document'.

**Description** - an optional description of the Asset

**Attributes** - This drop down section contains any custom attributes that were added to the asset.

**Versions** - the published versions of the document

{{< note >}}
**Note:**
The share button allows you to access and copy the private and public (if enabled) links for the asset to share with other users. Private links are for logged in users with assigned permissions, Public links are for everyone.
{{< /note >}}

{{< img src="InstaproofShare.png" alt="Rectangle" caption="<em>Share Links</em>" class="border-0" >}}

The **Event History** tab shows the full history of Events including custom Events, new Versions and Withdraw Events.

Click on the tab and select an Event to view the details.

{{< img src="InstaproofResultsDetails.png" alt="Rectangle" caption="<em>Event History Overview Tab</em>" class="border-0" >}}

The **Overview** information about the Event

**Event Identity** -  The Event ID will always be of the format 'publicassets/<asset_id>/events/<event_id>' for public assets or 'assets/<asset_id>/events/<event_id>' for private assets.

**Asset Identity** - the ID of the parent Asset for this Event.

**Transaction** - This link contains the details of the blockchain transaction.
{{< img src="InstaproofTransaction.png" alt="Rectangle" caption="<em>Transaction Details</em>" class="border-0" >}}

**Type** - For Document Profile Events this will always be 'Publish'

**Document changes** - The version and document hash for new version Events. There is no data here for custom Events. 

The **Event attributes** and **Asset attributes** tabs contain information about any custom attributes that were added or modified as part this Event. 


