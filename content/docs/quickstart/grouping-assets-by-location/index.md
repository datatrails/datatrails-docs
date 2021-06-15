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

Locations associate an Asset with a 'home' that can help when governing sharing policies with OBAC and ABAC. Locations do not need pinpoint precision and can be named by site, building or other logical grouping.

It may still be useful to indicate an Asset's origin. For example, if tracking traveling consultant's Laptops, you may still wish to associate them with a 'home' office.


## Creating a Location

1. In the Dashboard select `Add Location` in the Sidebar.

{{< img src="LocationAdd.png" alt="Rectangle" caption="<em>Adding a Location</em>" class="border-0" >}}

2. The following screen will appear:

{{< img src="LocationDescribe.png" alt="Rectangle" caption="<em>The Location Webform</em>" class="border-0" >}}

3. Enter both the required Location Name and Address here.

{{< img src="LocationForm.png" alt="Rectangle" caption="<em>Adding the Location Details</em>" class="border-0" >}}

4. There is an option to add Extended Attributes to a Location using the `Extended Attributes` Tab. 

This is useful to add metadata to a Location, e.g. a site contact's number and email address.

{{< img src="LocationAttributes.png" alt="Rectangle" caption="<em>Adding Extended Attributes to a Location</em>" class="border-0" >}}

5. Once completed and all details entered, click `Create Location`.

{{< img src="LocationSubmitted.png" alt="Rectangle" caption="<em>Submitting a Location</em>" class="border-0" >}}

6. Navigate to `Manage Locations` in the Sidebar to see a list of existing Locations.

{{< img src="LocationView.png" alt="Rectangle" caption="<em>Managing a Location</em>" class="border-0" >}}

7. You can inspect details using the eye symbol ( ![](EyeSymbol.png) ) to the right of the Location.

{{< img src="LocationDetails.png" alt="Rectangle" caption="<em>Viewing a Location</em>" class="border-0" >}}

## Assigning a Location to an Asset

### Adding at Asset Creation

1. To assign a pre-existing Location to an Asset during Asset Creation you need only select it from the Location drop-down.

{{< img src="LocationAssetCreation.png" alt="Rectangle" caption="<em>Creating an Asset with an Existing Location</em>" class="border-0" >}}

### Adding to a pre-existing Asset

1. To assign a pre-existing asset with a new Location you need to identify the Location Identity

This is found by viewing the Location once complete using the (![](EyeSymbol.png)) to the right.

{{< img src="LocationIdentity.png" alt="Rectangle" caption="<em>Location Identity</em>" class="border-0" >}}

2. Then create an Event for the Asset and specify the identity of the new Location as noted in step 1, against the `arc_home_location_identity` key, for example:

{{< img src="LocationAssetUpdate.png" alt="Rectangle" caption="<em>Updating an Existing Asset with a new Location</em>" class="border-0" >}}

{{< note >}}
**Note** - You need to include the full `locations/<UUID>` reference as using only the `UUID` will not be recognized.
{{< /note >}}

3. In the following screenshot note the Location of our Asset has been updated.

{{< img src="LocationUpdateComplete.png" alt="Rectangle" caption="<em>Completed update of Asset Location</em>" class="border-0" >}}

