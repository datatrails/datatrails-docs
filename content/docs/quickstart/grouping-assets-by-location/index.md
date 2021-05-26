---
title: "Grouping Assets by Location"
description: ""
lead: ""
date: 2021-05-18T15:32:27+01:00
lastmod: 2021-05-18T15:32:27+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 4
toc: true
---

Locations are not always high fidelity but are useful to logically indicate an Asset's associated home, they help to organize users and the required access to assets when used ABAC and OBAC Policies to share assets.

Even if an Asset moves around it is still useful to indicate its original home, for example, if you wanted to track Laptop Assets for consultants who travelled you may still wish they are associated with a specific office. 


Creating a Location
-------------------

1. In the Dashboard select 'Add Location' in the Sidebar

{{< img src="LocationAdd.png" alt="Rectangle" caption="<em>Adding a Location</em>" class="border-0" >}}

2. The following screen will appear:

{{< img src="LocationDescribe.png" alt="Rectangle" caption="<em>The Location Webform</em>" class="border-0" >}}

3. Here you can fill out both the required Location Name and Address

{{< img src="LocationForm.png" alt="Rectangle" caption="<em>Adding the Location Details</em>" class="border-0" >}}

4. You also have the option of adding Extended Attributes to a Location using the 'Extended Attributes' Tab. This is useful to add metadata to a location, e.g. a site contact's number and email address.

{{< img src="LocationAttributes.png" alt="Rectangle" caption="<em>Adding Extended Attributes to a Location</em>" class="border-0" >}}

5. Once completed and all of the details are inputted you can then select 'Create Location'

{{< img src="LocationSubmitted.png" alt="Rectangle" caption="<em>Submitting a Location</em>" class="border-0" >}}

6. If you navigate to 'Manage Locations' in the Sidebar you should see a list of existing Locations

{{< img src="LocationView.png" alt="Rectangle" caption="<em>Managing a Location</em>" class="border-0" >}}

7. You can then use the eye symbol ( ![](EyeSymbol.png) ) to the right of the Location to investigate details of the desired Location

{{< img src="LocationDetails.png" alt="Rectangle" caption="<em>Viewing a Location</em>" class="border-0" >}}

Assigning a Location to an Asset
--------------------------------

### Adding at Asset Creation

1. To assign a pre-existing Location to an Asset during Asset Creation you need only to select it from the Location drop-down

{{< img src="LocationAssetCreation.png" alt="Rectangle" caption="<em>Creating an Asset with an Existing Location</em>" class="border-0" >}}

### Adding to a pre-existing Asset

1. To assign a pre-existing asset with a new Location you need to first identify the Location Identity, this can be found using by viewing the Location once it is completed using the (![](EyeSymbol.png)) to the right.

{{< img src="LocationIdentity.png" alt="Rectangle" caption="<em>Location Identity</em>" class="border-0" >}}

2. You then create an Event against the Asset specifying the identity of the Location as recorded in step 1, against the `arc_home_location_identity` key, for example:

{{< img src="LocationAssetUpdate.png" alt="Rectangle" caption="<em>Updating an Existing Asset with a new Location</em>" class="border-0" >}}

``` 
💡 Note - you need to include the full 'locations/<UUID>' reference
   RKVST will not recognise only the 'UUID'
```

3. As we can see in the following screenshot, the Location of our Asset has been updated

{{< img src="LocationUpdateComplete.png" alt="Rectangle" caption="<em>Completed update of Asset Location</em>" class="border-0" >}}

