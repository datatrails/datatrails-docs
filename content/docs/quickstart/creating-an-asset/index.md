---
title: "Creating an Asset"
description: ""
lead: ""
date: 2021-05-18T14:52:25+01:00
lastmod: 2021-05-18T14:52:25+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 3
toc: true
---

An Asset can be anything: a Connected Machine, a Shipping Container or even a Data Set. It can be any physical or digital object with an associated Name, Description, and Attributes.

Each Asset will have a history of any actions performed upon it by any actor. 

The creation of an Asset is the first Event in its lifecycle. The following steps will guide you in creating your first Asset.

## Creating an Asset

1. Using the Sidebar, select `Add Asset`.

{{< img src="AssetAdd.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}

2. You will see an Asset Creation form, where you provide details of your new Asset:

{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}

3. At minimum, you will need to add an Asset Name and Asset Type when using the UI to create an Asset:

* `Asset Name` - This is the unique name of the Asset i.e. 'My First Container'
* `Asset Type` - This is the class of object, while it is arbitrary, it is best to have consistency amongst the type of Assets you use i.e. if it is a shipping container, the type could be `Shipping Container` which will then be pre-populated for future Assets to use as their own types

{{< img src="AssetCreationDetails.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}

4. At this point, you may wish to add other details to your Asset including attachments such as PDFs or Thumbnail Images. You may also wish to add Extended Attributes. 

Extended Attributes are user-defined and can be added to each unique Asset. 

Not all Assets of a specific type need to have the same Extended Attributes, but in most cases it is better to do so for consistency. 

To add a new Attribute to an Asset select `Add Attribute` then enter your key-value pair.

For Example:

{{< img src="AssetExtendedAttributes.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}

5. Once complete, click `Create Asset`

{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}

6. Navigate to `Manage Assets` to see your Asset in the UI.

{{< img src="AssetManage.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}

7. To view your Asset, click on the small eye symbol ( ![](EyeSymbol.png) ) to the right of the Asset in the Manage view. You will see the detailed history of your Asset.

{{< img src="AssetView.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}

Here we see all details entered: The Extended Attributes and a history of Events recorded on the Asset.

The first Event will always be the Asset Creation, in the next section we will cover how to create your own Events for your Asset.

