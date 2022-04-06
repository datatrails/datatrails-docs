---
title: "Grouping Assets by Location"
description: "Adding a Location"
lead: "Adding a Location"
date: 2021-05-18T15:32:27+01:00
lastmod: 2021-05-18T15:32:27+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 23
toc: true
---

Locations associate an Asset with a 'home' that can help when governing sharing policies with OBAC and ABAC. Locations do not need pinpoint precision and can be named by site, building or other logical grouping.

It may still be useful to indicate an Asset's origin. For example, if tracking traveling consultant's Laptops, you may still wish to associate them with a 'home' office.


## Creating a Location

1. Create your Location.


{{< tabs name="add_location" >}}
{{{< tab name="UI" >}}
In the Dashboard, select `Add Location` in the Sidebar.
{{< img src="LocationAdd.png" alt="Rectangle" caption="<em>Adding a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
The RKVST YAML runner is executed as a series of steps, each step representing a single operation with an `action`.

In order to create a Location, we use the action `LOCATIONS_CREATE_IF_NOT_EXISTS`.
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
```
{{< /tab >}}}
{{< /tabs >}}


2. Add information about the Location you are creating. 

{{< tabs name="add_location_info" >}}
{{{< tab name="UI" >}}
The following screen will appear:
{{< img src="LocationDescribe.png" alt="Rectangle" caption="<em>The Location Webform</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
You may add a `description` and a `selector`. `selector` is the identifying attribute the YAML runner will use to check if your asset exists before attempting to create it. In this case, we use `display_name` which represents the name of the Location.
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create UK factory location. 
    selector:
      - display_name
```
{{< /tab >}}}
{{< /tabs >}}


3. Enter the required Location Name and Address, or in the case of the YAML Runner, Coordinates.

{{< tabs name="add_location_name" >}}
{{{< tab name="UI" >}}
{{< img src="LocationForm.png" alt="Rectangle" caption="<em>Adding the Location Details</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
`latitude` and `longitude` pinpoint the Location when using the YAML Runner. 
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create UK factory location. 
    selector:
      - display_name
    display_name: UK Factory
    description: Factory in Bristol Harbor
    latitude: 51.4477
    longitude: -2.5980
```
{{< /tab >}}}
{{< /tabs >}}



4. There is an option to add Extended Attributes to a Location. This is useful to add metadata to a Location, e.g. a site contact's number and email address.

{{< tabs name="add_location_attributes" >}}
{{{< tab name="UI" >}}
Use the `Extended Attributes` Tab.
{{< img src="LocationAttributes.png" alt="Rectangle" caption="<em>Adding Extended Attributes to a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Extended attributes may also be added to your YAML file. 
 
```yaml
---
steps:
  - step:
      action: LOCATIONS_CREATE_IF_NOT_EXISTS
      description: Create UK factory location. 
    selector:
      - display_name
    display_name: UK Factory
    description: Factory in Bristol Harbor
    latitude: 51.4477
    longitude: -2.5980
    attributes:
      address: Princes Wharf, Wapping Rd, Bristol BS1 4RN, UK
      Primary_Contact: Jill Tiller
      Primary_Mobile_Number: +447700900077
```
{{< /tab >}}}
{{< /tabs >}}




5. Complete your Location. 

{{< tabs name="complete_location" >}}
{{{< tab name="UI" >}}
Click `Create Location`.
{{< img src="LocationSubmitted.png" alt="Rectangle" caption="<em>Submitting a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Use the [archivist_runner](https://python.rkvst.com/runner/index.html) to run your YAML file!
 
```bash
$ archivist_runner \
      -u https://app.rkvst.io \
      --client-id <your-client-id> \
      --client-secret client_secret.txt \
      UK_factory_location.yaml
```
{{< /tab >}}}
{{< /tabs >}}


6. View a list of your existing Locations.

{{< tabs name="list_locations" >}}
{{{< tab name="UI" >}}
Navigate to `Manage Locations` in the Sidebar to see a list of existing Locations.
{{< img src="LocationView.png" alt="Rectangle" caption="<em>Managing a Location</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
###yaml action to list locations?###
 
```yaml
need added capability
```
{{< /tab >}}}
{{< /tabs >}}



7. You can inspect details of a single Location.

{{< tabs name="location_details" >}}
{{{< tab name="UI" >}}
Click the desired Location row. 
{{< img src="LocationDetails.png" alt="Rectangle" caption="<em>Viewing a Location</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
###yaml action to list locations?###
 
```yaml
need added capability
```
{{< /tab >}}}
{{< /tabs >}}


## Assigning a Location to an Asset

### Adding at Asset Creation

1. To assign a pre-existing Location to an Asset during Asset creation, you need only select it. 

{{< tabs name="add_at_asset_create" >}}
{{{< tab name="UI" >}}
Choose the desired Location from the Location drop-down.
{{< img src="LocationAssetCreation.png" alt="Rectangle" caption="<em>Creating an Asset with an Existing Location</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
A pre-exisitng Location can be added during Asset creation, using the Location ID as an identifier. 
```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset with pre-existing Location. 
      asset_label: My Asset 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    attributes: 
      arc_display_name: My Asset 
      arc_display_type: Example
    location: 
      selector: 
        - arc_home_location_identity
      arc_home_location_identity: <your-location-id>
    confirm: true
```
{{< /tab >}}}
{{< /tabs >}}



### Adding to a pre-existing Asset

1. To assign a pre-existing asset with a new Location, you need to identify the Location Identity. To do this, view the Location details by clicking the Location row. 

{{< img src="LocationIdentity.png" alt="Rectangle" caption="<em>Location Identity</em>" class="border-0" >}}

2. Then create an Event for the Asset and specify the identity of the new Location as noted in step 1, against the `arc_home_location_identity` key. 

{{< tabs name="add_to_asset" >}}
{{{< tab name="UI" >}}

{{< img src="LocationAssetUpdate.png" alt="Rectangle" caption="<em>Updating an Existing Asset with a new Location</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
For more information on creating Events, please visit [Creating and Event Against an Asset](https://docs.rkvst.com/docs/quickstart/creating-an-event-against-an-asset/).
```yaml
---
steps:
  - step:
      action: EVENTS_CREATE
      description: Add Location to existing Asset.
      asset_id: <your-asset-id> 
    operation: Record
    behaviour: RecordEvidence
    asset_attributes:
      arc_home_location_identity: <your-location-id>
    confirm: true
```
{{< /tab >}}}
{{< /tabs >}}


{{< note >}}
**Note** - You need to include the full `locations/<UUID>` reference as using only the `UUID` will not be recognized.
{{< /note >}}

3. In the following screenshot, note the Location of our Asset has been updated.

{{< img src="LocationUpdateComplete.png" alt="Rectangle" caption="<em>Completed update of Asset Location</em>" class="border-0" >}}

