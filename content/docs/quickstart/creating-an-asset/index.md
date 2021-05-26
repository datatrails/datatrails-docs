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
weight: 2
toc: true
---

As discussed in the previous section, An Asset can be anything: an IOT Sensor, a Shipping Container or even a Purchase Order. Any kind of object, physical or otherwise, which has a Name, Description and Attributes associated with it.

More than this though an Asset is also the sum of it's history, any change it has been through and any action against it.

In that regard you may consider the creation of an Asset to be the first event in its lifecycle, the following steps will walk you through creating your first asset.

Creating an Asset
--------------

1. In the UI, using the Sidebar, select 'Add Asset'

{{< img src="AssetAdd.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}


2. You will be presented with the following screen, where you can provide the details of your Asset:

{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}

3. You will need to at least add the Asset Name and Asset Type when using the UI to create an Asset

* Asset Name - This is the unique name of the Asset i.e. 'My First Container'
* Asset Type - This is the class of object, while this is arbitrary it is best to have consistency amongst the type of Assets you use i.e. if it is a shipping container the type could be 'Shipping Container' which will then be prepopulated for future Assets to use as their own types

{{< img src="AssetCreationDetails.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}

4. It is at this point you may wish to add any other details to your Asset, including attaching any kind of PDF or maybe Image an image to show the asset. You may even wish to add some Extended Attributes. 

Extended Attributes are Custom Attributes that can be added per Unique Asset. Not all Assets of a specific type need to have the exact same Extended Attributes but in most cases it is better to do so for posterity. To add a new attribute to an asset you just need to select 'Add Attribute' and then type in your key-value pair.

For Example:

{{< img src="AssetExtendedAttributes.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}

5. Once complete you can then hit 'Create Asset'

{{< img src="AssetCreate.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}

6. Now if you navigate to Manage Assets you should be able to see your Asset in the UI

{{< img src="AssetManage.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}

7. If you wish to view your Asset you can click on the small eye symbol ( ![](EyeSymbol.png) ) to the right of the Asset in the manage view, this will show you the detailed history of your asset.

{{< img src="AssetView.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}

Here we can see all of the details we filled out earlier, we can also see the custom attributes we added and a history of the events against the asset, the first event should always be the Asset Creation event, in the next section we will cover how to create your own events against your asset.

